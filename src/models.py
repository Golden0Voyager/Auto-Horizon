"""Core data models for Horizon."""

import re
from datetime import UTC, datetime
from enum import StrEnum
from typing import Annotated, Any, Literal, NamedTuple

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator, model_validator


class SourceType(StrEnum):
    """Supported information source types."""

    GITHUB = "github"
    HACKERNEWS = "hackernews"
    RSS = "rss"
    REDDIT = "reddit"
    TELEGRAM = "telegram"
    TWITTER = "twitter"
    OPENBB = "openbb"
    OSSINSIGHT = "ossinsight"
    GDELT = "gdelt"
    GOOGLE_NEWS = "google_news"


class SourceDefinition(NamedTuple):
    """How a top-level source is represented in SourcesConfig."""

    config_field: str
    config_is_list: bool = False
    item_fields: tuple[str, ...] = ()


SOURCE_REGISTRY = {
    SourceType.GITHUB.value: SourceDefinition("github", config_is_list=True),
    SourceType.HACKERNEWS.value: SourceDefinition("hackernews"),
    SourceType.RSS.value: SourceDefinition("rss", config_is_list=True),
    SourceType.REDDIT.value: SourceDefinition("reddit", item_fields=("subreddits", "users")),
    SourceType.TELEGRAM.value: SourceDefinition("telegram", item_fields=("channels",)),
    SourceType.TWITTER.value: SourceDefinition("twitter", item_fields=("users", "keywords")),
    SourceType.OPENBB.value: SourceDefinition("openbb", item_fields=("watchlists",)),
    SourceType.OSSINSIGHT.value: SourceDefinition("ossinsight"),
    SourceType.GDELT.value: SourceDefinition("gdelt"),
    SourceType.GOOGLE_NEWS.value: SourceDefinition("google_news"),
}

ProfileRoute = str | list[str] | None


class ClassificationResult(BaseModel):
    """Resolved processing profile for a content item."""

    profile: str
    method: Literal["source_override", "ai_match"]
    confidence: float | None = Field(default=None, ge=0, le=1)
    reason: str | None = None


class ContentAnalysis(BaseModel):
    """Profile-driven first-pass analysis."""

    score: float | None = Field(default=None, ge=0, le=10, allow_inf_nan=False)
    reason: str
    summary: str
    tags: list[str] = Field(default_factory=list)


class ArtifactSource(BaseModel):
    """External source used while producing an artifact."""

    id: str
    title: str
    url: str


class ContentBlock(BaseModel):
    """A renderable section produced by an enrichment profile."""

    id: str
    type: Literal["section"] = "section"
    title: str
    content: str
    source_refs: list[str] = Field(default_factory=list)
    primary: bool = False


class ContentArtifact(BaseModel):
    """Localized, profile-defined enriched content."""

    language: str
    title: str
    blocks: list[ContentBlock] = Field(default_factory=list)
    sources: list[ArtifactSource] = Field(default_factory=list)


class ProcessingResult(BaseModel):
    """All AI processing state for a content item."""

    classification: ClassificationResult
    analysis: ContentAnalysis | None = None
    artifacts: dict[str, ContentArtifact] = Field(default_factory=dict)


class ContentItem(BaseModel):
    """Unified content item model from any source."""

    model_config = ConfigDict(extra="forbid")

    id: str  # Format: {source}:{subtype}:{native_id}
    source_type: SourceType
    title: str
    url: HttpUrl
    content: str | None = None
    author: str | None = None
    published_at: datetime
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, Any] = Field(default_factory=dict)

    # AI analysis results
    ai_score: float | None = None  # 0-10 importance score
    ai_reason: str | None = None
    ai_summary: str | None = None
    ai_tags: list[str] = Field(default_factory=list)

    # Profile-driven processing results
    profile: ProfileRoute = None
    processing: ProcessingResult | None = None


class AIProvider(StrEnum):
    """Supported AI providers."""

    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    OPENAI_CHATGPT = "openai-chatgpt"
    AZURE = "azure"
    ALI = "ali"
    GEMINI = "gemini"
    DOUBAO = "doubao"
    MINIMAX = "minimax"
    DEEPSEEK = "deepseek"
    MODELSCOPE = "modelscope"
    XIAOMIMIMO = "xiaomimimo"
    MOONSHOTAI = "moonshotai"
    OPENROUTER = "openrouter"
    GROQ = "groq"
    SILICONFLOW = "siliconflow"
    NVIDIA = "nvidia"
    SENSENOVA = "sensenova"
    OLLAMA = "ollama"


# Provider-specific defaults used by setup and provider-chain expansion.
AI_PROVIDER_DEFAULTS: dict[AIProvider, dict[str, Any]] = {
    AIProvider.ANTHROPIC: {
        "model": "claude-sonnet-5-5",
        "api_key_env": "ANTHROPIC_API_KEY",
        "base_url": None,
    },
    AIProvider.OPENAI: {
        "model": "gpt-4",
        "api_key_env": "OPENAI_API_KEY",
        "base_url": None,
    },
    AIProvider.OPENAI_CHATGPT: {
        "model": "",  # Selected from the signed-in account's model catalog.
        "api_key_env": "",
        "base_url": None,
    },
    AIProvider.AZURE: {
        "model": "gpt-4",
        "api_key_env": "AZURE_OPENAI_API_KEY",
        "base_url": None,
        "azure_endpoint_env": "AZURE_OPENAI_ENDPOINT",
        "api_version": "2024-10-21",
    },
    AIProvider.ALI: {
        "model": "qwen-plus",
        "api_key_env": "DASHSCOPE_API_KEY",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    },
    AIProvider.GEMINI: {
        "model": "gemini-3-flash-preview",
        "api_key_env": "GOOGLE_API_KEY",
        "base_url": None,
    },
    AIProvider.DOUBAO: {
        "model": "doubao-pro-32k",
        "api_key_env": "DOUBAO_API_KEY",
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    },
    AIProvider.MINIMAX: {
        "model": "MiniMax-M3.1-Flash",
        "api_key_env": "MINIMAX_API_KEY",
        "base_url": "https://api.minimax.io/v1",
    },
    AIProvider.DEEPSEEK: {
        "model": "deepseek-chat",
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url": "https://api.deepseek.com",
    },
    AIProvider.OLLAMA: {
        "model": "llama3.1",
        "api_key_env": "",
        "base_url": "http://localhost:11434/v1",
    },
    AIProvider.MODELSCOPE: {
        "model": "Qwen/Qwen3.5-35B-A3B",
        "api_key_env": "MODELSCOPE_API_KEY",
        "base_url": "https://api-inference.modelscope.cn/v1",
    },
    AIProvider.XIAOMIMIMO: {
        "model": "mimo-v2.5-pro",
        "api_key_env": "XIAOMIMIMO_API_KEY",
        "base_url": "https://mimo.xiaomi.com/api/v1",
    },
    AIProvider.MOONSHOTAI: {
        "model": "moonshot-v1-8k",
        "api_key_env": "MOONSHOTAI_API_KEY",
        "base_url": "https://api.moonshot.cn/v1",
    },
    AIProvider.OPENROUTER: {
        "model": "openrouter/auto",
        "api_key_env": "OPENROUTER_API_KEY",
        "base_url": "https://openrouter.ai/api/v1",
    },
    AIProvider.GROQ: {
        "model": "llama-3.1-8b-instant",
        "api_key_env": "GROQ_API_KEY",
        "base_url": "https://api.groq.com/openai/v1",
    },
    AIProvider.SILICONFLOW: {
        "model": "Qwen/Qwen3.5-35B-A3B",
        "api_key_env": "SILICONFLOW_API_KEY",
        "base_url": "https://api.siliconflow.cn/v1",
    },
    AIProvider.NVIDIA: {
        "model": "nvidia/nemotron-3-super-120b-a12b",
        "api_key_env": "NVIDIA_API_KEY",
        "base_url": "https://integrate.api.nvidia.com/v1",
    },
    AIProvider.SENSENOVA: {
        "model": "sensenova-6.8-flash-lite",
        "api_key_env": "SENSENOVA_API_KEY",
        "base_url": "https://token.sensenova.cn/v1",
    },
}


class AIConfig(BaseModel):
    """AI client configuration."""

    provider: AIProvider
    provider_chain: str | None = None
    model: str
    base_url: str | None = None
    base_url_env: str | None = None
    api_key_env: str
    chatgpt_account: str | None = None
    extra_body: dict[str, Any] | None = None
    temperature: float = 0.3
    max_tokens: int = 4096
    throttle_sec: float = 0.0
    analysis_concurrency: int = 1
    enrichment_concurrency: int = 1
    languages: list[str] = Field(default_factory=lambda: ["en"])
    # Azure OpenAI specific; required when provider == AZURE
    azure_endpoint_env: str | None = None
    api_version: str | None = None

    @model_validator(mode="before")
    @classmethod
    def default_chatgpt_credentials(cls, value: Any) -> Any:
        if isinstance(value, dict) and value.get("provider") == AIProvider.OPENAI_CHATGPT:
            value = dict(value)
            value.setdefault("api_key_env", "")
        return value

    @model_validator(mode="after")
    def validate_chatgpt_settings(self) -> "AIConfig":
        chain = [name.strip() for name in (self.provider_chain or "").split(",")]
        if "openai-chatgpt" in chain and self.provider != AIProvider.OPENAI_CHATGPT:
            raise ValueError("ChatGPT in provider_chain requires ai.provider=openai-chatgpt and its account-specific model")
        if self.provider == AIProvider.OPENAI_CHATGPT:
            if not self.model.strip():
                raise ValueError("Choose a ChatGPT model using horizon-chatgpt models")
            if self.base_url and self.base_url.rstrip("/") != "https://api.openai.com/v1":
                raise ValueError("openai-chatgpt uses https://api.openai.com/v1; custom base_url is not supported")
            if self.extra_body:
                raise ValueError("ai.extra_body is not supported for openai-chatgpt preview requests")
            if self.api_key_env:
                raise ValueError("openai-chatgpt uses OAuth; leave api_key_env empty")
        return self

    @field_validator("languages")
    @classmethod
    def validate_languages(cls, languages: list[str]) -> list[str]:
        """Allow conventional language tags while excluding path syntax."""
        language_tag = re.compile(r"^[A-Za-z]{2,8}(?:[-_][A-Za-z0-9]{1,8})*$")
        invalid = [language for language in languages if not language_tag.fullmatch(language)]
        if invalid:
            raise ValueError(f"invalid language code: {invalid[0]!r}")
        language_keys = [language.replace("_", "-").casefold() for language in languages]
        if len(language_keys) != len(set(language_keys)):
            raise ValueError("output languages must be unique")
        return languages


class GitHubSourceConfig(BaseModel):
    """GitHub source configuration."""

    type: str  # "user_events", "repo_releases", etc.
    username: str | None = None
    owner: str | None = None
    repo: str | None = None
    enabled: bool = True
    category: str | None = None
    profile: ProfileRoute = None


class HackerNewsConfig(BaseModel):
    """Hacker News configuration."""

    enabled: bool = True
    fetch_top_stories: int = 30
    min_score: int = 100
    category: str | None = None
    profile: ProfileRoute = None


class ExtractorType(StrEnum):
    TRAFILATURA = "trafilatura"
    FIRECRAWL = "firecrawl"
    OUTCRAWL = "outcrawl"
    SPECSTREAM = "specstream"


class TrafilaturaExtractorConfig(BaseModel):
    type: Literal[ExtractorType.TRAFILATURA] = ExtractorType.TRAFILATURA
    favor_precision: bool = False
    favor_recall: bool = False


class FirecrawlExtractorConfig(BaseModel):
    type: Literal[ExtractorType.FIRECRAWL] = ExtractorType.FIRECRAWL
    api_key_env: str = "FIRECRAWL_API_KEY"
    only_main_content: bool = True


class OutcrawlExtractorConfig(BaseModel):
    type: Literal[ExtractorType.OUTCRAWL] = ExtractorType.OUTCRAWL
    api_key_env: str = "OUTCRAWL_API_KEY"
    only_main_content: bool = True


class SpecStreamExtractorConfig(BaseModel):
    type: Literal[ExtractorType.SPECSTREAM] = ExtractorType.SPECSTREAM
    api_key_env: str = "SPECSTREAM_API_KEY"


ExtractorConfig = Annotated[
    TrafilaturaExtractorConfig | FirecrawlExtractorConfig | OutcrawlExtractorConfig | SpecStreamExtractorConfig,
    Field(discriminator="type"),
]


class RSSSourceConfig(BaseModel):
    """RSS feed source configuration."""

    name: str
    url: HttpUrl
    enabled: bool = True
    category: str | None = None
    content_extractor: str | None = None
    profile: ProfileRoute = None


class RedditSubredditConfig(BaseModel):
    """Configuration for monitoring a specific subreddit."""

    subreddit: str
    enabled: bool = True
    sort: str = "hot"  # hot, new, top, rising
    time_filter: str = (
        "day"  # hour, day, week, month, year, all (only for top/controversial)
    )
    fetch_limit: int = 25
    min_score: int = 10
    category: str | None = None
    profile: ProfileRoute = None


class RedditUserConfig(BaseModel):
    """Configuration for monitoring a specific Reddit user."""

    username: str  # without u/ prefix
    enabled: bool = True
    sort: str = "new"
    fetch_limit: int = 10
    category: str | None = None
    profile: ProfileRoute = None


class RedditConfig(BaseModel):
    """Reddit source configuration."""

    enabled: bool = True
    subreddits: list[RedditSubredditConfig] = Field(default_factory=list)
    users: list[RedditUserConfig] = Field(default_factory=list)
    fetch_comments: int = 5  # top comments per post, 0 to disable


class TelegramChannelConfig(BaseModel):
    """Configuration for monitoring a specific Telegram channel."""

    channel: str  # channel username, e.g. "zaihuapd"
    enabled: bool = True
    fetch_limit: int = 20
    category: str | None = None
    profile: ProfileRoute = None


class TelegramConfig(BaseModel):
    """Telegram source configuration."""

    enabled: bool = True
    channels: list[TelegramChannelConfig] = Field(default_factory=list)


class TwitterConfig(BaseModel):
    """Twitter source configuration.

    Two modes are supported:
    - "apify": Use Apify scweet actor (requires APIFY_TOKEN, more reliable)
    - "playwright": Use Playwright + browser cookies (free, no token needed)

    `keywords` uses Apify search mode. Playwright logs a warning and skips them.
    """

    enabled: bool = True
    mode: str = "apify"  # "apify" or "playwright"
    users: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    fetch_limit: int = 10
    category: str | None = None
    profile: ProfileRoute = None
    fetch_reply_text: bool = False
    max_replies_per_tweet: int = 3
    max_tweets_to_expand: int = 10
    reply_min_likes: int = 0
    # Apify settings (used when mode == "apify")
    apify_token_env: str = "APIFY_TOKEN"
    actor_id: str = "altimis~scweet"
    # Playwright settings (used when mode == "playwright")
    cookie_dir: str = "data"
    cookie_file_pattern: str = "x_cookies_*.json"


class OpenBBWatchlist(BaseModel):
    """A named watchlist of tickers fetched from one OpenBB provider.

    Each watchlist produces one news.company() call per run, so group
    symbols by provider rather than creating one watchlist per symbol.
    """

    name: str
    symbols: list[str] = Field(default_factory=list)
    enabled: bool = True
    provider: str = "yfinance"
    fetch_limit: int = 20
    category: str | None = None
    profile: ProfileRoute = None


class OpenBBConfig(BaseModel):
    """OpenBB Platform source configuration.

    Uses the installed `openbb` SDK to fetch news and filings for a set of
    tickers. The SDK is an optional dependency; if it is not installed the
    scraper reports a source failure while other sources can still run.

    Provider credentials (FMP, Benzinga, Polygon, Intrinio, Tiingo, etc.)
    are resolved by openbb from environment variables / its own user
    settings file, so Horizon does not need to pass them explicitly.
    """

    enabled: bool = True
    watchlists: list[OpenBBWatchlist] = Field(default_factory=list)
    fetch_filings: bool = False
    filings_provider: str = "sec"


class OSSInsightConfig(BaseModel):
    """OSS Insight trending repos source configuration.

    Pulls top star-gain repositories from the OSS Insight public API and
    emits them as ContentItems. Optional `keywords` filter limits results
    to repos whose description, repo name, or collection names contain at
    least one of the listed substrings (case-insensitive). Leave
    `keywords` empty to ingest everything trending in the configured
    languages.
    """

    enabled: bool = False
    period: str = "past_24_hours"  # past_24_hours, past_28_days
    languages: list[str] = Field(
        default_factory=lambda: ["All", "Python", "TypeScript"]
    )
    keywords: list[str] = Field(default_factory=list)
    min_stars: int = 5
    max_items: int = 30
    category: str | None = None
    profile: ProfileRoute = None


class GDELTConfig(BaseModel):
    """GDELT 2.0 DOC API source configuration.

    Queries the key-less GDELT DOC API
    (https://api.gdeltproject.org/api/v2/doc/doc) for recent news articles
    matching a search query and emits them as ContentItems. No API key is
    required. The DOC API caps results at 250 records per request, so keep
    `max_records` modest.
    """

    enabled: bool = False
    query: str = "artificial intelligence"
    mode: str = "ArtList"
    max_records: int = 75  # GDELT DOC API caps at 250; keep modest
    timespan: str | None = None  # e.g. "24h"; overrides since-derived window
    language: str | None = None  # sourcelang filter, e.g. "english"; None = no filter
    country: str | None = None  # sourcecountry filter; None = no filter
    category: str | None = None  # Horizon category label for downstream grouping
    profile: ProfileRoute = None


class GoogleNewsConfig(BaseModel):
    """Google News RSS search source configuration.

    Builds Google News RSS search URLs
    (https://news.google.com/rss/search) for a query and parses the
    resulting feed via feedparser. No API key is required.
    """

    enabled: bool = False
    query: str = "artificial intelligence"
    language: str = "en"  # hl
    country: str = "US"  # gl
    ceid: str | None = None  # when None scraper derives it as "{country}:{language}"
    max_results: int = 100  # cap ~100
    category: str | None = None
    profile: ProfileRoute = None


class SourcesConfig(BaseModel):
    """All sources configuration."""

    github: list[GitHubSourceConfig] = Field(default_factory=list)
    hackernews: HackerNewsConfig = Field(default_factory=HackerNewsConfig)
    rss: list[RSSSourceConfig] = Field(default_factory=list)
    reddit: RedditConfig = Field(default_factory=RedditConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)
    twitter: TwitterConfig | None = None
    openbb: OpenBBConfig | None = None
    ossinsight: OSSInsightConfig = Field(default_factory=OSSInsightConfig)
    gdelt: GDELTConfig | None = None
    google_news: GoogleNewsConfig | None = None


class WebhookConfig(BaseModel):
    """Webhook notification configuration."""

    url_env: str | None = (
        None  # Environment variable name containing the webhook URL
    )
    request_body: str | dict | list | None = (
        None  # POST body: real JSON object or string with #{key} placeholders; if empty, will use GET
    )
    headers: str | None = None  # Custom headers, "Key: Value" per line
    delivery: Literal["summary", "summary_and_items"] = "summary"
    overview_position: Literal["first", "last"] = "first"
    platform: Literal["generic", "feishu", "lark", "dingtalk", "slack", "discord"] = "generic"
    layout: Literal["markdown", "collapsible"] = "markdown"
    fallback_layout: Literal["markdown", "collapsible"] = (
        "markdown"  # Layout to use when the requested layout is unsupported
    )
    languages: list[str] | None = (
        None  # Optional language filter for webhook delivery; defaults to all AI languages
    )
    enabled: bool = False


class WeChatConfig(BaseModel):
    """Optional iLink delivery; credentials live in the data directory's session file."""

    enabled: bool = False
    languages: list[str] | None = None
    chunk_size: int = Field(default=4000, gt=0, le=4000)


class EmailConfig(BaseModel):
    """Email configuration for updates/subscriptions."""

    imap_server: str
    imap_port: int = 993
    imap_enabled: bool = True
    smtp_server: str
    smtp_port: int = 465
    smtp_username: str | None = None
    email_address: str
    password_env: str = "EMAIL_PASSWORD"
    sender_name: str = "Horizon Daily"
    subscribe_keyword: str = "SUBSCRIBE"
    unsubscribe_keyword: str = "UNSUBSCRIBE"
    enabled: bool = False


class CategoryGroupConfig(BaseModel):
    """A quota group containing one or more source categories."""

    name: str | None = None
    limit: int = Field(gt=0)
    categories: list[str] = Field(min_length=1)


class ProfileSettingsConfig(BaseModel):
    """User preferences applied to a processing profile at runtime."""

    model_config = ConfigDict(extra="forbid")

    threshold: float | None = Field(default=None, ge=0, le=10)
    topic_dedup: bool = True


class ProcessingConfig(BaseModel):
    """Profile discovery and fallback settings."""

    model_config = ConfigDict(extra="forbid")

    profiles_dir: str = "profiles"
    default_profile: str = "tech-news"
    profile_settings: dict[str, ProfileSettingsConfig] = Field(default_factory=dict)


class DisplayConfig(BaseModel):
    """Controls terminal output presentation."""

    model_config = ConfigDict(extra="forbid")

    icon_style: Literal["emoji", "nerd", "ascii"] = "emoji"


class CollectionConfig(BaseModel):
    """Controls which source items are fetched."""

    model_config = ConfigDict(extra="forbid")

    # Positivity is collection_hours(), applied once before a run. This field
    # stores the configured number and does not check it again.
    time_window_hours: int = 24

    @field_validator("time_window_hours", mode="before")
    @classmethod
    def reject_boolean_time_window(cls, value: Any) -> Any:
        # Pydantic's lax int conversion accepts bool as 0/1, so reject it before
        # collection_hours() can only see the coerced integer.
        if isinstance(value, bool):
            raise ValueError("time_window_hours must be an integer, not a boolean")
        return value


class DigestConfig(BaseModel):
    """Controls grouping and limits in the final digest."""

    model_config = ConfigDict(extra="forbid")

    max_items: int | None = Field(default=None, gt=0)
    category_groups: dict[str, CategoryGroupConfig] = Field(default_factory=dict)
    group_by: Literal["category", "profile"] = "category"
    default_group: str = "other"
    default_group_limit: int | None = Field(default=None, gt=0)
    profile_order: list[str] = Field(default_factory=list)

    @field_validator("profile_order")
    @classmethod
    def validate_profile_order(cls, value: list[str]) -> list[str]:
        if any(not profile_id.strip() for profile_id in value):
            raise ValueError("digest.profile_order entries must be non-empty strings")
        if len(value) != len(set(value)):
            raise ValueError("digest.profile_order entries must be unique")
        return value


class Config(BaseModel):
    """Main configuration model."""

    model_config = ConfigDict(extra="forbid")

    ai: AIConfig
    sources: SourcesConfig
    collection: CollectionConfig = Field(default_factory=CollectionConfig)
    digest: DigestConfig = Field(default_factory=DigestConfig)
    processing: ProcessingConfig = Field(default_factory=ProcessingConfig)
    display: DisplayConfig = Field(default_factory=DisplayConfig)
    extractors: dict[str, ExtractorConfig] = Field(default_factory=dict)
    email: EmailConfig | None = None
    webhook: WebhookConfig | None = None
    wechat: WeChatConfig | None = None
