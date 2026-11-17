"""Tests for ``src/scrapers/rss.py`` — RSS/Atom feed scraper.

Coverage targets:
- ``fetch`` — disabled short-circuit, multi-source fan-out
- ``_fetch_feed`` — env var expansion in URL, date filter, HTTP error path
- ``_parse_date`` — feedparser time_parsed tuple + parsedate_to_datetime fallback
- ``_extract_content`` — summary / description / content[0].value fallback chain
"""

import asyncio
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def _since() -> datetime:
    return datetime(2025, 12, 1, tzinfo=UTC)


def _client_with_text(text, status_code=200):
    client = AsyncMock()

    async def fake_get(url, params=None, **kw):
        resp = MagicMock()
        resp.status_code = status_code
        resp.headers = {}
        resp.text = text
        resp.content = text.encode()
        resp.raise_for_status = MagicMock(
            side_effect=Exception("http error") if status_code >= 400 else None
        )
        return resp

    client.get = fake_get
    return client


def test_fetch_returns_empty_when_all_sources_disabled():
    sources = [RSSSourceConfig(name="x", url="https://example.com/feed.xml", enabled=False)]
    scraper = RSSScraper(sources, AsyncMock())
    result = asyncio.run(scraper.fetch(_since())).items
    assert result == []


def test_fetch_parses_feed_via_feedparser(monkeypatch):
    sentinel = [
        {
            "id": "e1",
            "title": "Sentinel Post",
            "link": "https://example.com/post-1",
            "published": "Wed, 01 Jan 2026 12:00:00 GMT",
            "summary": "Body text 1",
            "author": "alice",
        }
    ]

    def fake_parse(text, **kwargs):
        return _FeedDict({"entries": [_FeedDict(e) for e in sentinel]})

    monkeypatch.setattr("feedparser.parse", fake_parse)

    sources = [RSSSourceConfig(name="x", url="https://example.com/feed.xml")]
    scraper = RSSScraper(sources, _client_with_text("<xml/>"))
    result = asyncio.run(scraper.fetch(_since())).items
    assert len(result) == 1
    assert result[0].title == "Sentinel Post"
    assert result[0].source_type.value == "rss"
    assert result[0].metadata["feed_name"] == "x"


def test_fetch_filters_old_entries(monkeypatch):
    """Entries with published_at < since are skipped."""
    sentinel = [
        {"id": "old", "title": "Old", "link": "x",
         "published": "Wed, 01 Jan 2024 12:00:00 GMT", "summary": ""},
    ]
    monkeypatch.setattr(
        "feedparser.parse",
        lambda t, **kw: _FeedDict({"entries": [_FeedDict(e) for e in sentinel]}),
    )
    sources = [RSSSourceConfig(name="x", url="https://example.com/feed.xml")]
    scraper = RSSScraper(sources, _client_with_text("<xml/>"))
    result = asyncio.run(scraper.fetch(_since())).items
    assert result == []


def test_extract_content_prefers_longest_candidate():
    """Upstream keeps the longest of content/summary/description."""
    entry = _FeedDict({"summary": "short", "description": "the longer description"})
    content = RSSScraper([RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock())._extract_content(entry)
    assert content == "the longer description"


def test_extract_content_falls_back_to_description():
    entry = _FeedDict({"description": "the description"})
    scraper = RSSScraper([RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock())
    assert scraper._extract_content(entry) == "the description"


def test_extract_content_falls_back_to_content_value():
    entry = _FeedDict({"content": [{"value": "the body"}]})
    scraper = RSSScraper([RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock())
    assert scraper._extract_content(entry) == "the body"


def test_extract_content_returns_empty_when_no_fields():
    assert RSSScraper([RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock())._extract_content({}) == ""


def test_parse_date_uses_feedparser_structured_time():
    """When ``published_parsed`` is set, that wins over the string parse path."""
    # Pass a 9-tuple directly; calendar.timegm converts to int epoch.
    entry = {
        "published_parsed": (2026, 1, 15, 12, 0, 0, 0, 0, 0),
        "published": "Mon, 01 Jan 2024 00:00:00 GMT",
    }
    scraper = RSSScraper(
        [RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock()
    )
    dt = scraper._parse_date(entry)
    assert dt is not None
    assert dt.year == 2026 and dt.month == 1 and dt.day == 15


def test_parse_date_returns_none_when_no_date_fields():
    scraper = RSSScraper([RSSSourceConfig(name="x", url="https://example.com/feed.xml")], AsyncMock())
    assert scraper._parse_date({"id": "x"}) is None


def test_fetch_expands_env_vars_in_url(monkeypatch):
    """URLs containing ``${VAR}`` placeholders are expanded from the OS environment."""
    monkeypatch.setenv("RSS_TOKEN", "secret")
    monkeypatch.setattr(
        "feedparser.parse", lambda t, **kw: _FeedDict({"entries": []})
    )

    captured_url: dict = {}

    async def fake_get(url, **kw):
        captured_url["url"] = url
        resp = MagicMock()
        resp.status_code = 200
        resp.headers = {}
        resp.text = "<xml/>"
        resp.content = b"<xml/>"
        resp.raise_for_status = MagicMock(return_value=None)
        return resp

    client = AsyncMock()
    client.get = fake_get

    sources = [RSSSourceConfig(name="x", url="https://example.com/feed?token=${RSS_TOKEN}")]
    scraper = RSSScraper(sources, client)
    asyncio.run(scraper.fetch(_since()))
    assert "secret" in captured_url["url"]



class _FeedDict(dict):
    """Dict subclass supporting attribute access like feedparser.FeedParserDict.

    Production code calls ``entry.summary`` / ``entry.description`` / ``entry.content``
    as attributes; a plain dict raises AttributeError. Tests pre-feed entries
    through this dict subclass.
    """

    def __getattr__(self, key):
        # feedparser.FeedParserDict always exposes these, defaulting them keeps
        # fake feeds shaped like real ones for the bozo/entries checks.
        if key == "bozo":
            return self.get("bozo", False)
        if key == "bozo_exception":
            return self.get("bozo_exception")
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError(key) from exc
