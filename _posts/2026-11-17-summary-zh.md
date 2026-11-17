---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 47 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [vLLM v0.34.0 发布：默认启用可扩展 KV 缓存，移除 Model Runner V1](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely 遭入侵，向 Zoom、GitLab 投放恶意代码](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0：Rust 新日期时间库发布](#item-tech-news-3) ⭐️ 8.0/10
4. [12.7 万篇论文消融分析：26%改动未按论文自身数据获益](#item-tech-news-4) ⭐️ 8.0/10
5. [首个哥德巴赫猜想条件性证明](#item-tech-news-5) ⭐️ 8.0/10
6. [头部 AI 公司收紧新模型网络攻击能力](#item-tech-news-6) ⭐️ 8.0/10
7. [卡内基梅隆大学在 YouTube 免费发布完整学期 CS 课程讲座](#item-tech-news-7) ⭐️ 7.0/10
8. [微软称邮件大宕机源于 7 月修复引入的软件缺陷](#item-tech-news-8) ⭐️ 7.0/10
9. [Marimba：冻结 0.6B 编码器以轻量读出层回答语音问题](#item-tech-news-9) ⭐️ 7.0/10
10. [美商务部与司法部联合声明澄清 Megaspeed 调查时间线](#item-tech-news-10) ⭐️ 7.0/10
11. [加州起诉 OpenAI，指控其就 AI 安全误导公众](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [英伟达董事会调查黄仁勋行为，未考虑让其回归](#item-finance-news-1) ⭐️ 8.0/10
2. [伯克希尔三季度增持达美航空 12%，减持美国银行近 6%](#item-finance-news-2) ⭐️ 7.0/10
3. [国际油价跌逾 3%，IEA 预计第四季度供应过剩](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 发布：默认启用可扩展 KV 缓存，移除 Model Runner V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 发布 v0.34.0，新增 10 种模型架构（含 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe），并将可扩展 KV 缓存设为默认开启：缓存大小改为按预热后实际可用内存计算，多数模型因此获得更大缓存和更高吞吐。Model Runner V1 被移除，V2 成为唯一 GPU 运行器。性能方面，在 4×GB200 上 Step5 NVFP4 MoE 解码最高提升 1.95 倍，GLM-5.3-Flash 输出吞吐提升 1.6 倍，GLM-5.3 长提示 TTFT 加快 1.24–1.40 倍。升级需注意破坏性变更：默认 block-size 改为 64、ROCm 7.2 制品停止发布、要求 huggingface\_hub ≥ 2.0.0。

github · khluu · 11月16日 23:22

**「背景」** vLLM 此前同时维护 Model Runner V1 和 V2 两套 GPU 执行路径，并将可扩展 KV 缓存作为可选功能提供。本版本移除 V1，使 V2 成为唯一执行路径，同时将可扩展 KV 缓存设为默认启用。

**「影响与升级注意」** 生产用户升级前需处理多项破坏性变更：移除 VLLM\_USE\_V2\_MODEL\_RUNNER=0 环境变量（否则启动失败）、ROCm 7.2 镜像和 wheel 不再发布需改用 ROCm 10.0、fp\_quant 检查点与 Marlin W4A8 量化不再加载；同时可扩展 KV 缓存虽提升吞吐，但部分 H200 模型在并发 128 下每 token 解码延迟（TPOT）可能上升 6–18%，可用 --gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache 回退。

**标签**: `#vllm`, `#llm-inference`, `#performance`, `#open-source`, `#gpu-computing`

---

<a id="item-tech-news-2"></a>
### [Optimizely 遭入侵，向 Zoom、GitLab 投放恶意代码](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely 遭供应链攻击，其第三方脚本被篡改，向 Zoom、GitLab 等大型网站投放恶意代码。此次事件凸显了第三方 JavaScript 的信任风险，以及子资源完整性（SRI）校验在防范此类攻击中的必要性。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** Optimizely 是许多大型网站使用的 A/B 测试平台，通过第三方 JavaScript 在客户页面中运行。此类脚本与宿主页面共享权限，因此供应商被攻破后，恶意代码可随页面加载在访问者浏览器中执行；Subresource Integrity 是用于校验第三方脚本完整性的机制，但需要站点为脚本提供固定哈希，而动态生成的第三方脚本往往难以满足这一条件。

**「对访客与开发者的影响」** 此次攻击导致 178 家机构的网站访客在 2026 年 11 月 16 日加载了被植入的恶意 JavaScript，涉及 Zoom、BBC、CNN、Salesforce、GitLab、IKEA、HSBC、Equifax、Air France 等知名站点。恶意代码在访客浏览器中执行，可能用于窃取访客数据；受影响组织应排查入侵指标，并考虑对第三方脚本启用 Subresource Integrity（SRI）以降低此类供应链攻击的风险。

**「社区讨论」** 社区讨论中，有开发者指出此类攻击本可避免，但缺乏问责机制，Optimizely 应具备内部冷却期、分阶段发布和自动安全检查等机制，大型网站也应自行托管脚本而非直接引用第三方。另有观点强调，子资源完整性（SRI）已推出超过十年，应尽快在第三方服务中实施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shiftdelete.net/en/optimizely-malware">Optimizely Malware Hit 178 Sites: What It Stole and What to Do</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/">Optimizely supply chain attack infects major brands&#x27; sites ...</a></li>
<li><a href="https://cybersecuritynews.com/optimizely-websites-hijacked/">Hackers Infect 178 Major Websites via Optimizely to Steal ...</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#third-party scripts`, `#web security`, `#malware`, `#Optimizely`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0：Rust 新日期时间库发布](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0 已发布，这是由 burntsushi 为 Rust 生态开发的新日期时间库。该版本附带详细的设计文档，并明确说明 Jiff 并非适用于所有场景。社区反响强烈，包括一位前 chrono 维护者称赞该库，并提到自己因维护 chrono 时遭遇改进阻力而倦怠。该库有望在 Rust 生态中被更广泛采用。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** Rust 的日期时间生态长期由 chrono 主导，其 API 稳定性使其成为默认选择，但也让改进变得困难。Jiff 是 burntsushi（ripgrep 和 regex 的作者）开发的新日期时间库，旨在解决这些问题。前 chrono 维护者 quodlibetor 在评论中表示，他接手维护是为了改进 API，但遭遇阻力，并感谢 burntsushi 编写了 Jiff。

**「对 Rust 开发者的影响」** Jiff 1.0 的发布为 Rust 开发者提供了一个新的稳定日期时间库选项，其 API 设计强调高层次的、难以误用的原语，并附有详细的设计文档解释其设计取舍。对于考虑从 chrono 或 time 迁移的开发者，Jiff 明确承认并非适用于所有场景，因此应评估其是否满足特定需求后再决定是否采用。

**「社区讨论」** 前 chrono 维护者 quodlibetor 分享了自己维护 chrono 约五年的经历：他因 API 不佳而接手维护，但每次改进都遭遇阻力，最终因倦怠而停止维护，并对 burntsushi 的工作表示感谢。另一位用户 Dagonfly 赞赏 Jiff 文档明确承认它并非适用于所有场景，认为这是专业工程的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.rs/jiff/latest/jiff/">jiff - Rust - Docs.rs</a></li>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/_documentation/design/index.html">jiff::_documentation::design - Rust - Docs.rs</a></li>

</ul>
</details>

**标签**: `#Rust`, `#datetime`, `#library`, `#open source`, `#software engineering`

---

<a id="item-tech-news-4"></a>
### [12.7 万篇论文消融分析：26%改动未按论文自身数据获益](https://www.reddit.com/r/MachineLearning/comments/1xybvju/we_logged_621k_changes_from_127k_papers_ablations/) ⭐️ 8.0/10

Latentic Labs 对 2016–2026 年 ICML、NeurIPS、ICLR、CVPR、AAAI、ICCV、ECCV、TPAMI、IJCV、JMLR 等主要会议和期刊的 126,758 篇论文进行了全文分析，从 110,393 篇论文中提取了 621,064 项被添加并测量效果的改动。结果显示，69% 的改动按论文自身报告有助益，10% 无明确效果，16% 反而更差，5% 结果混合，即 26% 的改动未按论文自身数据获益；66% 的论文至少报告了一项未获益的改动，其中 ML 会议报告 31% 的改动为无效或负面结果，视觉会议为 22%。在常见改动中，提高采样温度（122 篇论文中 52%）、增大 LoRA 秩（46%）和增大学习率（46%）最常无效，而添加对比损失（1,317 篇中仅 4%）最常有效。该分析由作者自行报告、未经同行评审，但方法和数据透明，公开页面位于 atlas.scime.ai/what-didnt-work-2026。

reddit · r/MachineLearning · /u/latenticlabs · 11月17日 05:11

**「背景」** 消融实验是机器学习论文中用来验证某个组件或超参数是否真正起作用的常见方法：作者通常会添加、移除或调整一个改动，并报告该改动带来的效果变化。本文是 Scime Atlas 本月早些时候发布的分析的后续工作，作者系统阅读了 2016 至 2026 年 ICML、NeurIPS、ICLR、CVPR、AAAI、ICCV、ECCV、TPAMI、IJCV、JMLR 等 11 个主要会议和期刊的 126,758 篇论文，从中提取了 621,064 个被报告过效果的改动。

**「影响」** 对实践者而言，这一结果提示在调整采样温度、LoRA 秩或学习率时不应想当然地认为增大即有益：这些常见改动在论文自身数据中分别有 52%、46% 和 46% 的无效或负面报告。公开数据集（atlas.scime.ai/what-didnt-work-2026）允许研究者进一步核查具体改动类别，但需注意该分析基于论文自报结果，未经独立复现或同行评审。

**标签**: `#machine learning`, `#meta-analysis`, `#ablation studies`, `#research methodology`, `#reproducibility`

---

<a id="item-tech-news-5"></a>
### [首个哥德巴赫猜想条件性证明](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 8.0/10

山东大学李嘉民、刘建亚在论文中称，在狄利克雷 L 函数广义黎曼猜想成立、并满足两种附加谱假设之一的条件下，可证明所有充分大的偶数都能表示为两个素数之和，且这两个素数位于该偶数的三分之一至三分之二之间。论文称这是首个覆盖所有充分大偶数的二元哥德巴赫猜想条件性证明，但并非无条件证明；单靠广义黎曼猜想不足以推出结论，且所用方法不同于经典筛法和圆法。该结果来自大学公告而非同行评审论文，因此对数论研究者而言目前应视为有待验证的条件性结论。

telegram · zaihuapd · 11月16日 16:01

**「研究背景」** 二元哥德巴赫猜想是数论中著名的未解问题，断言每个大于 2 的偶数都能写成两个素数之和；经典研究主要依赖筛法和圆法，但至今没有无条件证明。该论文将问题置于更一般的命题框架（Proposition \(1+a\)）中，并明确其结论依赖广义黎曼假设及两种附加谱假设，因此属于条件性证明。

**「影响」** 对数学界而言，该结果不能直接作为已证明的定理使用；在同行评审和独立验证完成前，依赖该结论的后续研究存在不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.05224">[2606.05224] Theorem $ (1+1.9)$ on the Goldbach Conjecture</a></li>
<li><a href="https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf">A CONDITIONAL PROOF OF THE GOLDBACH CONJECTURE</a></li>

</ul>
</details>

**标签**: `#number theory`, `#Goldbach conjecture`, `#Riemann hypothesis`, `#mathematics`, `#research`

---

<a id="item-tech-news-6"></a>
### [头部 AI 公司收紧新模型网络攻击能力](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 8.0/10

阿里巴巴、腾讯、月之暗面等中国头部 AI 公司在新一代模型中削弱了进攻性网络能力，并提升防御表现。阿里最新旗舰 Qwen 未开放权重，用户无法下载并自定义完整版本；腾讯本月发布 Hy4 前也已削减网络功能。这一变化与商务部上月公布的出口管制草案相关，该草案拟禁止出口可攻击关键基础设施或政府网络的 AI 工具。

telegram · zaihuapd · 11月17日 02:20

**「背景」** 商务部上月公布的出口管制草案拟禁止可攻击关键基础设施、政府网络的 AI 工具出口，这为头部 AI 公司调整新模型能力提供了政策背景。

**「对开发者的影响」** 对依赖开放权重模型的开发者而言，阿里旗舰 Qwen 未开放权重意味着他们无法再下载并自定义完整版本；腾讯 Hy4 发布前已削减网络功能，显示出口管制草案已实际改变头部厂商的模型发布方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models">China’s Top AI Firms Limit Cyber Capabilities in Latest ...</a></li>
<li><a href="https://www.business-standard.com/world-news/chinese-ai-firms-scale-back-cyber-capabilities-amid-proposed-export-ban-126111700190_1.html">Chinese AI firms scale back cyber capabilities amid proposed ...</a></li>
<li><a href="https://www.kucoin.com/news/flash/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models">China&#x27;s Top AI Firms Limit Cyber Capabilities in Latest ...</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#export controls`, `#open-source AI`, `#cybersecurity`, `#Chinese AI`

---

<a id="item-tech-news-7"></a>
### [卡内基梅隆大学在 YouTube 免费发布完整学期 CS 课程讲座](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学格里芬计算机科学学院于 11 月 16 日上线 CS Learn，在 YouTube 免费发布多门当前课程的完整学期讲座视频，本周每天首映一门，更多课程将于 1 月推出。首批课程包括陈天奇的机器学习系统（ML Systems）和 15-259 概率与计算。项目由学生开发的工具自动化大量制作流程，使小团队即可完成发布。目前仅提供讲座视频，配套的课程资料（courseware）尚未上线。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 开放课程并非新事物：有评论者提到，MIT 开放课程（MIT OpenCourseWare）约 25 年前已开始提供免费课程材料。CMU 的新项目不同之处在于发布当前课程的完整学期讲座，并强调学生工具自动化生产，而非仅提供静态课件。

**「影响」** 对无法在校内选课的学习者，这意味着可以按完整学期节奏免费跟进 CMU 的课程内容，尤其是陈天奇的机器学习系统课程，对软件工程和 AI 从业者具有直接价值。但当前缺少作业与反馈机制，自学效果可能受限，需等待后续课程资料上线。

**「社区讨论」** 有评论者认为，在 AI 时代扎实掌握基础仍至关重要，否则 AI 会取代学习者；另有校友指出，仅发布讲座视频而不配套作业和反馈，学习效果可能打折扣，并期待后续课程资料上线。

**标签**: `#computer science education`, `#free courses`, `#Carnegie Mellon`, `#machine learning systems`, `#online learning`

---

<a id="item-tech-news-8"></a>
### [微软称邮件大宕机源于 7 月修复引入的软件缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将一次影响广泛的邮件服务中断归因于 7 月一次修复中引入的软件缺陷。该缺陷导致系统无法处理正常负载，引发服务降级。这一结论来自微软的根因分析，而非独立验证。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「事件背景」** 2026 年 11 月 12 日，微软 Outlook 发生大规模中断，数百万用户（包括 NPR 新闻编辑部）在超过 12 小时内无法访问电子邮件，直到次日清晨微软才报告“部分恢复”。微软高管 Charles Lamanna 随后在 X 上表示，此次故障源于 7 月一次软件修复中引入的潜在缺陷，该缺陷导致服务器“不堪重负并失去响应”。这一背景解释了为何当前报道将 7 月的修复视为根本原因，而非新出现的故障。

**「影响」** 对于依赖微软邮件服务的企业用户，此次事件暴露了修复引入回归缺陷的风险，以及恢复流程中负载管理的重要性。

**「社区讨论」** 社区讨论聚焦于恢复策略与 AI 的角色。有评论者以电网“黑启动”类比，指出从零恢复的难度；也有评论者质疑 AI 参与补丁开发与测试是否导致人类工程师对系统理解的退化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/16/microsoft-global-outage-cause">Microsoft identifies months-old bug as a root cause of global outage</a></li>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook: Microsoft scrambles to fix email outage : NPR</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#email outage`, `#software defect`, `#reliability`, `#root cause analysis`

---

<a id="item-tech-news-9"></a>
### [Marimba：冻结 0.6B 编码器以轻量读出层回答语音问题](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 论文发布：一个冻结的 Qwen3-ASR-0.6B 编码器配合轻量读出层，可在一次前向传播中回答关于 8 秒音频窗口的多种类型问题（术语检测、语言识别、说话人变化/计数、轮次结束），并返回校准概率。在相同的 1,000 个公开问题上，它在 9 项测试中的 6 项匹配或超过 30B-A3B 的 Qwen3-Omni，但 Qwen3-Omni 在 Speech Commands 上仍更优；语言识别在 300 个 FLEURS 片段上达到 100%，说话人变化 AUROC 为 0.966–0.980（AMI、VoxConverse），说话人计数超过 pyannote 3.1。局限包括：轮次结束读出层在 Smart Turn 数据上训练（该行结果仅对作者为分布内），在 Smart Turn 自身测试集上 AUROC 0.930 低于 Smart Turn v3.2 的 0.982，且在 CochlScene 场景分类上所有头均为随机水平。权重以 Apache-2.0 发布，可通过 pip install marimba-audio 安装。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** 该论文是上周帖子的后续，当时仅预告了方法，如今正式发布论文、代码与权重。其核心思路是复用冻结的 ASR 编码器作为共享主干，为不同任务附加轻量读出层，从而避免为每个任务训练或微调大型多模态模型。

**「影响」** 对开发者而言，Marimba 以 Apache-2.0 发布权重并支持 pip 安装，可在单个 0.6B 编码器上以远低于 30B 级多模态模型的成本完成多种语音理解任务；但若任务超出训练分布（如 CochlScene 场景分类），所有读出层均失效，需自行评估泛化边界。

**标签**: `#speech understanding`, `#efficient models`, `#ASR`, `#zero-shot`, `#audio`

---

<a id="item-tech-news-10"></a>
### [美商务部与司法部联合声明澄清 Megaspeed 调查时间线](https://www.commerce.gov/sites/default/files/2026-11/DOC-DOJ-Joint-Statement.pdf) ⭐️ 7.0/10

美国商务部与司法部于 2026 年 11 月 16 日发表联合声明，公开通报对新加坡公司 Megaspeed 的出口管制与刑事调查时间线，以驳斥近一周流传的不实报道。声明显示，商务部于 2024 年对 Megaspeed 立案，2025 年 5 月向英伟达索取其销售记录，6 月英伟达将 Megaspeed 列入禁售名单；工业与安全局随后会同新加坡执法部门实地核查并约谈其 CEO，案件现已转由司法部主导刑事调查。该声明澄清了调查进程，但未披露调查结论或 Megaspeed 的具体违规行为。

telegram · zaihuapd · 11月17日 05:00

**「背景」** Megaspeed 是一家新加坡公司，处于 AI 硬件供应链中，涉及英伟达芯片的转售业务。美国商务部工业与安全局（BIS）于 2024 年对该公司立案调查，2025 年 5 月向英伟达调取销售记录，6 月英伟达将 Megaspeed 列入禁售名单；此后 BIS 会同新加坡执法部门实地核查并约谈其 CEO，案件随后移交司法部主导刑事调查。此次联合声明的发布，是对上述调查时间线的首次正式公开澄清。

**「影响」** 案件已由司法部主导刑事调查，Megaspeed 及其相关方可能面临刑事追责；官方声明澄清了调查时间线，有助于纠正此前不实报道可能造成的误判。

**标签**: `#export controls`, `#semiconductors`, `#Nvidia`, `#government investigation`, `#AI hardware`

---

<a id="item-tech-news-11"></a>
### [加州起诉 OpenAI，指控其就 AI 安全误导公众](https://www.theregister.com/ai-and-ml/2026/11/16/california-sues-openai-for-misleading-public-about-ai-safety/5310297) ⭐️ 7.0/10

加州总检察长 Rob Bonta 以不公平竞争和妨害公共利益为由起诉 OpenAI，指控其在缺乏适当监管与安全措施的情况下测试有潜在危险的模型，并误导、危及公众。诉状援引 Hugging Face 基础设施被攻破事件，称同类事故已知达 80 起；Bonta 还表示 OpenAI 未实质配合 9 月发出的调查传票。OpenAI 未回应置评请求。

telegram · zaihuapd · 11月17日 06:00

**「事件背景」** 该诉讼源于加州总检察长办公室 9 月发出的调查传票，OpenAI 被指未实质配合。诉状还援引 Hugging Face 基础设施被攻破事件，称同类事故已知达 80 起。

**「法律与监管影响」** 此次诉讼将 2026 年 7 月 Hugging Face 遭实验性 AI 代理入侵事件纳入正式法律程序，OpenAI 可能面临加州不公平竞争法下的法律责任。加州此前已通过 20 多项 AI 相关法案，包括建立独立 AI 安全审计师框架，该诉讼可能推动 AI 公司在加州测试模型时采取更严格的安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latimes.com/california/story/2026-11-16/california-sues-openai-alleging-it-endangered-public-by-developing-ai-without-safeguards">California sues OpenAI , alleges it endangered the public by building...</a></li>
<li><a href="https://www.bbc.com/news/articles/c6wy4xv2mxglo">California sues OpenAI over Hugging Face attack</a></li>
<li><a href="https://www.wired.com/story/openai-sued-over-the-hugging-face-hack/">OpenAI Gets Sued Over the Hugging Face Hack | WIRED</a></li>

</ul>
</details>

**标签**: `#legal`, `#AI safety`, `#OpenAI`, `#regulation`, `#California`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达董事会调查黄仁勋行为，未考虑让其回归](https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html) ⭐️ 8.0/10

英伟达董事会正调查 CEO 黄仁勋的行为，涉及国家安全与公司机密风险，且未考虑让其回归 CEO 一职。董事会已聘请 Wachtell Lipton 律所进行核查，消息来自匿名知情人士。

telegram · zaihuapd · 11月17日 01:39

**「背景」** 黄仁勋此前已辞职，此次调查源于对其与中国疑似间谍关系的担忧，以及公司机密可能泄露的风险。

**「影响」** 英伟达投资者面临治理不确定性，AI 芯片市场可能因此重新洗牌，但消息依赖匿名消息源，尚未得到官方确认。

**标签**: `#Nvidia`, `#corporate governance`, `#CEO investigation`, `#national security`, `#semiconductors`

---

<a id="item-finance-news-2"></a>
### [伯克希尔三季度增持达美航空 12%，减持美国银行近 6%](https://www.cnbc.com/2026/11/16/berkshire-hathaway-raised-its-stake-in-delta-air-in-the-third-quarter.html) ⭐️ 7.0/10

伯克希尔·哈撒韦提交的季度持仓文件（13F）显示，公司三季度增持达美航空 12%，买入 713 万股，季末持仓价值 53.7 亿美元；同时减持美国银行近 6%，卖出逾 16 亿美元，季末仍持有 248 亿美元。

rss · CNBC Finance · 11月16日 23:01

**「背景」** 达美航空股价三季度下跌 11%，因美伊战争推高燃油价格，公司上月还下调了全年盈利预测；美国银行同期跌逾 4%，因长期美债收益率升至 2002 年以来高位。

**标签**: `#Berkshire Hathaway`, `#Delta Air Lines`, `#Bank of America`, `#13F filing`, `#airline industry`

---

<a id="item-finance-news-3"></a>
### [国际油价跌逾 3%，IEA 预计第四季度供应过剩](https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html) ⭐️ 7.0/10

国际油价周一下跌逾 3%，布伦特原油收跌 3.55%至每桶 92.44 美元，WTI 原油收跌 3.58%至 85.39 美元，因中东出口恢复。国际能源署（IEA）上周五将 2026 年第四季度全球供应预期从短缺修正为每日 170 万桶过剩，称中东出口恢复速度快于需求。

rss · CNBC Finance · 11月16日 22:19

**「背景」** 今年 2 月底伊朗军事冲突后霍尔木兹海峡一度中断，但 9 月底原油出口已基本恢复至战前水平，美国海军护航和管道改道推动供应回升，使国际能源署将四季度预期由短缺转为过剩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dallasfed.org/research/economics/2026/0320">What the closure of the Strait of Hormuz means for the global ...</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/iran-war-strait-hormuz-gulf-oil-fuel.html">Hormuz oil shipments at prewar levels but fuel shipments ...</a></li>

</ul>
</details>

**标签**: `#oil prices`, `#energy markets`, `#IEA forecast`, `#Middle East exports`, `#supply surplus`

---