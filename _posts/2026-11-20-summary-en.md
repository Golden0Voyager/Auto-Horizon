---
layout: default
title: "Horizon Summary: 2026-11-20 (EN)"
date: 2026-11-20
lang: en
---

> From 34 items, 12 important content pieces were selected

---

**Technology News**
1. [UK government admits secret encryption order to Apple](#item-tech-news-1) ⭐️ 8.0/10
2. [Java &\#x27;java4shell&\#x27; vulnerability reported in OpenJDK PR, Oracle takes over fix](#item-tech-news-2) ⭐️ 8.0/10
3. [PostgreSQL 19 adds WAIT FOR LSN for read-your-writes on standbys](#item-tech-news-3) ⭐️ 8.0/10
4. [Gemini&\#x27;s computer-use feature on Mac lets users delegate UI tasks](#item-tech-news-4) ⭐️ 8.0/10
5. [European Commission deploys Matrix to more than 40,000 staff](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic&\#x27;s Nasdaq debut sparks AI valuation and software engineering debate](#item-tech-news-6) ⭐️ 7.0/10
7. [Anthropic&\#x27;s Claude solves two open problems in black hole physics](#item-tech-news-7) ⭐️ 7.0/10
8. [Google Play mandates foldable/large-screen adaptation from 2027](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI reports 14% PPA gain on AMD GPU IP via AI chip design](#item-tech-news-9) ⭐️ 7.0/10
10. [PHP silently disables TLS for uppercase-S schemes; fixed in 8.2.36+](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Anthropic opens 34% above IPO price on Nasdaq debut](#item-finance-news-1) ⭐️ 9.0/10
2. [Pinduoduo Q3 Revenue 108.3B Yuan, Shares Rise Over 8% Premarket](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [UK government admits secret encryption order to Apple](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) ⭐️ 8.0/10

The UK government has admitted it issued a secret encryption order to Apple, according to a judgment from the Investigatory Powers Tribunal. The order is a technical capability notice, and its contents remain secret; the media learned of it through confidential security briefings rather than a leak. The admission raises concerns about weakened security and surveillance, though the specific requirements imposed on Apple are not public.

hackernews · Terretta · Nov 19, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50562113)

**「Background」** The Investigatory Powers Tribunal is an independent court that allows citizens to challenge UK government surveillance orders, including technical capability notices under the Investigatory Powers Act 2016. On 19 November 2026 it issued a judgment in Apple Inc v Home Secretary and others, rejecting the Home Office&\#x27;s bid to keep secret its attempt to force Apple to create what critics call a backdoor.

**「Impact」** For Apple users, the admission creates uncertainty about the scope of government access to encrypted data, as the specific requirements of the technical capability notice remain secret.

**「Community Discussion」** Commenters debated the significance of the admission: one argued Apple has weakened its security assurances in a way that is arguably deceptive, noting that the user&\#x27;s key may be a key-encryption key that opens another key protecting the data, while another pointed to the Investigatory Powers Tribunal judgment as the primary source and noted the media learned of the notice through confidential briefings, not a leak.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/19/u-k-government-forced-to-disclose-secret-apple-backdoor-order/">UK government forced to disclose secret Apple backdoor order</a></li>
<li><a href="https://www.judiciary.uk/judgments/apple-inc-v-home-secretary-and-others/">Apple Inc -v- Home Secretary and others - Courts and ...</a></li>
<li><a href="https://www.ft.com/content/46a5cf3c-a827-477f-b72f-e7415565e729?syn-25a6b1a6=1">UK loses bid to keep Apple ‘backdoor’ order secret</a></li>

</ul>
</details>

**Tags**: `#encryption`, `#privacy`, `#UK government`, `#Apple`, `#surveillance`

---

<a id="item-tech-news-2"></a>
### [Java &\#x27;java4shell&\#x27; vulnerability reported in OpenJDK PR, Oracle takes over fix](https://github.com/openjdk/jdk/pull/32781) ⭐️ 8.0/10

A critical Java vulnerability, dubbed &\#x27;java4shell&\#x27;, was reported in OpenJDK PR \#32781 in September 2026; Oracle took over the fix after asking the reporter to hold off, and at least one other researcher independently reported a similar RCE chain. The PR author said Oracle requested no further PR work on October 1 and confirmed takeover on October 28. Independent researcher dlor reported finding the same issue via fuzzing and building a full RCE chain, though the exact scope and affected versions remain unclear from the discussion.

hackernews · notmine1337 · Nov 19, 11:47 · [Discussion](https://news.ycombinator.com/item?id=50558906)

**「Background」** OpenJDK pull request \#32781, filed in September 2026, reported a critical Java vulnerability later dubbed &\#x27;java4shell&\#x27;. A commenter citing the linked adoptium-support issue noted that the PR author said Oracle asked them not to proceed with a PR until receiving approval, and that Oracle later took over the fix.

**「Update required for Java4Shell \(CVE-2026-114938\)」** Java4Shell \(CVE-2026-114938\) is a heap overflow in OpenJDK&\#x27;s Base64 decoder that affects Java 17.0.6 and later on certain x86-64 systems, and Oracle and the OpenJDK Vulnerability Group released fixes on November 17, 2026. Affected teams should update to their vendor&\#x27;s fixed Java release; if they cannot update immediately, they can disable the affected optimization as a temporary mitigation.

**「Community discussion」** Commenters debated whether the &\#x27;independent&\#x27; discoveries were truly independent: wood\_spirit suggested the LLM assisting the California researchers may have read the earlier adoptium-support issue, while dlor said their own fuzzing harness had no Internet access and did not access the PR directly, though they could not rule out training-data contamination. darkamaul noted the model may have examined the repo&\#x27;s open and closed issues, but that understanding criticality and exploitation still required human supervision.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dynatrace.com/news/blog/java4shell-cve-2026-114938-which-java-runtimes-are-affected-and-how-to-fix-them/">Java4Shell (CVE-2026-114938): Affected Java Versions &amp; fixes</a></li>
<li><a href="https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability">Java4Shell (CVE-2026-114938): OpenJDK RCE Vulnerability FAQ</a></li>
<li><a href="https://pentest-tools.com/blog/java4shell-cve-2026-114938">Java4Shell (CVE-2026-114938): affected versions and fixes</a></li>

</ul>
</details>

**Tags**: `#security`, `#java`, `#vulnerability`, `#openjdk`, `#rce`

---

<a id="item-tech-news-3"></a>
### [PostgreSQL 19 adds WAIT FOR LSN for read-your-writes on standbys](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 8.0/10

PostgreSQL 19 shipped in November 2026, about two months later than usual, after the team addressed a flurry of AI-reported security issues. The release adds the WAIT FOR LSN command, which lets a session on a standby wait until the standby has replayed the write-ahead log up to a specific log sequence number before running a query, enabling read-your-writes consistency for applications that send reads to standbys. The command supports an optional TIMEOUT, after which the query errors if the replica has not caught up.

rss · Simon Willison · Nov 19, 20:43

**「Background」** PostgreSQL typically ships a new major release each September, but the PostgreSQL 19 release was delayed by about two months because the team had to address a wave of security issues reported by AI tools. The new WAIT FOR LSN command addresses the long-standing challenge of replication lag: applications that read from standby servers previously had to implement their own synchronization, as MediaWiki does with MySQL&\#x27;s WAIT\_FOR\_EXECUTED\_GTID\_SET\(\) and SOURCE\_POS\_WAIT\(\) functions.

**「Impact」** For applications that send reads to standbys, WAIT FOR LSN replaces the need for hand-rolled session-based replication lag tracking, such as the pattern MediaWiki implements against MySQL; adopting it requires upgrading to PostgreSQL 19.

**Tags**: `#PostgreSQL`, `#database`, `#release`, `#replication`, `#high availability`

---

<a id="item-tech-news-4"></a>
### [Gemini&\#x27;s computer-use feature on Mac lets users delegate UI tasks](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 8.0/10

Google Gemini&\#x27;s new computer-use feature on Mac can click, type, browse menus, and fill forms on users&\#x27; behalf. It is available to US users of the Mac version of Gemini who subscribe to Google AI Plus, Pro, or Ultra. Users can run Gemini in a separate background window while continuing to use the main screen and cursor, restrict which apps it can access, view operations in real time, pause at any time, and approve before key operations.

telegram · zaihuapd · Nov 20, 02:51

**「Background」** The computer-use feature is available to users in the United States who run the Mac version of Gemini and subscribe to Google AI Plus, Pro, or Ultra.

**「Impact」** Mac users in the US with a Google AI Plus, Pro, or Ultra subscription can now delegate clicking, typing, and form-filling to Gemini, while retaining control through real-time monitoring, pause, and approval prompts.

**Tags**: `#AI agents`, `#Gemini`, `#Mac`, `#automation`, `#human-in-the-loop`

---

<a id="item-tech-news-5"></a>
### [European Commission deploys Matrix to more than 40,000 staff](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) ⭐️ 7.0/10

The European Commission has deployed Matrix, the open-source messaging protocol, to more than 40,000 staff, in a notable open-source messaging deployment at a major government institution. The rollout reportedly required disabling live presence indicators because the real-time online/away feature created performance load as user numbers grew. Community discussion highlights unresolved concerns about Matrix&\#x27;s end-to-end encryption and client usability, with some users predicting the Commission may eventually migrate to another platform.

hackernews · liotier · Nov 19, 10:58 · [Discussion](https://news.ycombinator.com/item?id=50558533)

**「Background」** Matrix is an open standard for decentralized real-time communication, built on a federated architecture in which independent servers interoperate while users retain control over their data. Its end-to-end encryption and self-hosting capabilities have positioned it as an alternative to proprietary messaging platforms for organizations with data-sovereignty requirements.

**「Operational trade-offs for adopters」** Organizations following the Commission&\#x27;s example should expect operational trade-offs: the Commission disabled live presence because the real-time online/away indicator degraded performance as staff numbers grew, and commenters on the announcement argue that Matrix&\#x27;s end-to-end encryption is not yet sufficient for national-security use cases.

**「Community Discussion」** Commenters disagree on Matrix&\#x27;s readiness: one reports a positive self-hosted experience with ElementX and privacy benefits, while another argues the protocol&\#x27;s end-to-end encryption is a &\#x27;tire fire&\#x27; and its MLS migration appears abandoned, making it unsuitable for national security use. A third commenter hopes the Commission&\#x27;s adoption will bring development resources to address long-standing usability problems.

<details><summary>References</summary>
<ul>
<li><a href="https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/">How the European Commission rolled out Matrix to more than 40,000...</a></li>

</ul>
</details>

**Tags**: `#Matrix`, `#European Commission`, `#open source`, `#messaging`, `#privacy`

---

<a id="item-tech-news-6"></a>
### [Anthropic&\#x27;s Nasdaq debut sparks AI valuation and software engineering debate](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) ⭐️ 7.0/10

Anthropic made its Nasdaq debut on November 19, 2026, according to Reuters. The IPO sparked significant discussion among investors and software engineers about AI valuations and the future of software engineering careers.

hackernews · wslh · Nov 19, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50562754)

**「Background」** Anthropic, the AI lab behind the Claude model family, was a privately held company before this listing. Its Nasdaq debut under the ticker ANT priced at $83 per share, opened at $111.50, and closed at $97.17, giving it a market capitalization of about $1.26 trillion — well below the $2 trillion-plus valuation some private investors had floated weeks earlier.

**「Investor impact」** Investors who bought ANT at the $111.50 opening price saw the stock close at $97.17, a 12.85% first-day decline, while IPO allocations at $83 were up 17.07%. The IPO raised $81.34 billion and valued Anthropic at $1.5 trillion on a fully diluted basis, per RoboForex.

**「Community Discussion」** Commenters disagreed about the significance: capital\_guy and beachy argued the debut signals the end of software engineering as a stable career, while cmiles8 focused on the stock&\#x27;s decline from its opening price and its implications for OpenAI&\#x27;s private valuation. 6thbit reported that the stock closed at $97.17, up 17.07% from the IPO price of $83 but down 12.85% from the opening price of $111.5.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html">Anthropic IPO live updates: ANT stock price and Nasdaq debut</a></li>
<li><a href="https://roboforex.com/blog/anthropic-ipo/anthropic-nasdaq-debut/">Anthropic Nasdaq Debut : IPO at 83 USD Beats SpaceX</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#valuation`, `#software engineering`

---

<a id="item-tech-news-7"></a>
### [Anthropic&\#x27;s Claude solves two open problems in black hole physics](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 7.0/10

Anthropic announced that Claude, its frontier model, solved two open problems in black hole physics, with the results presented in two papers. According to the company, neither result describes our own universe directly and neither has practical applications, but both contribute to a long-running theoretical effort to understand how quantum mechanics and relativity fit together. The results are real but niche, and the announcement is promotional, appearing as a bullet point in the Fable 5.2 release.

hackernews · cybermango · Nov 19, 17:30 · [Discussion](https://news.ycombinator.com/item?id=50563148)

**「Background」** The announcement builds on earlier work: in August, an Anthropic researcher tested Claude&\#x27;s capabilities as a side project, and two physicists later ran a calculation with Claude Fable 5.1 inside Claude Science. The result also follows closely related work from OpenAI and Anthropic that resolved major problems in math, physics, and computer science.

**「Impact」** For theoretical physicists, the results provide new constraints on quantum gravity theories, but Anthropic states they do not describe our own universe and have no practical applications, so the immediate impact is limited to a niche research area.

**「Community Discussion」** Commenters disagreed about how to interpret the announcement: dap argued that crediting Claude with &quot;solving&quot; problems anthropomorphizes the model and noted the blog post never mentions the prompt, while chunky1994 described the first result as a complex error-prone calculation and the second as proving an upper limit on black hole mass for a given central charge, which constrains quantum gravity theories. easterncalculus observed that most comments were not about the papers at all.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/claude-black-hole-physics">Claude Fable 5.2 solves two open problems in the physics of black ...</a></li>
<li><a href="https://www.scientificamerican.com/article/dueling-proofs-from-openai-and-anthropic-astound-scientists/">Dueling proofs from OpenAI and Anthropic ... | Scientific American</a></li>
<li><a href="https://claypier.com/en/claude-nine-loop-physics-record/">Claude Takes On a Theoretical Physics Challenge... | claypier</a></li>

</ul>
</details>

**Tags**: `#AI for science`, `#theoretical physics`, `#black holes`, `#Claude`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [Google Play mandates foldable/large-screen adaptation from 2027](https://developer.android.google.cn/blog/posts/google-play-adaptive-quality-standards?hl=zh-cn) ⭐️ 7.0/10

Google Play will require apps to meet an adaptive compatibility level for foldables and large-screen devices starting April 2027, with new apps and updates needing to target Android 17 \(API 37\) from August 2027. Developers must submit foldable device screenshots; non-compliant apps may face update publication restrictions or reduced store exposure. The policy aims to prevent UI stretching, black bars, and aspect-ratio locking, and to preserve app state across form-factor changes.

telegram · zaihuapd · Nov 19, 08:42

**「Background」** Google Play has been encouraging Android apps to support large screens and foldables, and this announcement turns that push into a formal quality requirement. The new policy sets a specific adaptive compatibility level and, from August 2027, requires new apps and updates to target Android 17 \(API 37\).

**「Developer compliance deadlines」** Developers must meet Google Play&\#x27;s Tier 3 foldable compatibility standards and submit foldable screenshots by April 2027, and target Android 17 \(API 37\) for new apps and updates by August 2027, or face restricted updates and reduced store exposure. Google provides design guidelines, Figma templates, and adaptive app quality tests to help apps run optimally across form factors.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.android.com/blog/posts/google-play-adaptive-quality-standards">Elevating apps: New adaptive quality standards on Google Play</a></li>
<li><a href="https://developer.android.com/docs/quality-guidelines/adaptive-app-quality">Adaptive app quality guidelines | App quality | Android ...</a></li>
<li><a href="https://www.androidheadlines.com/2026/11/google-android-foldable-app-requirements-2027.html">Google Forces Android Developers to Support Foldables by 2027 ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Google Play`, `#折叠屏`, `#大屏适配`, `#开发者政策`

---

<a id="item-tech-news-9"></a>
### [OpenAI reports 14% PPA gain on AMD GPU IP via AI chip design](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

OpenAI says its models helped design its own Jalapeño inference chip, reducing vector standard-cell area by about 13% and matrix-unit area by about 10%, with the optimizations verified during chip bring-up. In a collaboration with AMD, the company reports up to a 14% improvement in power, performance, and area \(PPA\) on a flagship GPU IP relative to a highly optimized baseline, with some changes already incorporated into a design sent to manufacturing. OpenAI also announced a partnership with Synopsys to train a GPT-Synopsys model. These figures are company-reported claims rather than independently verified results.

telegram · zaihuapd · Nov 19, 09:30

**「Background」** AI-assisted chip design uses machine-learning models to optimize physical layout and power, performance, and area \(PPA\) metrics. OpenAI has been testing this approach on its own inference chip Jalapeño, where the reported area reductions were verified in silicon, before applying the same methodology to external partners such as AMD and Synopsys.

**「Impact」** For chip designers, the reported gains suggest AI models can improve PPA even on already optimized designs, but the results are vendor-reported and not independently measured. The Synopsys partnership may bring these models into commercial electronic design automation workflows, though no product, availability, or integration details were disclosed.

**Tags**: `#AI chip design`, `#OpenAI`, `#AMD`, `#EDA`, `#hardware`

---

<a id="item-tech-news-10"></a>
### [PHP silently disables TLS for uppercase-S schemes; fixed in 8.2.36+](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 7.0/10

PHP&\#x27;s HTTP and FTP stream wrappers treated schemes case-insensitively but enabled TLS only when the fifth character was lowercase s, so URLs such as httpS://, HTTPS://, or FTPS:// were sent as plaintext HTTP/FTP, exposing tokens, Basic auth, cookies, POST bodies, and FTP credentials. The flaw, tracked as CVE-2026-128064 \(GHSA-f6gg-rchx-xw8j\) with a CVSS 4.0 score of 8.2, went unnoticed for about 20 years and is fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, and 8.6.0. PHP 8.1 and earlier are end-of-life and receive no fix, so developers on those versions must normalize URL schemes to lowercase themselves.

telegram · zaihuapd · Nov 20, 03:04

**「Background」** PHP&\#x27;s HTTP and FTP stream wrappers parse URL schemes case-insensitively, but the code that enables TLS checks for a lowercase &\#x27;s&\#x27; at a fixed position, so mixed-case schemes such as httpS:// are treated as plaintext HTTP/FTP \(tool-1-1\). This behavior has existed in PHP&\#x27;s stream wrapper implementation for years and was addressed in the PHP Foundation&\#x27;s November 2026 security release, which also patched other critical flaws such as CVE-2026-115560 \(tool-1-2, tool-1-3\).

**「Impact」** Developers using PHP&\#x27;s HTTP/FTP stream wrappers should upgrade to a fixed release or, on end-of-life versions, lowercase the scheme before use; otherwise any uppercase-S scheme—including one introduced by a third-party redirect—sends credentials and request data in plaintext.

<details><summary>References</summary>
<ul>
<li><a href="https://everycve.com/CVE-2026-128064">CVE - 2026 - 128064 : Mixed- case HTTPS and FTPS URLs can expose...</a></li>
<li><a href="https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html">PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote...</a></li>
<li><a href="https://cybersecuritynews.com/php-8-released/">PHP Warns of Critical Security Flaws Affecting All Supported Versions...</a></li>

</ul>
</details>

**Tags**: `#PHP`, `#security`, `#TLS`, `#CVE`, `#vulnerability`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic opens 34% above IPO price on Nasdaq debut](https://www.cls.cn/detail/2539480) ⭐️ 9.0/10

AI company Anthropic \(ANT\) opened at $111.50 on its Nasdaq debut, 34% above its $83 IPO price, giving it a market value of about $1.5 trillion. The IPO and a concurrent private placement together raised about $107.3 billion, according to Cailian Press.

telegram · zaihuapd · Nov 19, 16:56

**「Background」** Anthropic is an AI safety and research company founded in 2021 by Dario and Daniela Amodei, known for its Claude family of large language models and structured as a public benefit corporation.

**「Impact」** The $107B raise moves AI infrastructure financing from private to public markets, exposing AI capital spending to investor scrutiny and potentially benefiting chip and data-center suppliers, while the debut comes amid political backlash against data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dario_Amodei">Dario Amodei - Wikipedia</a></li>
<li><a href="https://www.britannica.com/money/Anthropic-PBC">Anthropic | History , Controversies, &amp; Claude AI | Britannica Money</a></li>
<li><a href="https://www.anthropic.com/company">Company \ Anthropic</a></li>
<li><a href="https://www.linkedin.com/posts/martaknorton_research-spotlight-the-ipo-triple-threat-activity-7478149907883716608-cR5w">SpaceX OpenAI Anthropic IPO Impact on Markets | LinkedIn</a></li>
<li><a href="https://www.cnbc.com/2026/11/07/anthropic-ipo-ai-data-center-backlash.html">Anthropic IPO hits AI backlash after midterms show rebuke data centers</a></li>

</ul>
</details>

**Tags**: `#IPO`, `#Anthropic`, `#AI`, `#capital markets`, `#technology`

---

<a id="item-finance-news-2"></a>
### [Pinduoduo Q3 Revenue 108.3B Yuan, Shares Rise Over 8% Premarket](https://mp.weixin.qq.com/s/vMtfWkFZ0hRTDU54BlD80Q) ⭐️ 7.0/10

Pinduoduo reported third-quarter 2026 revenue of 108.3 billion yuan and net profit of 29.5 billion yuan, according to its earnings release on Nov. 19. The company&\#x27;s U.S.-listed shares rose more than 8.6% in premarket trading after the results.

telegram · zaihuapd · Nov 19, 12:56

**「Background」** Revenue was essentially flat from a year earlier, while net profit rose to 29.5 billion yuan from 29.3 billion yuan; the company attributed the quarter&\#x27;s performance partly to its &\#x27;Free Shipping to Villages&\#x27; rural logistics program, which it said drove transaction volume growth of more than 30% across several product categories.

**「Impact on investors and sector」** The results were followed by a more than 8% premarket rise in Pinduoduo&\#x27;s shares, directly benefiting its investors and drawing attention to the Chinese e-commerce sector.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.biggo.com/news/0d9e52f2-b35f-46b1-bac7-5b4b50e471ca">Pinduoduo&#x27;s Q3 Revenue Hits 108.3 Billion Yuan as 100 Billion ...</a></li>
<li><a href="https://www.gate.com/news/detail/PDD/pinduoduo-q3-fiscal-2026-revenue-hits-rmb-1083-billion-rural-logistics-25742155">Pinduoduo Q3 Fiscal 2026 Revenue Hits RMB 108.3 Billion ...</a></li>
<li><a href="https://www.marketbeat.com/instant-alerts/transcript-pdd-q3-earnings-call-highlights-2026-11-19/">PDD Q3 Earnings Call Highlights - MarketBeat</a></li>

</ul>
</details>

**Tags**: `#earnings`, `#Pinduoduo`, `#e-commerce`, `#stock movement`, `#China market`

---