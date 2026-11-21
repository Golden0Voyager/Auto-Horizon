---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 40 条内容中筛选出 19 条重要资讯。

---

**科技新闻**
1. [声称证明无外力 Navier–Stokes 方程有限时间爆破](#item-tech-news-1) ⭐️ 10.0/10
2. [陶哲轩探讨无外力纳维-斯托克斯奇点与广义黎曼假设的联系](#item-tech-news-2) ⭐️ 9.0/10
3. [Signal 发布限制 AI 代理捕获移动端数据的技术方案](#item-tech-news-3) ⭐️ 8.0/10
4. [Inkling 2 Mini 开源循环变压器模型发布](#item-tech-news-4) ⭐️ 8.0/10
5. [台积电暂停对华 16nm 及以下芯片订单](#item-tech-news-5) ⭐️ 8.0/10
6. [马苏洛广义黎曼假设证明草案提前发布](#item-tech-news-6) ⭐️ 7.0/10
7. [AI 编程工具将开发者推向架构师](#item-tech-news-7) ⭐️ 7.0/10
8. [阿伦森博客探讨 AI&\#x27;随机鹦鹉&\#x27;证明黎曼猜想的可能性](#item-tech-news-8) ⭐️ 7.0/10
9. [美国 SEC 调查英伟达潜在会计问题](#item-tech-news-9) ⭐️ 7.0/10
10. [美国收紧芯片出口，印度 Yotta 拟新增约 10 万块 GPU](#item-tech-news-10) ⭐️ 7.0/10
11. [OpenAI 上线后台模式：长任务可挂 8 小时，Token 最高省 40%](#item-tech-news-11) ⭐️ 7.0/10
12. [特斯拉辅助驾驶获意大利批准，月费 99 欧元](#item-tech-news-12) ⭐️ 7.0/10
13. [KVM 漏洞 CVE-2026-99312 致 AMD 主机内存泄露](#item-tech-news-13) ⭐️ 7.0/10

**科技博客**
1. [为何 LLM 输出缓存不值得做](#item-tech-blog-1) ⭐️ 8.0/10

**财经新闻**
1. [预测市场对 2026 年标普 500 触及 8000 点的概率骤降](#item-finance-news-1) ⭐️ 7.0/10
2. [美联储官员讲话增多，沃什回避前瞻指引引发市场不确定性](#item-finance-news-2) ⭐️ 7.0/10
3. [美国企业转向净发行股票，为牛市带来供应压力](#item-finance-news-3) ⭐️ 7.0/10
4. [阿里巴巴遭股东集体诉讼，被指隐瞒业务关系及出口管制风险](#item-finance-news-4) ⭐️ 7.0/10
5. [北京拟明确租房正常损耗不得扣减押金](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [声称证明无外力 Navier–Stokes 方程有限时间爆破](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 10.0/10

一篇声称证明无外力 Navier–Stokes 方程有限时间爆破的论文于 2026 年 11 月 20 日发布在 GitHub 上；若该证明成立，将解决千禧年大奖难题之一。该结果尚未经过同行评审或独立验证，目前只能视为预印本/声明，而非已确认的数学定理。对数学物理和流体力学研究者而言，这意味着一个潜在的重大进展，但需要等待验证。

hackernews · trotro · 11月20日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=50576232)

**「背景」** 纳维-斯托克斯方程是描述流体运动的基本方程；千禧年难题关注的是，在无外力作用下，其光滑解是否对所有时间都存在，还是会在有限时间内失去正则性（即发生爆破）。社区讨论将这一版本与需要精心设计外力的“受迫”版本区分开来，认为无外力情形更接近真实物理过程。

**「对千禧年问题的潜在影响」** 若该无外力版本的证明得到验证，它将消除 OpenAI 9 月结果中因依赖精心设计的外力而留下的局限，使该策略更接近千禧年大奖难题的原始设定。不过，两个结果目前仍存在与原始问题（排除欧拉方程、要求外力光滑）的差距，因此尚不能视为对千禧年问题的完整解决。

**「社区讨论」** 据评论者称，OpenAI 曾找到依赖精心设计外力的受迫 Navier–Stokes 反例；本结果针对无外力情形，因此被认为更接近真实流体。另有评论者希望看到实际物理演示或实时模拟，以直观检验爆破是否真的发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy">Navier–Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>

</ul>
</details>

**标签**: `#Navier-Stokes`, `#mathematics`, `#fluid dynamics`, `#millennium problem`, `#PDE`

---

<a id="item-tech-news-2"></a>
### [陶哲轩探讨无外力纳维-斯托克斯奇点与广义黎曼假设的联系](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 9.0/10

陶哲轩在博客文章中探讨了无外力纳维-斯托克斯奇点问题与广义黎曼假设之间的联系，这一讨论在 Hacker News 上引发热议。社区讨论的焦点集中在人工智能辅助证明验证（尤其是 Lean 形式化验证）对数学研究的影响，以及 AI 是否正在改变数学发现的方式。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**「背景」** Navier-Stokes 存在性与光滑性问题是克雷数学研究所的千禧年大奖难题之一，要求判断三维不可压缩 Navier-Stokes 方程的解是否会在有限时间内出现奇点；无外力 Euler 奇点问题则是其无粘极限情形。广义黎曼假设是关于 L-函数非平凡零点分布的猜想。Tao 的这篇博文正是在这些既有问题之间建立联系。

**「对数学验证与 AI 辅助证明的影响」** 独立数学家目前几乎确信，AI 生成的黎曼猜想证明是真实的，验证工作已接近完成；该证明依赖 Lean 形式化验证，而社区报告称两个独立内核均接受该结果，降低了内核漏洞被利用的担忧。这一进展意味着 AI 辅助证明在数学界获得实质性认可，但也凸显了形式化验证工具在确保证明正确性方面的关键作用。

**「社区讨论」** 有用户质疑 Lean 形式化验证是否真正验证了正确的命题，认为编译通过并不保证业务逻辑正确。另一些用户则对 AI 在数学研究中的角色感到既兴奋又担忧，认为 AI 可能超越人类智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity , unforced Navier - Stokes singularity , and...</a></li>
<li><a href="https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/">The AI Riemann hypothesis proof is almost... | Scientific American</a></li>
<li><a href="https://www.amazon.science/blog/how-the-lean-language-brings-math-to-coding-and-coding-to-math">How the Lean language brings math to coding and... - Amazon Science</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#AI`, `#proof verification`, `#Lean`, `#Riemann hypothesis`

---

<a id="item-tech-news-3"></a>
### [Signal 发布限制 AI 代理捕获移动端数据的技术方案](https://signal.org/blog/protecting-your-privacy/) ⭐️ 8.0/10

Signal 于 2026 年 11 月 20 日发布博客文章，介绍在移动操作系统上限制 AI 代理捕获数据的技术措施。该方案针对 AI 应用过度访问用户设备数据的隐私问题，包括防止 AI 应用访问 Signal 聊天内容。据社区用户引用 Signal 高管的说法，Signal 对解决这一问题持&quot;谨慎乐观&quot;态度。

hackernews · dotcoma · 11月20日 09:42 · [社区讨论](https://news.ycombinator.com/item?id=50572348)

**「背景」** 移动操作系统正在将 AI 代理深度集成到系统层，这些代理能够捕获屏幕内容，从而读取应用中的敏感数据。Signal 在博客中警告，这种集成对应用层隐私构成“生存威胁”，并因此采取措施限制截图，以阻止 AI 代理读取私人聊天内容。

**「影响」** Signal 的防捕获措施对用户操作产生了实际影响。社区用户报告称，Windows 上已无法对 Signal 聊天进行截屏，这引发了关于基本功能受限的讨论。

**「社区讨论」** 社区用户 pajamasam 引用 Signal 高管 Meredith Whittaker 的访谈指出，AI 应用对用户设备数据访问过多，且即使未安装 AI 应用，联系人仍可能泄露聊天内容；用户 cimnine 则呼吁 Signal 公开取证调查结果，以便其他开发者受益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal &gt;&gt; Blog &gt;&gt; Signal is Serious About Protecting...</a></li>
<li><a href="https://www.reuters.com/legal/litigation/signal-restricts-screenshots-block-ai-agents-reading-messages-2026-11-20/">EXCLUSIVE: Signal restricts screenshots to block AI agents ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI agents`, `#mobile operating systems`, `#Signal`, `#data security`

---

<a id="item-tech-news-4"></a>
### [Inkling 2 Mini 开源循环变压器模型发布](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines 发布了 Inkling 2 Mini，一款开放权重的循环变压器（looped transformer）模型，其基准测试与 Qwen3.8-27B 相当，并采用端到端 nvfp4 训练。社区报告显示本地推理表现强劲：在 Ryzen 395 上配合 llama.cpp Vulkan 达到约 27 tokens/s，在 M1 Pro MacBook 32GB 上使用 q4 xl 约 10 tokens/s。这些性能数据来自社区实测，尚未经独立验证；模型在部分任务上表现不稳定，例如一个硬币识别测试在 12,000 tokens 后仍未给出正确答案。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「背景」** Inkling 2 Mini 是 Thinking Machines Lab 于 2026 年 11 月发布的 26.4B 参数 MoE（5.4B 激活）开放权重模型，面向编码、智能体和视觉任务。它采用循环（looped）Transformer 架构，通过重复使用同一组权重来扩展有效深度，这是其能在较小激活参数下取得高基准分数的关键。

**「影响」** 对本地推理用户而言，该模型可直接在 llama.cpp/Ollama 上运行，但需应用未合并的 PR（32694、32657、32429、32704）及一个小补丁以获得约 30% 的速度提升；同时，模型在复杂视觉识别任务上的可靠性有限，用户应自行验证其适用性。

**「社区讨论」** 有评论者推测，Inkling 2 Mini 的开放权重和循环架构可能促使多数开源模型转向循环设计，但这一观点尚未得到证据支持；另一用户报告了混合结果：Python 排序任务表现良好，但硬币识别任务在 12,000 tokens 后仍失败，说明实际性能因任务而异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling-2-mini">Inkling 2 Mini - Intelligence, Performance &amp; Price... | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#looped-transformer`, `#local-inference`, `#benchmarks`

---

<a id="item-tech-news-5"></a>
### [台积电暂停对华 16nm 及以下芯片订单](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 8.0/10

台积电已通知客户，暂停接受中国公司 16nm 及以下先进制程订单，除非事先取得美国出口许可或豁免，否则不得供货。此前台积电可自行评估客户设计是否符合豁免条件，现改为须由客户提前申请；美国获批名单包括苹果、AMD 和英伟达，尚无中国公司。受此影响，中国企业只能转向 28nm、40nm 等旧制程，无法获得 AI 数据中心所需的高带宽内存。台积电表示将遵守新规。

telegram · zaihuapd · 11月21日 02:01

**「背景」** 此前，台积电可自行评估客户设计是否符合美国出口豁免条件；新规实施后，客户须提前向美国申请出口许可或豁免，台积电不再自行判断。这一变化意味着中国企业若想获得 16nm 及以下先进制程芯片，必须先取得美方许可，否则只能使用 28nm、40nm 等较旧制程。

**「对客户的影响」** 对依赖台积电先进制程的中国芯片设计公司而言，16nm 及以下订单被暂停意味着其 AI 相关芯片无法按原计划投产，只能退回 28nm/40nm 等成熟制程，并失去获得 AI 数据中心所需 HBM 的渠道。由于新规要求客户提前申请美国出口许可，而获批名单中尚无中国公司，这些客户需自行走审批流程；TrendForce 报道称，冗长的审批程序可能打乱生产排期，且台积电正收紧对中国客户的制造要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendforce.com/news/2026/11/20/news-tsmc-samsung-reportedly-pause-china-consumer-chip-shipments-under-new-u-s-rules-16nm-orders-affected/">[News] TSMC, Samsung Reportedly Pause China Consumer Chip ...</a></li>
<li><a href="https://www.reuters.com/world/china/tsmc-tightens-china-ai-chip-curbs-new-us-rules-close-manufacturing-loophole-2026-11-19/">TSMC tightens China AI chip curbs as new US rules close ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#export controls`, `#TSMC`, `#AI hardware`, `#chip supply chain`

---

<a id="item-tech-news-6"></a>
### [马苏洛广义黎曼假设证明草案提前发布](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 7.0/10

拉维·瓦基尔宣布，亚历山德罗·马苏洛提出了广义黎曼假设的证明草案，布莱恩·康拉德已对其进行了数月的仔细审查，反馈正在被纳入，目前看来情况良好。该证明完全由人类完成，不涉及人工智能。原计划让马苏洛在斯坦福待一年打磨文稿并广泛征求意见后再公布，但现在似乎最好先发布当前草案。该证明尚未经过独立验证，发布显得仓促。

hackernews · jasondavies · 11月20日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=50579568)

**「背景」** 广义黎曼假设（GRH）是数论中最重要的未解问题之一。此前，Anthropic 的 AI 系统被报道在该问题上取得发现，同时 Levent Alpöge 也声称给出了 GRH 的证明；在此背景下，Alessandro Masullo 的证明草案被匆忙公布。

**「验证压力与竞争性声明」** 该声明进入验证阶段：Brian Conrad 表示论文仍在进行重大修订，需待更终稿才能判断方法是否成功，因此数学界目前不能将 GRH 视为已证明；与此同时，Anthropic 的 AI 与 Alpöge 提出的另一项证明采用完全不同的方法，形成竞争性验证压力。

**「社区讨论」** 评论者指出，手稿声称作者已研究该问题 12 年，仓促发布可能是为了在与 AI 发现的竞争中主张优先权；也有人质疑 940 页草稿的完整性（如第一节 1.1.1 为空），并建议数学家应定期发布带时间戳的工作哈希以争取部分功劳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/dueling-claims-of-riemann-hypothesis-proofs-emerge/">Dueling claims of Riemann hypothesis proofs ... | Scientific American</a></li>
<li><a href="https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html">Anthropic Mathematician Claims to Solve Riemann Hypothesis With...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#generalized-riemann-hypothesis`, `#ai`, `#proof`, `#anthropic`

---

<a id="item-tech-news-7"></a>
### [AI 编程工具将开发者推向架构师](https://manidoraisamy.com/developer-to-architect.html) ⭐️ 7.0/10

一篇博客文章与 Hacker News 讨论提出，AI 编程工具正在移除开发者的手写编码工作，使其角色向架构师式的监督与决策转变，作者称这是&\#x27;未被告知的晋升&\#x27;。社区评论对此分歧明显：有开发者认为工程师本就承担需求推敲与数据模型设计，只是少了键盘编码；也有评论者反驳称这并非晋升，而是薪资更低、乐趣更少，沦为 LLM 决策的&\#x27;责任承担者&\#x27;。该讨论获得 333 分与 195 条评论，为 AI 对软件工程实践的影响提供了现实视角。

hackernews · QueensGambit · 11月20日 18:17 · [社区讨论](https://news.ycombinator.com/item?id=50579331)

**「背景」** AI 编码工具（如 Claude Code 等智能体）能够根据自然语言提示生成和修改代码，从而减少了开发者手动编写代码的需求。这一变化是本文讨论的前提：当动手编码工作逐渐由 AI 承担，开发者剩余的角色就变成审查、指导和架构设计，而非直接实现。

**「影响」** 具体后果已有实例：一位开发者报告，Claude 在审查其 IPA 输入法键盘项目时，会留下未标记的调试工具，使程序实质上成为键盘记录器。这提示使用 AI 编码代理的开发者需在代码审查中额外关注日志与调试基础设施的残留，而非仅依赖 AI 生成的代码。

**「社区讨论」** 社区讨论的核心分歧在于：有开发者认为工程师本就承担需求推敲与数据模型设计，AI 只是移除了键盘编码，角色本质未变；另一些评论者则反驳称这并非晋升，而是薪资更低、乐趣更少，开发者沦为 LLM 决策的&\#x27;责任承担者&\#x27;。另有评论指出，优秀团队本就要求成员身兼 PM、架构师、系统工程师等多重角色，AI 只是放大了这一趋势。

**标签**: `#AI`, `#software engineering`, `#developer roles`, `#LLM`, `#architecture`

---

<a id="item-tech-news-8"></a>
### [阿伦森博客探讨 AI&\#x27;随机鹦鹉&\#x27;证明黎曼猜想的可能性](https://scottaaronson.blog/?p=10344) ⭐️ 7.0/10

理论计算机科学家斯科特·阿伦森发表博客文章，探讨 AI&\#x27;随机鹦鹉&\#x27;可能已证明黎曼猜想的可能性，引发关于机器理解与数学发现的讨论。该文内容无法获取验证，且标题具有煽动性，应视为观点讨论而非已确认的数学突破。

hackernews · stratos123 · 11月20日 20:03 · [社区讨论](https://news.ycombinator.com/item?id=50581084)

**「背景」** 黎曼猜想由 Bernhard Riemann 于 1859 年提出，它断言素数沿数轴的分布由一种精细而有序的规律决定；而“随机鹦鹉”则是对大型语言模型的批评性比喻，指其生成文本时只模仿统计模式而不理解意义。Aaronson 的博文正是在这一背景下讨论 AI 是否可能“证明”黎曼猜想，而《科学美国人》此前报道的 Anthropic 数学家声称证明该猜想仍属未确认的声明。

**「社区讨论」** 评论者 janalsncm 以 Stockfish 国际象棋引擎为例，指出 AI 给出的&\#x27;解释&\#x27;实为大量计算的聚合，难以满足人类对&\#x27;为什么&\#x27;的追问；jstummbillig 则担忧人类将越来越无法理解科学和工程，沦为&\#x27;快乐的猫&\#x27;。这些观点属于个人意见，并非已证实的事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scottaaronson.blog/?p=10344">Shtetl-Optimized » Blog Archive » The stochastic parrots have...</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis , most...</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Riemann Hypothesis`, `#stochastic parrots`, `#theoretical computer science`

---

<a id="item-tech-news-9"></a>
### [美国 SEC 调查英伟达潜在会计问题](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627) ⭐️ 7.0/10

美国证券交易委员会（SEC）正在对英伟达（Nvidia）可能存在的会计问题进行调查，据知情人士透露。该调查目前仍处于调查阶段，尚未构成对违规行为的确认。对英伟达及其投资者而言，这一监管行动增加了不确定性，尤其是在公司融资和芯片销售做法受到关注的情况下。

hackernews · ftchd · 11月20日 20:22 · [社区讨论](https://news.ycombinator.com/item?id=50581438)

**「背景」** 英伟达此前已因向“新云”（neoclouds）提供融资安排而受到关注，这些安排被指涉及循环融资。在首席执行官离职后，公司面临更广泛的法律困境。

**「社区讨论」** 社区评论中，有用户指出，英伟达代理 CEO 兼前 CFO Colette Kress 自 2013 年起任职，质疑其是否对多年来的“黑市芯片销售”知情；另有用户认为这是过去五年困扰英伟达的“循环融资”问题的延续。这些是评论者的观点，并非已证实的事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investing.com/news/economy-news/exclusiveus-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-5042460">Nvidia ’s accounting is a focus of US SEC investigation, sources say...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/nvidia-financing-role-neoclouds-faces-181433179.html">Nvidia ’s financing role for neoclouds faces scrutiny after CEO exit</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#SEC`, `#accounting`, `#AI hardware`, `#regulation`

---

<a id="item-tech-news-10"></a>
### [美国收紧芯片出口，印度 Yotta 拟新增约 10 万块 GPU](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 7.0/10

美国收紧对马来西亚、泰国和新加坡的先进芯片出口后，印度 AI 业界认为可承接外溢需求。Yotta 宣布未来一年新增约 10 万块 GPU，相当于印度现有算力再增约 10%，但这是公司计划而非已交付能力。印度现有 153 个数据中心，居全球第 14；信实承诺投入至多 1100 亿美元、阿达尼 1000 亿美元建设 AI 基础设施，但长期仍受算力基础设施短缺与资本受限拖累。

telegram · zaihuapd · 11月20日 07:31

**「背景」** 美国收紧对马来西亚、泰国、新加坡的先进芯片出口，延续了此前对华芯片出口管制的思路；印度 AI 业界认为，这会使部分算力需求外溢到印度。印度现有 153 个数据中心、算力规模居全球第 14 位，长期受基础设施短缺和资本限制，因此 Yotta 计划新增约 10 万块 GPU（相当于现有算力再增约 10%）被视为承接这一需求的具体动作。

**「影响」** 对印度 AI 开发者和数据中心运营商而言，美国出口限制可能带来短期算力需求转移，但 Yotta 的 GPU 扩张仍属规划，且信实、阿达尼的大额投资尚未转化为可用算力；资本与基础设施瓶颈可能限制实际落地速度。

**标签**: `#AI infrastructure`, `#chip export controls`, `#India`, `#GPU`, `#data centers`

---

<a id="item-tech-news-11"></a>
### [OpenAI 上线后台模式：长任务可挂 8 小时，Token 最高省 40%](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI 推出后台模式，将长耗时 API 请求改为异步执行：在请求中设置 \`background: true\`，并通过 \`background\_options.completion\_window\` 选择 2 小时或 8 小时的完成时限，对应 Token 费率分别比标准价低 30% 和 40%；不设置时默认使用 \`soonest\`，无折扣。该功能目前在 GPT-6.2 Astra、GPT-6.2 Sol、GPT-6.1 Terra 和 GPT-6 Luna 上公测。后台模式会临时存储响应数据，即使 \`store\` 设为 false 或启用了零数据保留也不例外。

telegram · zaihuapd · 11月20日 11:15

**「背景」** 此前，OpenAI API 的长耗时请求以同步方式执行，连接需保持到任务完成，成本与等待时间随任务长度线性增长。后台模式将这类请求转为异步执行，让开发者以较低费率换取更长的完成窗口，适合批量推理、数据管道或长时间运行的代理任务。

**「影响」** 对运行长任务（如批量推理或长时间代理工作流）的开发者而言，选择 8 小时窗口可将 Token 成本降低 40%，但需接受最长 8 小时的延迟，并注意响应数据会在后台临时存储——即使已设置 \`store: false\` 或启用零数据保留，这一行为仍会生效，可能影响数据合规策略。

**标签**: `#OpenAI`, `#API`, `#background mode`, `#cost optimization`, `#async processing`

---

<a id="item-tech-news-12"></a>
### [特斯拉辅助驾驶获意大利批准，月费 99 欧元](https://www.ilfattoquotidiano.it/2026/11/20/tesla-assisted-driving-arriva-in-italia-via-libera-alla-guida-assistita-avanzata/8578482/) ⭐️ 7.0/10

特斯拉宣布其高级辅助驾驶系统已获意大利主管部门批准，将通过 OTA 推送，订阅价为每月 99 欧元。该系统可处理城市道路、路口与变道，但驾驶员须全程监控并承担法律责任。意大利是继荷兰之后第 12 个欧洲市场，特斯拉称欧洲累计行驶超 2 亿公里，碰撞率最多低至手动驾驶的七分之一，但该数据出自公司自有方法，未经独立验证。

telegram · zaihuapd · 11月20日 12:14

**「背景」** 特斯拉的高级辅助驾驶系统于 2026 年 4 月率先在荷兰上线，此次获意大利批准后，成为该系统进入的第 12 个欧洲市场。该系统此前已在多个欧洲国家获得批准，此次意大利的批准进一步扩大了其欧洲覆盖范围。

**「影响」** 对于意大利的特斯拉车主而言，每月 99 欧元的订阅费意味着使用该功能需要持续付费，且驾驶员仍需全程监控并承担事故责任，这限制了其作为完全自动驾驶的用途。此次批准也表明欧洲监管机构对辅助驾驶系统的态度正在逐步开放，但特斯拉的安全数据缺乏独立验证，仍需谨慎看待。

**标签**: `#autonomous driving`, `#Tesla`, `#regulatory approval`, `#AI systems`, `#Europe`

---

<a id="item-tech-news-13"></a>
### [KVM 漏洞 CVE-2026-99312 致 AMD 主机内存泄露](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 7.0/10

Linux 内核 KVM 组件存在 CVE-2026-99312 漏洞，仅影响启用嵌套虚拟化的 AMD 主机，攻击者可从虚拟机内读取宿主内存，研究人员已在 DigitalOcean 上实测读取约 127 GB。上游修复已于 11 月 18 日随稳定内核 7.3.5 等版本发布，但 Debian、Ubuntu 等发行版内核尚未包含该补丁。在补丁到位前，管理员可关闭嵌套虚拟化作为临时缓解措施。

telegram · zaihuapd · 11月20日 14:23

**「背景」** KVM（Kernel-based Virtual Machine）是 Linux 内核内置的虚拟化模块，负责在宿主机上运行虚拟机；嵌套虚拟化则允许虚拟机内部再运行虚拟机，从而扩大攻击面。CVE-2026-99312 正是出现在这一扩展路径上，使 AMD 主机上的虚拟机能够越界读取宿主内存。

**「影响与缓解措施」** 对于运行 AMD 主机并启用嵌套虚拟化的云服务商和用户，该漏洞意味着虚拟机内代码可读取宿主内存；DigitalOcean 研究人员实测从虚拟机内读取到约 127 GB 宿主内存。Intel 主机不受影响，因为漏洞代码仅存在于 KVM 对 AMD 嵌套虚拟化的支持路径中。上游已在 11 月 18 日随稳定内核 7.3.5 等发布修复，但 Debian、Ubuntu 等发行版内核尚未包含补丁；在补丁到位前，可关闭嵌套虚拟化作为缓解措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE - 2026 - 99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization, Responsible Disclosure , and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to- Host Escape | Terra Security Research</a></li>

</ul>
</details>

**标签**: `#security`, `#KVM`, `#AMD`, `#virtualization`, `#Linux kernel`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [为何 LLM 输出缓存不值得做](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 8.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** 输入缓存已是 LLM 推理的常规做法，但输出缓存看似同样诱人：编码智能体常把代码片段、证据文档在可见回复中重复引用，浪费了比输入更贵的输出 token。作者 Sean Goedecke 却认为，这种优化并不划算。

**「方案」** 关键在于可见输出只占全部输出 token 的极小部分。作者依据自己的智能体运行记录估算，约 50% 的输出 token 是推理 token，44% 是工具调用，留给可见输出的只有约 6%。即便乐观地省下可见输出的三分之二，按阿姆达尔定律也只减少总输出 token 的 4%。因此，与其缓存输出，不如削减那 94% 的不可见 token——这主要取决于模型智能：更聪明的模型用更少的推理和工具调用就能答对，所以单价贵 5 倍的模型反而可能因 token 消耗少 6 倍而更便宜。

**「启示」** 作者由此得出结论：输出缓存不值得做，真正该投入的是提升模型智能与 harness 质量，让模型少绕弯子、少调用工具，从而从源头节省输出成本。

**标签**: `#LLM caching`, `#Amdahl&\#x27;s law`, `#output tokens`, `#reasoning tokens`, `#agent economics`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [预测市场对 2026 年标普 500 触及 8000 点的概率骤降](https://www.cnbc.com/2026/11/20/sp-500-8000-kalshi-odds-ai-selloff.html) ⭐️ 7.0/10

据 CNBC 报道，Kalshi 预测市场上交易员认为标普 500 指数在 2026 年突破 8000 点的概率已从 10 月 13 日的 72%骤降至 6%，因人工智能相关科技股遭抛售，纳斯达克指数年内转跌，道指和标普 500 指数均进入回调区间。

rss · CNBC Finance · 11月20日 19:59

**「市场背景」** 人工智能相关股票的抛售已蔓延至全球市场，Anthropic 创纪录的 IPO 也未能止住跌势，同时市场普遍预期美联储将在 12 月加息，类似 2018 年的紧缩周期。

**「对投资者的影响」** 持有科技股和 AI 相关资产的投资者面临持续抛售压力，美联储 12 月加息预期是主要驱动因素；《股票交易者年鉴》预计 12 月中旬至下旬可能还有进一步下行空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off">Global stock markets slump as Anthropic IPO fails to stem AI sell - off</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-19/gold-set-for-worst-week-since-march-on-hawkish-fed-ai-selloff">Gold Set for Worst Week Since March on Hawkish Fed, AI Selloff</a></li>

</ul>
</details>

**标签**: `#stock market`, `#prediction markets`, `#AI sell-off`, `#Federal Reserve`, `#S&amp;P 500`

---

<a id="item-finance-news-2"></a>
### [美联储官员讲话增多，沃什回避前瞻指引引发市场不确定性](https://www.cnbc.com/2026/11/20/warsh-fed-forward-guidance-rate-hikes.html) ⭐️ 7.0/10

美联储主席沃什上任六个月来避免给出利率前瞻指引，但其他官员近期讲话频率创 2025 年初以来新高，且观点分歧加大。市场目前定价 12 月至少加息 25 个基点的概率为 100%。

rss · CNBC Finance · 11月20日 21:10

**「背景」** 沃什认为前瞻指引会束缚政策制定者，但美联储内部对通胀持续高于 3%目标（2%）的应对方式存在分歧，部分官员主张更激进加息。

**「影响」** 沟通分歧可能加剧利率市场波动，在动荡时期带来额外不确定性。

**标签**: `#Federal Reserve`, `#monetary policy`, `#forward guidance`, `#inflation`, `#interest rates`

---

<a id="item-finance-news-3"></a>
### [美国企业转向净发行股票，为牛市带来供应压力](https://www.cnbc.com/2026/11/20/equity-issuance-bull-market-problem.html) ⭐️ 7.0/10

美国企业已从回购股票转向净发行股票，截至上周晚些时候，净新增发行量达总市值的 3.1%。虽仍低于科技泡沫和疫情泡沫时期的峰值，但标志着回购时代结束，为持续四年的牛市带来新的供应压力。

rss · CNBC Finance · 11月20日 14:15

**「背景」** 此前企业回购减少了流通股，推高股价和每股收益；如今趋势逆转，新增供应成为潜在逆风。Baker-Wurgler 研究显示，股权发行相对债券发行增加时，后续市场回报往往较低。

**标签**: `#equity issuance`, `#stock buybacks`, `#market structure`, `#IPO activity`, `#bull market`

---

<a id="item-finance-news-4"></a>
### [阿里巴巴遭股东集体诉讼，被指隐瞒业务关系及出口管制风险](https://www.zaobao.com.sg/news/china/story20261120-10029652) ⭐️ 7.0/10

阿里巴巴 11 月 19 日在纽约曼哈顿联邦法院遭股东集体诉讼，被指在 2024 至 2026 年年报中低估出口管制违规风险并隐瞒与 Alice Huang 及新加坡公司超速国际的业务关系。诉状称，相关报道令股价四个交易日内跌 14%，索赔金额未列明。

telegram · zaihuapd · 11月20日 09:32

**「背景」** 诉讼源于此前报道指阿里巴巴与黄仁勋丑闻相关人物 Alice Huang 及新加坡公司超速国际（Megaspeed，前身 7Road International）有关联；超速国际为英伟达云合作伙伴，黄仁勋曾向董事会否认与 Alice Huang 有不正当关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.freemalaysiatoday.com/category/business/2026/11/20/alibaba-accused-of-hiding-ties-to-suspected-spy-in-nvidia-scandal">Alibaba accused of hiding ties to suspected spy in Nvidia scandal | FMT</a></li>
<li><a href="https://www.wired.com/story/jensen-huangs-lying-alarmed-nvidia-board-ahead-of-his-resignation/">Jensen Huang ’s ‘Lying’ Alarmed Nvidia Board Ahead of His... | WIRED</a></li>
<li><a href="https://www.zerohedge.com/political/gpus-capri-sunsets-and-detained-husband-who-alice-huang">GPUs, Capri Sunsets, And A Detained Husband: Who Is Alice ...</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#shareholder lawsuit`, `#class action`, `#export controls`, `#stock decline`

---

<a id="item-finance-news-5"></a>
### [北京拟明确租房正常损耗不得扣减押金](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

北京市住建委与市场监管局 20 日起就《北京市住房租赁合同（示范文本）（修订征求意见稿）》公开征求意见，拟明确承租人正常使用造成的房屋正常损耗不承担赔偿责任，出租人不得以此为由扣减押金。征求意见稿还要求转租经营的租赁企业将租押金付至监管账户。

telegram · zaihuapd · 11月20日 13:46

**「背景」** 该文件为住房租赁合同示范文本的修订稿，目前处于公开征求意见阶段，尚未正式生效。

**「影响」** 若正式通过，北京租房者将免于因正常损耗被扣押金，转租经营企业则需将租押金纳入监管账户。

**标签**: `#housing policy`, `#rental market`, `#consumer protection`, `#Beijing`, `#regulation`

---