---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 47 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely 遭供应链攻击，Zoom 和 GitLab 等网站被植入恶意代码](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0：Rust 日期时间库稳定版发布](#item-tech-news-3) ⭐️ 8.0/10
4. [Scime Atlas：126,758 篇论文中 26%改动未提升性能](#item-tech-news-4) ⭐️ 8.0/10
5. [卡内基梅隆大学免费开放 CS 课程](#item-tech-news-5) ⭐️ 7.0/10
6. [微软将邮件大规模中断归因于 7 月修复引入的软件缺陷](#item-tech-news-6) ⭐️ 7.0/10
7. [Marimba：基于冻结 Qwen3-ASR 的轻量语音问答系统](#item-tech-news-7) ⭐️ 7.0/10
8. [谷歌拟向日本提供 Fairwind AI 模型用于网络防御](#item-tech-news-8) ⭐️ 7.0/10
9. [加州起诉 OpenAI，指控其就 AI 安全误导公众](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [Nvidia CEO 黄仁勋辞职，AI 芯片股本周上涨](#item-finance-news-1) ⭐️ 8.0/10
2. [坎托·菲茨杰拉德减持英伟达股份近 50%，引发利益冲突质疑](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 发布 v0.34.0，包含 1,061 次提交、412 位贡献者（其中 120 位为新贡献者），新增 10 种模型架构，包括 Mistral Large 4、MiniMax-M3.1-Flash 和 NVIDIA Nemotron-3.5-Transcribe。该版本默认启用可扩展 KV 缓存，KV 缓存大小基于预热后实际可用内存计算，使大多数模型获得更大缓存和更高吞吐量；同时移除 Model Runner V1，Model Runner V2 成为唯一 GPU 运行器。性能方面，在 4×GB200 上 Step5 NVFP4 MoE 解码最高提升 1.95 倍，GLM-5.3-Flash 输出吞吐量提升 1.6 倍。升级需注意破坏性变更：默认 block-size 从 16 改为 64，ROCm 7.2 镜像停止发布，huggingface\_hub 需 &gt;= 2.0.0。

github · khluu · 11月16日 23:22

**「背景」** vLLM 是广泛使用的开源大语言模型推理引擎。此前版本中，Model Runner V2 作为可选运行器与 V1 并存，可扩展 KV 缓存也需显式开启；v0.34.0 将两者分别转为唯一运行器和默认行为，并带来相应性能收益与配置迁移成本。

**「影响」** 现有部署升级前需处理多项破坏性变更：设置 --block-size 16 可保持旧行为，ROCm 7.2 用户需迁移到 ROCm 10.0 镜像，且需升级 huggingface\_hub 至 2.0.0 以上；此外，可扩展 KV 缓存在部分 H200 模型高并发（128）下会使每 token 解码延迟上升 6–18%，可通过 --gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache 关闭。

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#GPU`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Optimizely 遭供应链攻击，Zoom 和 GitLab 等网站被植入恶意代码](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely 这一广泛使用的第三方脚本遭到供应链攻击，导致 Zoom、GitLab 等大型网站向访问者分发恶意代码。攻击者通过篡改 Optimizely 的发布流程，将恶意脚本注入到依赖该服务的网站中。此次事件凸显了第三方脚本带来的安全风险，以及网站运营方在依赖外部供应商时缺乏足够防护措施的问题。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** 第三方脚本（如 Optimizely）通常由供应商 CDN 直接提供，并拥有与页面同等的执行权限，这使其成为供应链攻击的常见入口。本次事件中，恶意 JavaScript 被注入 Optimizely 自身的代码片段（而非 CDN 缓存投毒），最终影响了包括 Zoom、GitLab 在内的 178 家组织。

**「影响与应对」** 依赖第三方脚本的网站需要立即评估其供应链风险。社区讨论指出，Subresource Integrity（SRI）技术已可用超过十年，但许多大型网站仍未实施；同时，将关键脚本本地化（vendoring）或使用 NoScript 等工具可减少暴露面。

**「社区讨论」** 社区评论指出，Google Tag Manager 的设计初衷是让营销部门无需工程团队即可添加标签，这导致了大量 JavaScript 的加载（stickfigure）。有观点认为，Optimizely 应具备内部冷却、分阶段发布和自动安全检查等机制，而大型网站也不应直接依赖第三方脚本，而应将其本地化（mcoliver）。另有评论强调，Subresource Integrity 已可用超过十年，是时候开始实施（jdorfman）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50524767">Optimizely compromised , served malware on Zoom , GitLab</a></li>
<li><a href="https://gizmodo.com/sprawling-malware-attack-reportedly-affects-zoom-cnn-fox-news-peacock-and-170-others-2000840831">Sprawling Malware Attack Reportedly Affects Zoom and Other Major...</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#third-party scripts`, `#web security`, `#subresource integrity`, `#malware`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0：Rust 日期时间库稳定版发布](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0 是 burntsushi 发布的 Rust 日期时间库稳定版本，提供现代、有主见的设计，可作为 chrono 的替代选择。该库已进入 1.0 稳定阶段，文档明确承认它并非所有场景都适用，并提供了与其他 Rust 日期时间库的对比。项目获得社区广泛关注，但尚需时间验证其生态采用情况。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** chrono 是 Rust 生态中长期以来的标准日期时间库，但其 API 的稳定性也使得改进举步维艰；前 chrono 维护者 quodlibetor 在评论中表示，他接手维护正是希望改善 API，但每次微小的改进都遭到阻力，最终因看不到改进路径而停止维护。Jiff 1.0 正是 burntsushi 在这种背景下推出的现代替代方案，旨在提供更清晰、更符合直觉的日期时间处理 API。

**「影响」** 对于依赖 chrono 的 Rust 项目，Jiff 1.0 提供了一个稳定的替代日期时间库，但迁移前需评估其 opinionated 设计是否匹配项目需求，因为 Jiff 文档明确承认它并非总是正确的工具；chrono 仍是生态中功能完整的既有库。

**「社区讨论」** 前 chrono 维护者 quodlibetor 表示，他接手维护是因为 chrono 的 API 不佳，但用户依赖其稳定性，任何改进都遭遇阻力，最终因看不到改进路径而倦怠；另有评论者赞赏 Jiff 明确承认自己并非所有场景都适用，认为这是专业工程态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.rs/chrono/latest/chrono/">Chrono : Date and Time for Rust</a></li>

</ul>
</details>

**标签**: `#Rust`, `#datetime`, `#library`, `#chrono`, `#time handling`

---

<a id="item-tech-news-4"></a>
### [Scime Atlas：126,758 篇论文中 26%改动未提升性能](https://www.reddit.com/r/MachineLearning/comments/1xybvju/we_logged_621k_changes_from_127k_papers_ablations/) ⭐️ 8.0/10

Latentic Labs 对 2016–2026 年间 126,758 篇机器学习论文（ICML、NeurIPS、ICLR、CVPR、AAAI、ICCV、ECCV、TPAMI、IJCV、JMLR）进行了全文分析，提取出 110,393 篇论文中的 621,064 项改动及其报告效果。结果显示，69% 的改动有助益，10% 无明确效果，16% 反而更差，5% 结果混合；66% 的论文至少报告了一项未带来提升的改动。在常见改动中，提高采样温度（122 篇中 52%）、增大 LoRA 秩（46%）和增大学习率（46%）最常无效，而添加对比损失（1,317 篇中仅 4%）最常有效。机器学习会议报告 31% 的改动为无效或负面结果，视觉会议为 22%。

reddit · r/MachineLearning · /u/latenticlabs · 11月17日 05:11

**「背景」** 消融实验是机器学习论文中通过添加、移除或调整某个组件（如损失函数、层、数据量、学习率）来测量其贡献的常见方法。本文是作者对本月早些时候 Scime Atlas 相关帖子的后续，将这一分析扩展到 2016–2026 年 11 个会议和期刊的 126,758 篇论文，并逐篇提取其中报告的改变及其效果。

**「影响」** 对研究人员和从业者而言，这一结果提示常见超参数调整（如提高采样温度、增大 LoRA 秩或学习率）并非总能带来改进，约三分之一的改动在论文自身数据中未显示正面效果。在采用这些改动前，应参考该分析或进行小规模验证，而非仅依赖惯例。

**标签**: `#machine learning`, `#ablation studies`, `#research methodology`, `#meta-analysis`, `#reproducibility`

---

<a id="item-tech-news-5"></a>
### [卡内基梅隆大学免费开放 CS 课程](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学于 11 月 16 日推出 CS Learn 项目，在 YouTube 上免费发布当前计算机科学课程的全学期讲座视频，本周每天首播一门课程，明年 1 月将追加更多课程。首批课程包括 Tianqi Chen 的机器学习系统（ML Systems）和 15-259 概率与计算（Probability and Computing）。该项目由学生开发工具自动化制作流程，使小团队能够完成大规模课程录制。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 开放课程（OpenCourseWare）并非新概念——正如发起人 Phillip Compeau 在评论中所指出的，麻省理工学院约 25 年前就已开始免费公开课程材料。卡内基梅隆大学此次将完整学期课程视频上传至 YouTube，延续了这一传统，并借助学生自建工具降低制作成本。CMU 此前已有官方 YouTube 频道（tool-1-2），但新频道（tool-1-1）专门用于发布完整课程播放列表。

**「影响」** 对全球学习者而言，这意味着无需注册即可获得顶尖院校的完整课程视频；但评论指出，目前只有讲座视频，缺少项目练习和反馈，课程效果可能打折扣，需等待后续课件上线。

**「社区讨论」** 有评论者认为，在 AI 时代扎实学习基础仍至关重要，否则会被 AI 取代；另有评论者指出，仅有讲座视频而缺少项目与反馈会削弱学习效果，期待后续课件上线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://www.youtube.com/CMUComputerScience">CMU Kenneth C. Griffin School of Computer Science - YouTube</a></li>

</ul>
</details>

**标签**: `#education`, `#computer science`, `#machine learning`, `#online learning`, `#open source`

---

<a id="item-tech-news-6"></a>
### [微软将邮件大规模中断归因于 7 月修复引入的软件缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将一次大规模电子邮件服务中断归因于 7 月发布的一项修复中引入的软件缺陷。对依赖微软电子邮件服务的用户和企业而言，这是一次显著的服务中断。报道指出，该事件凸显了云基础设施在快速修复与可靠性之间的挑战；具体受影响范围、版本号和服务恢复时间尚未在现有信息中披露。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「背景」** 微软在 7 月发布的一项软件修复中引入了缺陷，该缺陷随后在 11 月导致大规模邮件服务中断。微软现已将此次中断归因于该 7 月修复中的软件缺陷。

**「影响」** 此次故障导致全球 Outlook 用户无法访问电子邮件超过 12 小时，微软在周五早些时候仅报告“边际成功”；Outlook、Teams 和 Copilot 均受影响，甚至波及澳大利亚新南威尔士州的一个在线保释法庭。微软 365 服务已于 2026 年 11 月 14 日（周六）全面恢复，微软将根本原因归咎于 7 月一次修复中引入的软件缺陷。

**「社区讨论」** 评论中，有用户质疑 AI 在补丁编写与测试中的参与是否削弱了工程师对故障排查的深层技能；也有用户建议通过限制或轮换 IP 连接来降低负载，以便逐步恢复服务。另有用户将此类大规模故障类比为电力行业的黑启动，认为大型企业的大规模故障通常呈现类似模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook: Microsoft scrambles to fix email outage : NPR</a></li>
<li><a href="https://www.abc.net.au/news/2026-11-13/microsoft-outage-affects-users-worldwide/107381050">Microsoft outage hits users worldwide — as it happened</a></li>
<li><a href="https://abc7news.com/post/microsoft-outage-update-company-says-365-services-fully-restored-outlook-teams-ai-assistant-copilot-impacted/20039967/">Microsoft outage update: Company says Microsoft 365 services fully...</a></li>

</ul>
</details>

**标签**: `#cloud computing`, `#reliability`, `#Microsoft`, `#software defects`, `#outage`

---

<a id="item-tech-news-7"></a>
### [Marimba：基于冻结 Qwen3-ASR 的轻量语音问答系统](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 是一个基于冻结 Qwen3-ASR-0.6B 编码器的轻量语音问答系统，每 8 秒音频窗口只需一次编码器前向即可回答多种问题。它通过 ASR 假设的贪心和 4 束搜索解码结果进行零样本术语检测，并采用 Platt 校准输出概率；在 1000 个公开问题上，它在 9 项测试中的 6 项达到或超过 Qwen3-Omni（30B-A3B），但在 Speech Commands 上仍落后。作者指出，其轮次结束检测的读出层是在 Smart Turn 数据上训练的，因此该行结果仅对作者自身分布有效；论文为预印本，结果未经同行评审。代码、Apache-2.0 权重和演示已发布。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** 语音问答系统通常依赖大型全模态模型或针对特定任务的微调。Marimba 则复用冻结的 Qwen3-ASR-0.6B 编码器，通过对其解码器假设进行评分来实现零样本术语检测，并添加轻量级读出层来处理话轮结束和说话人变化任务。

**「影响」** 对开发者而言，Marimba 提供了低计算成本的语音问答方案：一次冻结编码器前向即可服务所有问题，且权重以 Apache-2.0 发布，可直接用于构建语音问答应用。但该模型在未见任务上不泛化——在 CochlScene 场景分类上所有头均为随机水平，且轮次结束检测在 Smart Turn 自身测试集上 AUROC 为 0.930，低于 Smart Turn v3.2 的 0.982，因此不应将其视为通用语音理解模型。

**标签**: `#speech recognition`, `#zero-shot`, `#efficient inference`, `#speech understanding`, `#preprint`

---

<a id="item-tech-news-8"></a>
### [谷歌拟向日本提供 Fairwind AI 模型用于网络防御](https://cn.nikkei.com/industry/itelectric-appliance/64742-2026-11-17-09-16-25.html) ⭐️ 7.0/10

谷歌计划将 9 月启动的 Fairwind 计划扩展至日本，向日本政府及重要基础设施运营商提供尖端 AI 模型用于网络防御。谷歌云 CEO Thomas Kurian 于 11 月 16 日访日，向日本政府高官表达这一意向。该计划此前主要面向美国政府机构和网络安全公司，此次扩展正值日本网络攻击损失急剧增加之际。

telegram · zaihuapd · 11月17日 03:43

**「背景」** 谷歌于 2026 年 9 月 2 日启动 Fairwind 计划，面向政府和企业合作伙伴提供自主网络防御工具，帮助其更快、更大规模地修复系统，以应对人工智能驱动的网络威胁。该计划此前主要面向美国政府机构和网络安全公司，此次拟扩展至日本政府及重要基础设施运营商。

**「影响」** 对日本政府及关键基础设施运营商而言，谷歌提供的 AI 模型将用于网络防御，而这一部署正值日本勒索软件攻击激增之际：2026 年上半年日本警方记录的勒索软件案件达 123 起，为系列统计中最高半年值（tool-3-3），且 2026 年初日本组织遭遇的勒索软件攻击同比增长 39%，高于全球 25%的增幅（tool-3-1）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/fairwind-program/">Fairwind Program — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/">Google ’s Fairwind Program : Cyber defense tools for trusted partners</a></li>
<li><a href="https://tmroreport.com/en/article/google-fairwind-program-proactive-cyber-defense">Google launches Fairwind Program for proactive cyber defense</a></li>
<li><a href="https://www.forescout.com/blog/japans-2026-cyber-threat-landscape-risks-threats-and-guidance/">Japan’s 2026 Cyber Threat Landscape: Risks, Threats, and Guidance</a></li>
<li><a href="https://www.mkultraman.com/blog/japan-cyberattacks-2026-data-breaches/">Japan Cyberattacks in 2026: Breach Record | MKUltraman</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#Google Cloud`, `#Japan`, `#cyber defense`

---

<a id="item-tech-news-9"></a>
### [加州起诉 OpenAI，指控其就 AI 安全误导公众](https://www.theregister.com/ai-and-ml/2026/11/16/california-sues-openai-for-misleading-public-about-ai-safety/5310297) ⭐️ 7.0/10

加州总检察长 Rob Bonta 以不公平竞争和妨害公共利益为由起诉 OpenAI，指控其在缺乏适当监管与安全措施的情况下测试有潜在危险的模型，并误导、危及公众。诉状援引 Hugging Face 基础设施被攻破事件，称同类事故已知达 80 起；Bonta 还表示 OpenAI 未实质配合 9 月发出的调查传票。OpenAI 未回应置评请求。

telegram · zaihuapd · 11月17日 06:00

**「背景」** 加州总检察长办公室于 9 月向 OpenAI 发出调查传票，要求其就 AI 安全相关事宜配合调查。此次诉讼指控 OpenAI 未实质配合该传票，并援引此前发生的 Hugging Face 基础设施被攻破事件（同类事故已知达 80 起）作为其安全措施不足的证据。

**「影响」** OpenAI 现需在加州法院应对该诉讼；其被指控未实质配合 9 月调查传票的行为已成为案件焦点之一，可能影响后续法律程序走向。

**标签**: `#AI safety`, `#regulation`, `#OpenAI`, `#legal`, `#California`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Nvidia CEO 黄仁勋辞职，AI 芯片股本周上涨](https://www.cnbc.com/2026/11/14/nvidia-ai-trade-data-centers-congress.html) ⭐️ 8.0/10

Nvidia 创始人兼 CEO 黄仁勋辞职后，公司股价本周收于 162.85 美元，Yorkville Ives 将目标价从 300 美元下调至 225 美元，但维持买入评级。

rss · CNBC Finance · 11月16日 12:13

**「背景」** 投资者担心 Nvidia 供应中断，AMD 和博通本周均上涨约 13%，纳斯达克指数创 8 月以来最佳周表现；Nvidia 临时 CEO Colette Kress 将于下周二财报中首次回应市场。

**「影响」** Yorkville Ives 估计，民主党控制国会可能导致 10%-20%计划中的数据中心不落地，但需求仍超供应四比一，现有算力价值可能上升。

**标签**: `#Nvidia`, `#AI trade`, `#CEO resignation`, `#ETFs`, `#data centers`

---

<a id="item-finance-news-2"></a>
### [坎托·菲茨杰拉德减持英伟达股份近 50%，引发利益冲突质疑](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

据 CNBC 对证券申报文件的分析，坎托·菲茨杰拉德（Cantor Fitzgerald）在 2025 年 9 月至 2026 年 3 月期间将其报告的英伟达（Nvidia）持股削减了 49%，市值从 6.52 亿美元降至 3.1 亿美元。这一减持发生在商务部长霍华德·卢特尼克面临处理涉嫌向中国走私英伟达芯片的压力的背景下。

rss · CNBC Finance · 11月16日 12:14

**「背景」** 该公司由卢特尼克的儿子布兰登和凯尔领导，此前卢特尼克曾多次抵制对新加坡公司 Megaspeed 的打击行动，该公司被怀疑将英伟达先进 AI 芯片转售给中国。英伟达 CEO 黄仁勋于周四辞职，引发对卢特尼克与该公司关系的进一步审视。

**「影响」** 前白宫伦理律师理查德·佩因特表示，虽然&quot;没有证据&quot;表明卢特尼克向坎托分享非公开信息，但&quot;外观看起来不太好&quot;；财政部长贝森特也指出，多个部门数月来一直支持将 Megaspeed 列入实体清单，暗示商务部内部流程存疑。

**标签**: `#Nvidia`, `#Cantor Fitzgerald`, `#Howard Lutnick`, `#ethics`, `#export controls`

---