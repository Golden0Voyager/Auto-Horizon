---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 43 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Java4Shell：OpenJDK Base64 处理中的远程代码执行漏洞](#item-tech-news-1) ⭐️ 8.0/10
2. [Phrack 73 发布：含 Docker 逃逸利用与 SSH1 RCE 历史](#item-tech-news-2) ⭐️ 8.0/10
3. [Solid 2.0 发布：新增服务端 RPC 与实时广播功能](#item-tech-news-3) ⭐️ 8.0/10
4. [微软发布 MAI Code 2 与 Code 2 Flash 编程模型](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI 发布 GPT-6.2 Astra 与 Sol，价格大幅下调](#item-tech-news-5) ⭐️ 8.0/10
6. [Datasette Lite 重写：Service Workers 让完整 Datasette 在浏览器中运行](#item-tech-news-6) ⭐️ 8.0/10
7. [美国高度机密国安通信网络中断](#item-tech-news-7) ⭐️ 7.0/10
8. [微软 ONNX Runtime 仓库从 GitHub 消失](#item-tech-news-8) ⭐️ 7.0/10
9. [Quad9 退出法国：DNS 屏蔽争议的警钟](#item-tech-news-9) ⭐️ 7.0/10
10. [外部沙箱模式：编码代理安全执行的新方案](#item-tech-news-10) ⭐️ 7.0/10
11. [中国完成 Q/V 频段 27 Gbps 双向无线通信验证](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [工信部委托中汽协评估 17 家车企 60 天账期](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Java4Shell：OpenJDK Base64 处理中的远程代码执行漏洞](https://calif.io/java4shell/) ⭐️ 8.0/10

OpenJDK 的 Base64 处理被曝出无需认证的远程代码执行漏洞 CVE-2026-114938，CVSS 4.0 评分 9.2，潜伏近 4 年。该漏洞影响 Java 17（17.0.6 及之后全部 17 线）、21、25、27；标准 Java 8/11 通常不受影响，但 Oracle Java 8 Performance Pack 例外。漏洞仅影响搭载 AVX-512 VBMI 指令集的 x86-64 服务器处理器，大致对应 2021 年及以后发布的 Intel 处理器（Ice Lake 及更新 Xeon）和 2022 年及以后发布的 AMD 处理器（Zen 4 及更新 EPYC/Ryzen）；ARM64 架构不受影响。

hackernews · werrett · 11月17日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50538240)

**「背景」** OpenJDK 的 Base64 解码在支持 AVX-512 VBMI 指令集的 x86-64 处理器上会生成 HotSpot 存根代码，该存根在处理特定输入时存在内存破坏，导致无需认证的远程代码执行。该漏洞编号 CVE-2026-114938，CVSS 4.0 评分 9.2，影响 Java 17.0.6 及之后全部 17 线、21、25、27；标准 Java 8/11 通常不受影响，但 Oracle Java 8 Performance Pack 例外，ARM64 架构不受影响。

**「影响与应对建议」** 运行受影响 Java 版本（17.0.6 及之后、21、25、27）且使用 AVX-512 VBMI 指令集 x86-64 处理器的组织，应尽快应用 Oracle 于 11 月 17 日发布的更新；目前尚无公开的利用报告。社区提出的 -XX:UseAVX=2 启动参数可作为临时缓解手段，但该建议尚未经官方确认。

**「社区讨论」** 社区讨论中，Semgrep 的 ievans 发布了免费检测脚本，用于检查 HotSpot VM、OpenJDK/Oracle JDK/GraalVM JDK 等五个条件；AgentME 则引用 Twitter 上的未确认说法，建议用 -XX:UseAVX=2 标志绕过该漏洞。lucasluitjes 指出当前攻击对网络条件（如 RTT 和抖动）敏感，低且稳定的往返时延更有利于利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cycode.com/blog/java4shell-cve-2026-114938/">Java4Shell (CVE-2026-114938): Affected Versions, How to Check ...</a></li>
<li><a href="https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/">Java4Shell: Remote Code Execution in OpenJDK (CVE-2026-114938)</a></li>
<li><a href="https://threatdefence.com/article/java4shell-cve-2026-114938-openjdk-rce-patching-hunting">Java4Shell CVE-2026-114938: Java 17 RCE Checks and Hunting</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Java`, `#OpenJDK`, `#RCE`

---

<a id="item-tech-news-2"></a>
### [Phrack 73 发布：含 Docker 逃逸利用与 SSH1 RCE 历史](https://phrack.org/issues/73/introduction_md) ⭐️ 8.0/10

Phrack 73 已发布，这是这份长期运行的电子杂志的最新一期，面向安全研究人员和漏洞利用开发者。本期包含一篇 Docker 逃逸漏洞利用技术文章，以及一篇回顾 2000 年 SSH1 远程代码执行漏洞的历史文章。该杂志延续了其技术深度传统，为安全社区提供了可直接研究的具体内容。

hackernews · notmine1337 · 11月17日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=50535992)

**「背景」** Phrack 是一份长期运行的黑客电子杂志，既刊载技术文章也记录地下文化；第 73 期延续这一传统，包含 Docker 逃逸利用和 2000 年 SSH1 RCE 的历史回顾。

**「影响」** 对于计划参考本期 Docker 逃逸利用文章的安全从业者，一个实际问题是该漏洞是否已负责任披露并获得 CVE 编号；在确认之前，直接采用该利用代码可能带来合规或部署风险。

**「社区讨论」** 社区讨论中，用户 ashleyn 质疑本期 Docker 逃逸利用文章所涉漏洞是否已负责任披露并获得 CVE 编号；用户 NelsonMinar 则指出，SSH1 RCE 历史回顾有助于反思当前安全领域的变化速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://phrack.org/">Phrack Magazine</a></li>

</ul>
</details>

**标签**: `#security`, `#hacking`, `#phrack`, `#exploit`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Solid 2.0 发布：新增服务端 RPC 与实时广播功能](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 8.0/10

Solid 2.0 已正式发布，这是该响应式 UI 框架的一次主要版本更新，新增了服务端 RPC、实时/广播（live/broadcast）功能以及改进的调试诊断能力。此次发布面向使用 Solid 构建响应式应用的前端开发者，新能力旨在简化全栈数据流。这是已发布的正式版本而非计划公告，但现有资料未提供具体的版本号或与 Solid 1.x 的兼容性细节。

hackernews · pier25 · 11月17日 18:56 · [社区讨论](https://news.ycombinator.com/item?id=50536387)

**「背景」** SolidJS 是一个响应式 UI 框架，此前版本以响应式更新为核心。2.0 作为新的主版本，在保留核心响应式模型的同时，新增了服务端 RPC、实时/广播能力以及改进的调试诊断。

**「社区讨论」** 社区评论中，用户 pwmglenn 认为 Solid 2.0 的服务端 RPC 与实时/广播功能比 LiveView 或 htmx/datastar 更自然易用，并提到 Remix 曾试图弥合前后端中间层但未完全成功；用户 wk\_end 则指出，&\#x27;Built to Be Written by Agents&\#x27; 部分所强调的更好调试诊断同样会帮助人类开发者，暗示&\#x27;代理最佳实践&\#x27;与&\#x27;人类最佳实践&\#x27;的区分可能被夸大。

**标签**: `#SolidJS`, `#frontend`, `#reactive programming`, `#major release`, `#web development`

---

<a id="item-tech-news-4"></a>
### [微软发布 MAI Code 2 与 Code 2 Flash 编程模型](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 8.0/10

微软于 11 月 17 日发布 MAI Code 2 和 MAI Code 2 Flash，两款新编程模型已集成到 GitHub Copilot 中。社区报告显示，MAI Code 2 在实际使用中表现强劲，性能与 Claude Opus 等领先模型相当，能够解决 Windows WSL/Ubuntu 环境下的 Python 构建问题、生成测试用例并修复 Azure 部署（Bicep）问题。

hackernews · lemonish97 · 11月17日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=50535885)

**「背景」** MAI Code 2 和 Code 2 Flash 是微软发布的新一代编程模型，并直接集成到 GitHub Copilot 中。此前 GitHub Copilot 已支持在多种模型之间切换，用户可在现有界面中选择模型；此次更新将 MAI Code 2 作为新选项加入，同时提供更轻量的 Flash 版本。

**「对开发者的影响」** MAI Code 2 Flash 在三个日常编码基准测试中，以 GPT-6 Luna 65% 和 Claude Haiku 5.5 20% 的成本提供相当性能，这为 GitHub Copilot 用户提供了更具成本效益的编码助手选项；GitHub Copilot Fusion 更新显示该模型已集成到 Copilot 中，用户可在 Fusion 模式下选用。

**「社区讨论」** 用户 chopete3 报告称，GitHub Copilot 今日以 50% 折扣提供 MAI Code 2，切换后成功解决了 Windows WSL/Ubuntu 下的 Python 构建问题、生成了测试用例并修复了 Azure 部署（Bicep）问题，感觉与 Claude Opus 没有差异。另一用户 LaurensBER 则表示已取消 GitHub Copilot 订阅，认为 19 美元档位难以证明其价值，但愿意尝试新模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models/">GitHub Copilot Fusion updates: more availability, benchmarks , and...</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at... | Microsoft AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding assistant`, `#Microsoft`, `#model release`, `#GitHub Copilot`

---

<a id="item-tech-news-5"></a>
### [OpenAI 发布 GPT-6.2 Astra 与 Sol，价格大幅下调](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/) ⭐️ 8.0/10

OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol，分别面向高强度任务与日常通用场景，API 模型名为 gpt-6.2-astra 和 gpt-6.2-sol。Astra 输入/输出定价为每百万 token 8 美元/40 美元，较 6 Astra 的 10/50 美元下调 20%，缓存价从每百万 1 美元降至 0.40 美元；Sol 维持 2/10 美元，为 GPT-5.6 Sol 的一半。Simon Willison 已发布 LLM 0.38 以支持新模型。

rss · Simon Willison · 11月17日 22:38

**「背景」** 此前 6 Astra 与 Claude Fable 5 的定价均为 10/50 美元，而 GPT-5.6 Sol 为 4/20 美元；本次 Astra 延续了前代 80% 的降价幅度，Sol 则维持 6.1 与 6 的价格不变。

**「影响」** 缓存价从每百万 1 美元降至 0.40 美元，对长时间运行的 agentic 会话尤其有利；但 Astra 6.2 在多项基准测试中未超过 Claude Fable 5.2，且 Theo Browne 反馈其长任务中会随机询问用户无法理解的内部实现细节，可能影响实际使用体验。

**「社区讨论」** 社区评价呈两极：chriddyp 在数据分析测试中测得 Astra 成本从约 20 美元降至 4 美元、Sol 从 2.6 美元降至 1.2 美元且准确率相近，但部分用例会提前结束而未找到答案；thefourthchime 的 PacBench 显示 Astra 得 92 分（6.6 分钟，2.04 美元），略低于 Kimi K3.1 Pro 的 93 分（11.5 分钟，0.68 美元），而 Sol 以 87 分与 Muse Wonder 持平但成本更低。

**标签**: `#OpenAI`, `#GPT-6.2`, `#LLM pricing`, `#AI models`, `#agentic AI`

---

<a id="item-tech-news-6"></a>
### [Datasette Lite 重写：Service Workers 让完整 Datasette 在浏览器中运行](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison 发布了 Datasette Lite 的完整重写，改用 Service Workers 和 Pyodide 在浏览器中运行完整的服务端 Datasette Python 应用，效果几乎与真实服务端应用无异。新版本支持从 PyPI 选择特定版本的 Datasette、从 GitHub 仓库加载指定 commit、tag 或分支，可从超过 100 个 SQLite 版本中挑选，并可通过 URL 参数从 PyPI 或 wheel 文件 URL 安装额外插件（包括 JavaScript 可视化工具）。这些能力让开发者无需搭建 Web 服务器即可通过链接分享功能演示或复现 bug。

rss · Simon Willison · 11月17日 16:48

**「背景」** Datasette Lite 最初于 2022 年发布，当时通过在 Pyodide Web Worker 中运行 Datasette 并模拟请求，再将生成的 HTML 通过 innerHTML 注入页面。这种实现方式导致依赖 JavaScript 的功能无法工作，因为 innerHTML 中的 script 标签不会执行。此次重写改用 Service Workers 解决了这一问题，使浏览器端运行效果接近真实服务端应用。

**「影响」** 这一重写使 Datasette Lite 成为 Datasette 开发流程中的实用工具：Willison 已在 GitHub issue \#3056 中用它演示分页 bug 的旧行为与修复效果，开发者无需启动本地服务器即可通过 URL 复现问题或展示新功能。

**标签**: `#WebAssembly`, `#Pyodide`, `#Datasette`, `#service workers`, `#Python`

---

<a id="item-tech-news-7"></a>
### [美国高度机密国安通信网络中断](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down) ⭐️ 7.0/10

美国一个高度机密的国家安全通信网络于 11 月 17 日发生中断，具体影响范围和持续时间尚未公布。该网络服务于国家安全通信，其故障引发了对关键基础设施韧性的担忧。目前官方尚未确认故障原因，外界猜测涉及网络攻击或人员削减，但这些说法尚未得到证实。

hackernews · monkeydust · 11月17日 15:38 · [社区讨论](https://news.ycombinator.com/item?id=50532849)

**「背景」** 该网络是美国政府用于传输高度机密情报与军事指令的专用通信系统，其运行状态通常不对外公开。

**「NSA 内部机密网络中断影响情报共享」** 此次中断直接影响了美国国家安全局（NSA）内部机密通信与信息共享能力。路透社报道称该网络出现“临时性降级”；CBS 新闻确认该网络（被称为“NSA Net”）用于该情报机构内部的机密通信。在恢复之前，依赖该网络的机密信息流转与协同工作将受到延误或中断，可能影响 NSA 的日常情报处理与响应时效。

**「社区讨论」** 评论者就故障原因展开争论：有人猜测与 AI 辅助攻击或“vibe coded”相关，也有人质疑 NSA 为何在恢复前就公开宣布网络中断，认为这可能存在战略意图。这些观点均属推测，尚无证据支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/technology/highly-classified-us-national-security-communications-network-is-down-cnn-2026-11-17/">Classified US national security communications network hit by ...</a></li>
<li><a href="https://www.cbsnews.com/news/nsa-network-down-classified-fort-meade/">NSA&#x27;s classified internal network goes down, sources say</a></li>

</ul>
</details>

**标签**: `#national security`, `#critical infrastructure`, `#network outage`, `#IT operations`, `#cybersecurity`

---

<a id="item-tech-news-8"></a>
### [微软 ONNX Runtime 仓库从 GitHub 消失](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

微软的 ONNX Runtime 开源推理引擎仓库已从 GitHub 上消失，导致依赖该仓库的构建和评估流水线中断。据用户 nvader 报告，其评估任务在 11 月 17 日早晨开始失败，且此前没有任何预警；该仓库此前拥有约 22,000 颗星标。目前消失原因尚未确认，微软也未发布官方说明，因此长期影响仍不确定。

hackernews · nvader · 11月17日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=50539610)

**「背景」** ONNX Runtime 是微软维护的跨平台机器学习推理/训练加速器，被 Office、Azure、Bing 等产品及大量社区项目使用（tool-2-2、tool-2-3）。此前有开发者提到，2026 年 3 月曾发现一个解析器缺陷，可使 ONNX 模型在未经验证的情况下读取任意文件路径或内存地址（tool-2-1）；这一安全背景可能为本次仓库突然消失提供了部分上下文，但原因尚未确认。

**「影响」** 对依赖该仓库的开发者而言，CI/CD 和模型推理流水线会因无法拉取依赖而失败；目前可用的替代是 Intel 维护的 onnxruntime 分支，但它包含 OpenVINO 修改，并非完全等同的官方版本。

**「社区讨论」** 评论中，nvader 报告其评估流水线因仓库消失而失败且无预警；Heliodex 建议使用 Intel 的 onnxruntime 分支作为替代。另有用户猜测可能与软件包被入侵或模型后门攻击向量有关，但这些说法目前没有证据支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50539610">Microsoft &#x27;s ONNX Runtime has disappeared from GitHub</a></li>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft /onnxruntime: ONNX Runtime : cross-platform, high...</a></li>
<li><a href="https://onnxruntime.ai/docs/">ONNX Runtime is a cross-platform machine-learning model accelerator</a></li>

</ul>
</details>

**标签**: `#ONNX Runtime`, `#Microsoft`, `#GitHub`, `#open source`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [Quad9 退出法国：DNS 屏蔽争议的警钟](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Quad9 因法国法院命令的 DNS 屏蔽而退出法国，Cloudflare 在 11 月 17 日发布的博客文章中讨论了这一事件，并借此表达对互联网治理和 DNS 基础设施更广泛问题的担忧。文章将 Quad9 的退出视为一个警示信号，但 Cloudflare 本身并未宣布任何具体行动。

hackernews · subset · 11月17日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=50538994)

**「背景」** Quad9 是一家运营免费公共 DNS 解析器的瑞士非营利基金会。2026 年 10 月，巴黎法院就盗版网站屏蔽作出裁决并设定处罚后，Quad9 宣布将于 11 月 24 日停止向法国用户提供服务，成为第二家退出法国的 DNS 解析器。与此同时，比利时法院近期也向 Cloudflare、Google 和 Cisco 发出命令，要求它们在 2027 年 1 月初之前通过公共解析器屏蔽特定网站。

**「Quad9 撤出法国的直接后果」** 对法国用户而言，Quad9 撤出意味着他们失去了一个注重隐私的公共 DNS 解析器；Cloudflare 在博文中仅表示反对，但未承诺采取同等行动，社区成员正要求其在上诉失败时也撤出相关国家。

**「社区讨论」** Quad9 首席技术官 johnhtodd 在评论中称，他在 IETF 127 上感受到对 Quad9 立场的 100% 支持，并对 DNS 领域的现状感到普遍担忧。另一位评论者 driverdan 则批评 Cloudflare 文章态度模糊，质问 Cloudflare 是否会在上诉失败后也承诺退出受影响国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://reclaimthenet.org/quad9-leaving-france-over-dns-blocking-order">Quad9 to Leave France Over DNS Blocking Order - Reclaim The Net</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/">DNS Resolver Quad9 Will Leave France After Court Orders ...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#internet governance`, `#Quad9`, `#Cloudflare`, `#censorship`

---

<a id="item-tech-news-10"></a>
### [外部沙箱模式：编码代理安全执行的新方案](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison 与 Prime Radiant 实验室发布&quot;外部沙箱&quot;模式，让编码代理（如 Pi、Claude Code、Codex）执行的代码运行在独立沙箱中，而代理本身位于沙箱之外，以降低提示注入攻击导致本地模型执行破坏性操作的风险。该模式配套发布了三个沙箱服务器实现：external-sandbox-v86（Node.js 服务器，通过 v86 在 WebAssembly 中运行 Alpine Linux）、external-sandbox-container（Python 服务器，在 Apple Containers 实例中运行 Alpine Linux）以及 external-sandbox-quicksand（Python 服务器，使用微软 Quicksand 库，将 QEMU 和 Alpine Linux 打包在 Python 包中）。三个实现提供相同的 localhost API，并支持可选的 HTTP/HTTPS 允许列表代理，用于精确控制代理代码可访问的主机，以及凭据替换机制，使代理无需共享密钥即可进行认证 API 调用。

rss · Simon Willison · 11月17日 22:52

**「背景」** 编码代理（如 Claude Code、Codex 和 Pi）会在用户机器上执行代码，而提示注入攻击可能诱使代理执行恶意操作，因此沙箱化一直是缓解这一风险的关键手段。传统的沙箱方案通常将沙箱置于代理自身环境内部，而外部沙箱模式则把代理执行的代码放入独立沙箱，同时让代理本身留在沙箱之外，从而将代理与不可信代码的执行环境彻底隔离。

**「影响」** 使用 Pi、Claude Code 或 Codex 的开发者现在可以将代理执行的代码隔离到独立沙箱中，从而在本地安全地试验模型，而无需担心提示注入攻击导致破坏性操作；同时，允许列表代理和凭据替换机制让开发者能精确控制代理代码的网络访问范围，并在不向代理泄露密钥的情况下进行认证 API 调用。

**标签**: `#AI security`, `#prompt injection`, `#sandboxing`, `#coding agents`, `#LLM agents`

---

<a id="item-tech-news-11"></a>
### [中国完成 Q/V 频段 27 Gbps 双向无线通信验证](https://www.news.cn/tech/20261117/d6323540dccf4e2a976c48a762795956/c.html) ⭐️ 7.0/10

中科院空天信息创新研究院等单位在丽江中国遥感卫星地面站完成 Q/V 频段高阶体制高码速率双向通信实验，首次系统测试 64QAM 至 512QAM 多种调制模式。在 512QAM 调制下，单通道双向速率达 6.75 Gbps，通过双载频和极化复用将总速率提升至 27 Gbps，刷新国内该频段最高码速率纪录。实验方表示后续将争取实现超过 50 Gbps 的速率，该验证为 6G 与卫星互联研究提供了实验基础。

telegram · zaihuapd · 11月17日 08:45

**「背景」** Q/V 频段是 6G 星地融合通信的候选频段之一，带宽资源比现有 Ka 频段更丰富，但高频段路径损耗和雨衰也更严重，因此需要高阶调制与极化复用等技术来提升频谱效率和链路容量。此次实验正是针对这一技术路线，在丽江地面站对多种高阶调制模式进行系统测试。

**「影响」** 该实验为 6G 与卫星互联研究提供了 Q/V 频段高码速率传输的实测验证，但结果仍限于地面站实验阶段，后续需在星地实际链路中验证，并争取将速率提升至 50 Gbps 以上。

**标签**: `#wireless-communication`, `#satellite-communication`, `#6G`, `#QV-band`, `#high-throughput-communication`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [工信部委托中汽协评估 17 家车企 60 天账期](http://www.caam.org.cn/chn/5/cate_68/con_5237404.html) ⭐️ 7.0/10

中国汽车工业协会 11 月 16 日受工信部委托，对 17 家重点车企开展供应商账款支付评估。评估核查 60 天账期是否落地，以及非中小企业现金和银行承兑汇票支付比例是否不低于 80%。

telegram · zaihuapd · 11月18日 01:15

**「背景」** 修订后的《保障中小企业款项支付条例》自 2025 年 6 月 1 日施行，要求大型企业及时支付中小企业款项；此后至少 17 家车企于 6 月 10 日至 11 日密集表态将供应商账期统一至 60 天内，本次评估即核查上述承诺的落地情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.bjnews.com.cn/detail/1749644188168851.html">从“百日煎熬”到“ 60 天 承诺”： 车 企 账 期 瘦身，供应商解压</a></li>

</ul>
</details>

**标签**: `#汽车行业`, `#政策监管`, `#供应链`, `#中小企业`, `#账期管理`

---