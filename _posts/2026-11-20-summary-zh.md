---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 34 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [英国政府承认曾向苹果发布秘密加密令](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenJDK 曝 java4shell 漏洞，Oracle 接管修复](#item-tech-news-2) ⭐️ 8.0/10
3. [PostgreSQL 19 发布：新增 WAIT FOR LSN 实现只读副本读写一致性](#item-tech-news-3) ⭐️ 8.0/10
4. [Gemini 在 Mac 上新增电脑操作功能，可代用户点击输入](#item-tech-news-4) ⭐️ 8.0/10
5. [欧盟委员会向逾 4 万名员工部署开源消息协议 Matrix](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic 纳斯达克首日：发行价 83 美元，收盘 97.17 美元](#item-tech-news-6) ⭐️ 7.0/10
7. [Claude 解决黑洞物理两个开放问题](#item-tech-news-7) ⭐️ 7.0/10
8. [Google Play 2027 年起强制大屏适配与 Android 17 目标版本](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI 模型助力芯片设计，AMD 旗舰 GPU 提升 14%](#item-tech-news-9) ⭐️ 7.0/10
10. [PHP 流包装器大小写漏洞致 TLS 静默关闭，已修复](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [Anthropic 纳斯达克上市首日开盘涨 34%，市值约 1.5 万亿美元](#item-finance-news-1) ⭐️ 9.0/10
2. [拼多多三季度营收 1083 亿元，盘前股价涨逾 8%](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [英国政府承认曾向苹果发布秘密加密令](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) ⭐️ 8.0/10

英国政府已承认曾向苹果公司发布一项秘密技术能力通知（technical capability notice），要求其协助访问加密数据。这一承认是通过调查权力法庭（Investigatory Powers Tribunal）的裁决公开的，媒体通过保密安全简报而非泄密获知该通知的存在，但通知的具体内容仍处于保密状态。苹果此前承诺“无人能访问你的数据，包括苹果自己”，如今已弱化为“苹果无法访问你的数据”，这一变化引发了对用户数据安全保证的严重质疑。

hackernews · Terretta · 11月19日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50562113)

**「背景」** 英国调查权力法庭是允许公民挑战政府监控命令的独立司法机构；该法庭审理了 Apple Inc 诉内政大臣等案，政府曾试图迫使苹果创建批评者所称的后门，并申请对该命令保密。

**「影响」** 对苹果用户而言，这一承认意味着其端到端加密承诺的实际保障范围已收窄：苹果不再声称“无人能访问你的数据”，而仅声称“苹果无法访问你的数据”。社区评论指出，用户的密钥很可能是密钥加密密钥（KEK），用于解锁实际保护数据的密钥，因此“密钥从未离开设备”的说法并不能保证数据本身不可访问。

**「社区讨论」** 社区讨论中最有实质性的观点来自 natch，指出苹果已显著弱化其安全保证，且这种弱化“具有欺骗性”：用户的密钥很可能是密钥加密密钥（KEK），用于解锁实际保护数据的密钥，因此“密钥从未离开设备”的说法并不能保证数据本身不可访问。另一用户 fweimer 补充了主要来源（调查权力法庭），指出媒体是通过保密安全简报而非泄密获知该通知，通知内容仍属机密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/19/u-k-government-forced-to-disclose-secret-apple-backdoor-order/">UK government forced to disclose secret Apple backdoor order</a></li>
<li><a href="https://www.judiciary.uk/judgments/apple-inc-v-home-secretary-and-others/">Apple Inc -v- Home Secretary and others - Courts and ...</a></li>
<li><a href="https://www.ft.com/content/46a5cf3c-a827-477f-b72f-e7415565e729?syn-25a6b1a6=1">UK loses bid to keep Apple ‘backdoor’ order secret</a></li>

</ul>
</details>

**标签**: `#encryption`, `#privacy`, `#UK government`, `#Apple`, `#surveillance`

---

<a id="item-tech-news-2"></a>
### [OpenJDK 曝 java4shell 漏洞，Oracle 接管修复](https://github.com/openjdk/jdk/pull/32781) ⭐️ 8.0/10

OpenJDK 的 PR \#32781 在 2026 年 9 月报告了一个被社区称为 java4shell 的 Java 漏洞；PR 作者称 Oracle 要求其暂缓提交，随后于 10 月 28 日表示修复已由 Oracle 接管。该漏洞涉及可被利用的远程代码执行链，至少一名独立研究者通过 fuzzing 发现并报告了 Oracle。对 Java 应用维护者而言，这意味着需要关注 Oracle 后续发布的补丁，并在官方修复前评估暴露面。

hackernews · notmine1337 · 11月19日 11:47 · [社区讨论](https://news.ycombinator.com/item?id=50558906)

**「背景」** OpenJDK 的 PR \#32781 中报告了一个被社区称为 java4shell 的 Java 漏洞；在相关讨论中，PR 作者提到 Oracle 于 10 月 1 日要求其暂停提交，随后在 10 月 28 日确认修复已由 Oracle 接管。该问题还关联到 adoptium-support 的 issue \#1480，其中记录了作者与 Oracle 之间的沟通过程。

**「影响与修复建议」** Java4Shell（CVE-2026-114938）影响 Java 17.0.6 及更高版本，在特定 x86-64 系统上可导致远程代码执行；Oracle 与 OpenJDK 漏洞组已于 2026 年 11 月 17 日发布修复，受影响用户应尽快升级到厂商修复版本，若无法立即升级，可临时禁用受影响的优化作为缓解措施。该漏洞是 OpenJDK Base64 解码器中的堆溢出，需满足特定暴露条件才能被利用。

**「社区讨论」** 社区讨论中，wood\_spirit 质疑加州研究者的 LLM 可能读过此前的 bug 报告而非独立发现；dlor 则称自己通过 fuzzing 独立发现并构建了完整 RCE 链，且其测试环境无网络访问，但无法排除训练集影响。Botifier 指出 Oracle 在合并提交中的评论与 PR 中逐字相同，darkamaul 认为即使模型看过 issue，理解严重性和利用方法仍需监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dynatrace.com/news/blog/java4shell-cve-2026-114938-which-java-runtimes-are-affected-and-how-to-fix-them/">Java4Shell (CVE-2026-114938): Affected Java Versions &amp; fixes</a></li>
<li><a href="https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability">Java4Shell (CVE-2026-114938): OpenJDK RCE Vulnerability FAQ</a></li>
<li><a href="https://pentest-tools.com/blog/java4shell-cve-2026-114938">Java4Shell (CVE-2026-114938): affected versions and fixes</a></li>

</ul>
</details>

**标签**: `#security`, `#java`, `#vulnerability`, `#openjdk`, `#rce`

---

<a id="item-tech-news-3"></a>
### [PostgreSQL 19 发布：新增 WAIT FOR LSN 实现只读副本读写一致性](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 8.0/10

PostgreSQL 19 已正式发布，比通常的九月发布晚了约两个月，主要原因是团队需要处理 AI 报告的安全漏洞问题。新版本引入 WAIT FOR LSN 命令，允许应用在备用服务器上等待 WAL 重放到指定日志序列号后再执行查询，从而实现“读己之写”一致性。该命令支持可选超时参数，超时后返回错误。这一模式此前在 MediaWiki 中通过 MySQL 的 WAIT\_FOR\_EXECUTED\_GTID\_SET\(\) 等函数手工实现。

rss · Simon Willison · 11月19日 20:43

**「背景」** PostgreSQL 通常每年 9 月发布新的大版本，但今年因 AI 报告的安全漏洞问题而推迟了两个月。新的 WAIT FOR LSN 命令解决了备用服务器上“读己之写”一致性的长期问题，此前应用如 MediaWiki 需要自行实现复制延迟检查。

**「影响」** 使用只读副本的应用现在可以在不引入自定义应用层逻辑的情况下，确保读取到主库刚写入的数据，从而简化高可用架构下的读写一致性实现。

**标签**: `#PostgreSQL`, `#database`, `#release`, `#replication`, `#high availability`

---

<a id="item-tech-news-4"></a>
### [Gemini 在 Mac 上新增电脑操作功能，可代用户点击输入](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 8.0/10

Google 面向美国地区 Mac 版 Gemini 用户推出“电脑操作”功能，可代用户点击、输入、浏览菜单和填写表单。该功能仅向订阅 Google AI Plus、Pro 或 Ultra 的用户开放，并支持在独立后台窗口运行，用户可同时继续使用主屏幕和光标。安全控制方面，用户可限制 Gemini 能访问的应用、实时查看其操作、随时暂停，并在关键操作前要求审批。

telegram · zaihuapd · 11月20日 02:51

**「功能背景」** Gemini 是 Google 的 AI 助手，此前主要提供对话式问答与内容生成能力。此次新增的“电脑操作”功能将其角色从对话助手扩展为可直接操控用户界面的智能体。

**「影响」** 对 Mac 版 Gemini 的 AI Plus、Pro 和 Ultra 订阅用户而言，该功能意味着可将点击、填表等界面操作委托给 AI 代理，同时继续使用主屏幕；但关键操作仍需人工审批，且目前仅限美国地区使用。

**标签**: `#AI agents`, `#Gemini`, `#Mac`, `#automation`, `#human-in-the-loop`

---

<a id="item-tech-news-5"></a>
### [欧盟委员会向逾 4 万名员工部署开源消息协议 Matrix](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/) ⭐️ 7.0/10

欧盟委员会已将开源消息协议 Matrix 部署给超过 4 万名员工，Element 在官方博客中介绍了此次大规模部署的技术细节。这是一次值得关注的开源消息协议大规模部署，但社区讨论对端到端加密的成熟度和大规模部署下的可扩展性提出了质疑。需要指出的是，部署细节来自 Element 的官方博客，属于供应商自述，尚未有独立验证。

hackernews · liotier · 11月19日 10:58 · [社区讨论](https://news.ycombinator.com/item?id=50558533)

**「背景」** Matrix 是一个开源的消息协议，支持端到端加密，而欧盟委员会将其部署给超过 4 万名员工，是对这一标准的大规模采用。

**「影响」** 为维持 4 万余名用户的可接受性能，欧盟委员会关闭了实时在线状态功能，这体现了大规模部署中的功能取舍；同时，社区评论者质疑 Matrix 的端到端加密是否足以满足国家安全级用例。

**「社区讨论」** 社区讨论对此次部署评价两极分化：有用户认为 Matrix 的端到端加密仍存在严重问题，MLS 迁移工作似乎已停滞，不适合国家安全级用例；也有日常用户希望欧盟委员会的采用能为项目带来更多开发资源和资金。另有用户提到，随着用户增加，实时在线状态功能因性能压力已被关闭。

**标签**: `#Matrix`, `#European Commission`, `#open source`, `#messaging`, `#privacy`

---

<a id="item-tech-news-6"></a>
### [Anthropic 纳斯达克首日：发行价 83 美元，收盘 97.17 美元](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-test-2026-11-19/) ⭐️ 7.0/10

Anthropic 于 11 月 19 日在纳斯达克上市，股票代码 ANT。据社区评论，发行价 83 美元，开盘 111.5 美元，收盘 97.17 美元，较发行价上涨 17.07%，较开盘价下跌 12.85%，市值约 1.26 万亿美元。对投资者而言，按开盘价买入者收盘浮亏 12.85%，按发行价获配者浮盈 17.07%；首日交易显示市场对 AI 公司估值存在明显分歧，开盘冲高后回落。

hackernews · wslh · 11月19日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50562754)

**「背景」** Anthropic 是一家领先的人工智能实验室，此前为私有公司，此次在纳斯达克上市是其首次公开募股。

**「上市首日市值回落，低于 OpenAI 私募估值」** Anthropic（ANT）11 月 19 日登陆纳斯达克，IPO 定价 83 美元、募资 813.4 亿美元，按完全稀释口径估值 1.5 万亿美元，超过 SpaceX 成为史上最大 IPO。但开盘冲高至 111.5 美元后持续回落，收盘报 97.17 美元，较开盘价下跌 12.85%，市值降至约 1.26 万亿美元。这一收盘估值低于 OpenAI 近期在私募市场寻求的估值水平，可能对 OpenAI 的上市定价形成压力。

**「社区讨论」** 有评论者认为，市值约 1.26 万亿美元低于几周前部分人期望的 2 万亿美元以上，也低于 OpenAI 在私募市场的估值，对 OpenAI 不是好兆头；另有资深程序员认为 AI 已能完成编程工作，软件工程职业的“红利期”基本结束，初级从业者尤其难以规划未来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html">Anthropic IPO live updates: ANT stock price and Nasdaq debut</a></li>
<li><a href="https://roboforex.com/blog/anthropic-ipo/anthropic-nasdaq-debut/">Anthropic Nasdaq Debut : IPO at 83 USD Beats SpaceX</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#valuation`, `#software engineering`

---

<a id="item-tech-news-7"></a>
### [Claude 解决黑洞物理两个开放问题](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 7.0/10

Anthropic 在 Fable 5.2 发布公告中称，其前沿模型 Claude 解决了黑洞物理中的两个开放问题：第一个结果涉及复杂的自举（bootstrap）计算，第二个结果证明了与给定中心电荷一致的黑洞质量上限，从而为量子引力理论提供了一致性约束。但正如公告所承认的，这两个结果并不直接描述我们的宇宙，也没有实际应用，属于理论物理中的小众进展，且目前仅为 Anthropic 的单方面报告，尚未经独立验证。

hackernews · cybermango · 11月19日 17:30 · [社区讨论](https://news.ycombinator.com/item?id=50563148)

**「背景」** Anthropic 研究员 Hongbin Chen 在 8 月将 Claude 的能力测试作为一项副业项目，而该模型的早期版本（Fable 5.1）此前已挑战过涉及九环计算的理论物理难题。这些新结果出现在围绕 AI 生成证明的更广泛争议之中，OpenAI 与 Anthropic 的相近工作已引起科学家的审视。

**「社区讨论」** 评论中，用户 dap 批评“Claude 解决了”这种表述是持续且有问题地将机器拟人化，并指出公告全文未提及提示词（prompt），无法判断 Claude 究竟做了什么；用户 chunky1994 则从技术角度指出，第一个结果是复杂的易错计算，第二个结果证明了与给定中心电荷一致的黑洞质量上限，从而为量子引力理论提供了一致性约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/claude-black-hole-physics">Claude Fable 5.2 solves two open problems in the physics of black ...</a></li>
<li><a href="https://www.scientificamerican.com/article/dueling-proofs-from-openai-and-anthropic-astound-scientists/">Dueling proofs from OpenAI and Anthropic ... | Scientific American</a></li>
<li><a href="https://claypier.com/en/claude-nine-loop-physics-record/">Claude Takes On a Theoretical Physics Challenge... | claypier</a></li>

</ul>
</details>

**标签**: `#AI for science`, `#theoretical physics`, `#black holes`, `#Claude`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [Google Play 2027 年起强制大屏适配与 Android 17 目标版本](https://developer.android.google.cn/blog/posts/google-play-adaptive-quality-standards?hl=zh-cn) ⭐️ 7.0/10

Google Play 宣布自 2027 年 4 月起，应用须达到规定的自适应兼容等级，以适配折叠屏和大屏设备，避免界面拉伸、黑边、比例锁定等问题，并确保设备形态切换时应用状态正常保持。2027 年 8 月起，新应用及更新还须以 Android 17（API 37）为目标版本。未达标准的应用可能面临更新发布限制或商店曝光下降，开发者还需提交折叠屏设备截图。

telegram · zaihuapd · 11月19日 08:42

**「背景」** 自适应兼容等级是 Google Play 新引入的质量标准，用于评估应用在折叠屏和大屏设备上的适配情况，包括避免界面拉伸、黑边、比例锁定以及保持设备形态切换时的应用状态。Android 应用以特定 API 级别为目标版本，以利用对应平台的功能和兼容性改进；此次新规将目标版本提升至 Android 17（API 37）。

**「开发者须在 2027 年前完成折叠屏适配」** 开发者需在 2027 年 4 月前让应用达到 Tier 3 折叠屏兼容标准并提交折叠屏截图，否则可能面临更新发布限制或商店曝光下降；自 2027 年 8 月起，新应用及更新还须以 Android 17（API 37）为目标版本。Google 已提供 UI 设计指南、Figma 模板和自适应应用质量指南作为准备资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.android.com/blog/posts/google-play-adaptive-quality-standards">Elevating apps: New adaptive quality standards on Google Play</a></li>
<li><a href="https://developer.android.com/docs/quality-guidelines/adaptive-app-quality">Adaptive app quality guidelines | App quality | Android ...</a></li>
<li><a href="https://www.androidheadlines.com/2026/11/google-android-foldable-app-requirements-2027.html">Google Forces Android Developers to Support Foldables by 2027 ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#Google Play`, `#折叠屏`, `#大屏适配`, `#开发者政策`

---

<a id="item-tech-news-9"></a>
### [OpenAI 模型助力芯片设计，AMD 旗舰 GPU 提升 14%](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

OpenAI 11 月 19 日发布博文称，其模型参与自研推理芯片 Jalapeño 的设计，向量单元标准单元面积减少约 13%、矩阵单元减少约 10%，相关优化已在芯片点亮中验证。在与 AMD 的合作中，旗舰 GPU IP 的功耗、性能、面积（PPA）指标相对高度优化基线提升最高 14%，部分改动已进入送厂制造的设计。OpenAI 同时宣布与 Synopsys 合作训练 GPT-Synopsys 模型。这些数据来自 OpenAI 自身发布，尚未经独立验证，其中 Synopsys 合作仍属宣布阶段。

telegram · zaihuapd · 11月19日 09:30

**「背景」** Jalapeño 是 OpenAI 自研的推理芯片，本次公告称其模型参与该芯片设计，向量标准单元面积减少约 13%、矩阵单元减少约 10%，相关优化已在芯片点亮中验证。与 AMD 的合作针对旗舰 GPU IP 的功耗、性能、面积（PPA）指标，部分改动已进入送厂制造的设计。

**「影响」** 对 AMD 而言，部分采用 OpenAI 模型优化的改动已进入送厂制造的设计，意味着这些优化有机会体现在实际产品中，而非仅停留在研究阶段。

**标签**: `#AI chip design`, `#OpenAI`, `#AMD`, `#EDA`, `#hardware`

---

<a id="item-tech-news-10"></a>
### [PHP 流包装器大小写漏洞致 TLS 静默关闭，已修复](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 7.0/10

PHP 的 HTTP/FTP 流包装器在 scheme 含大写 S（如 httpS://、HTTPS://、FTPS://）时会静默禁用 TLS，将令牌、Basic 认证、Cookie、POST 请求体和 FTP 登录信息以明文发送。该漏洞编号 CVE-2026-128064（GHSA-f6gg-rchx-xw8j），CVSS 4.0 评分为 8.2，已在 PHP 8.2.36、8.3.37、8.4.28、8.5.13 和 8.6.0 中修复；8.1 及更早版本已 EOL，不会获得修复，只能自行将 URL scheme 转为小写。问题存在约 20 年，由 Lukasz Jachowicz 报告。

telegram · zaihuapd · 11月20日 03:04

**「背景」** PHP 的 HTTP/FTP 流包装器在解析 URL scheme 时大小写不敏感，但 TLS 启用逻辑只检查固定位置的小写 s，因此 HTTPS://、httpS://、FTPS:// 等混合大小写写法会被当作明文 HTTP/FTP 处理。该漏洞编号 CVE-2026-128064（GHSA-f6gg-rchx-xw8j），CVSS 4.0 评分 8.2，已在 PHP 8.2.36、8.3.37、8.4.28、8.5.13 和 8.6.0 中修复；8.1 及更早版本已结束支持，不会获得修复，只能自行将 URL scheme 统一转为小写。

**「影响」** 受影响的开发者应升级到已修复的 PHP 版本，或在使用前将 URL scheme 统一转为小写；若仍运行 8.1 及更早版本，需自行检查并规范化所有 HTTP/FTP 请求及重定向目标，否则凭据可能被第三方截获。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://everycve.com/CVE-2026-128064">CVE - 2026 - 128064 : Mixed- case HTTPS and FTPS URLs can expose...</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#TLS`, `#CVE`, `#vulnerability`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 纳斯达克上市首日开盘涨 34%，市值约 1.5 万亿美元](https://www.cls.cn/detail/2539480) ⭐️ 9.0/10

人工智能公司 Anthropic（ANT）11 月 19 日登陆纳斯达克，发行价 83 美元/股，开盘报 111.5 美元，较发行价上涨 34%，按开盘价计算市值约 1.5 万亿美元。本次 IPO 与同步私募配售合计募资约 1073.4 亿美元，其中同步配售 260 亿美元来自谷歌、英伟达、微软、AMD、博通、美光及台积电等战略投资者。

telegram · zaihuapd · 11月19日 16:56

**「背景」** Anthropic 由前 OpenAI 研究副总裁 Dario Amodei 于 2021 年创立，是一家专注 AI 安全与研究的公益公司，旗下拥有 Claude 系列大模型。

**「影响」** 对投资者而言，AI 资本开支的融资渠道正从私募转向公开市场，公共投资者将直接承担相关风险；同时中期选举后对数据中心的负面情绪也可能影响后续选址和审批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dario_Amodei">Dario Amodei - Wikipedia</a></li>
<li><a href="https://www.britannica.com/money/Anthropic-PBC">Anthropic | History , Controversies, &amp; Claude AI | Britannica Money</a></li>
<li><a href="https://www.anthropic.com/company">Company \ Anthropic</a></li>
<li><a href="https://www.linkedin.com/posts/martaknorton_research-spotlight-the-ipo-triple-threat-activity-7478149907883716608-cR5w">SpaceX OpenAI Anthropic IPO Impact on Markets | LinkedIn</a></li>
<li><a href="https://www.cnbc.com/2026/11/07/anthropic-ipo-ai-data-center-backlash.html">Anthropic IPO hits AI backlash after midterms show rebuke data centers</a></li>

</ul>
</details>

**标签**: `#IPO`, `#Anthropic`, `#AI`, `#capital markets`, `#technology`

---

<a id="item-finance-news-2"></a>
### [拼多多三季度营收 1083 亿元，盘前股价涨逾 8%](https://mp.weixin.qq.com/s/vMtfWkFZ0hRTDU54BlD80Q) ⭐️ 7.0/10

拼多多发布 2026 年第三季度财报，营收 1083 亿元，净利润 295 亿元；业绩公布后，其美股盘前股价上涨逾 8.6%。

telegram · zaihuapd · 11月19日 12:56

**「背景」** 上年同期（2025 年第三季度）营收基本持平，净利润由 293 亿元升至 295 亿元。

**「影响」** 拼多多股东及中国电商板块投资者受到直接影响：三季度营收和净利润超预期，推动股价盘前上涨逾 8%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.biggo.com/news/0d9e52f2-b35f-46b1-bac7-5b4b50e471ca">Pinduoduo&#x27;s Q3 Revenue Hits 108.3 Billion Yuan as 100 Billion ...</a></li>
<li><a href="https://www.marketbeat.com/instant-alerts/transcript-pdd-q3-earnings-call-highlights-2026-11-19/">PDD Q3 Earnings Call Highlights - MarketBeat</a></li>

</ul>
</details>

**标签**: `#earnings`, `#Pinduoduo`, `#e-commerce`, `#stock movement`, `#China market`

---