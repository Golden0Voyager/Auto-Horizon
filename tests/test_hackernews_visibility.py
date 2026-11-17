import asyncio
from datetime import UTC, datetime
from unittest.mock import AsyncMock

import pytest

from src.models import HackerNewsConfig
from src.scrapers.hackernews import HackerNewsScraper


@pytest.mark.parametrize("visibility", [{"dead": True}, {"deleted": True}, {"type": "comment"}])
def test_non_live_stories_are_not_included_or_enriched(visibility):
    scraper = HackerNewsScraper(HackerNewsConfig(min_score=0), AsyncMock())
    scraper._fetch_story = AsyncMock(return_value={
        "id": 1, "title": "Unavailable", "type": "story", "score": 1000,
        "time": 1793534400, "kids": [2], **visibility,
    })
    scraper._fetch_comments = AsyncMock(return_value=[])
    result = asyncio.run(scraper._fetch_story_item(1, datetime(2026, 10, 1, tzinfo=UTC)))
    assert result == []
    scraper._fetch_comments.assert_not_awaited()
