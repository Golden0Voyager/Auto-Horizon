"""Base scraper interface."""

from abc import ABC, abstractmethod
from collections.abc import Awaitable
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

import httpx

from ..models import ContentItem


@dataclass
class FetchResult:
    """Items and diagnostics from one fetch, including empty successful requests."""

    items: list[ContentItem] = field(default_factory=list)
    failures: dict[str, str] = field(default_factory=dict)
    successful: int = 0

    @property
    def status(self) -> Literal["success", "empty", "partial_failure", "failure"]:
        if self.failures:
            return "partial_failure" if self.successful or self.items else "failure"
        return "success" if self.items else "empty"

    def fail(self, source: str, error: Exception) -> None:
        self.failures[source] = f"{type(error).__name__}: {error}"

    async def collect(self, source: str, request: Awaitable[list[ContentItem]]) -> None:
        """Collect an independent request without losing other sources' results."""
        try:
            items = await request
        except Exception as exc:
            self.fail(source, exc)
        else:
            self.items.extend(items)
            self.successful += 1


class BaseScraper(ABC):
    """Abstract base class for all scrapers."""

    def __init__(self, config: dict, http_client: httpx.AsyncClient | None = None):
        """Initialize scraper.

        Args:
            config: Scraper-specific configuration
            http_client: Shared async HTTP client (optional for browser-based scrapers)
        """
        self.config = config
        self.client = http_client

    @property
    def http(self) -> httpx.AsyncClient:
        """The shared async HTTP client, narrowed to the non-``None`` type.

        Raises ``RuntimeError`` if no client was injected, rather than letting
        an ``AttributeError`` surface later at a ``self.client.get`` call.
        """
        if self.client is None:
            raise RuntimeError("HTTP client is required but was not provided")
        return self.client

    @abstractmethod
    async def fetch(self, since: datetime) -> FetchResult:
        """Fetch content items published since the given time.

        Args:
            since: Only fetch items published after this time

        Returns:
            FetchResult: Items, successful request count, and named failures
        """
        pass

    def _generate_id(self, source_type: str, subtype: str, native_id: str) -> str:
        """Generate unique content item ID.

        Args:
            source_type: Source type (github, hackernews, etc.)
            subtype: Content subtype (event, release, story, etc.)
            native_id: Native ID from the source platform

        Returns:
            str: Unique ID in format {source}:{subtype}:{native_id}
        """
        return f"{source_type}:{subtype}:{native_id}"
