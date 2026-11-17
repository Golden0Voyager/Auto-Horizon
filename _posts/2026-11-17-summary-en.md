---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 47 items, 11 important content pieces were selected

---

**Technology News**
1. [vLLM v0.34.0 adds 10 models, enables extensible KV cache by default](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely supply chain attack served malware on Zoom, GitLab](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0: A stable, opinionated Rust datetime library](#item-tech-news-3) ⭐️ 8.0/10
4. [Atlas meta-analysis of 126k ML papers: 26% of ablation changes unhelpful](#item-tech-news-4) ⭐️ 8.0/10
5. [Carnegie Mellon releases free CS course lectures on YouTube](#item-tech-news-5) ⭐️ 7.0/10
6. [Microsoft blames email outage on July fix defect](#item-tech-news-6) ⭐️ 7.0/10
7. [Marimba: Lightweight Speech QA on Frozen Qwen3-ASR](#item-tech-news-7) ⭐️ 7.0/10
8. [Google to extend Fairwind AI cyber defense program to Japan](#item-tech-news-8) ⭐️ 7.0/10
9. [California sues OpenAI over alleged AI safety misrepresentation](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Nvidia CEO resigns; other AI chipmakers gain as trade reshuffles](#item-finance-news-1) ⭐️ 8.0/10
2. [Cantor Fitzgerald cut Nvidia stake by nearly 50% amid chip-export scrutiny](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 adds 10 models, enables extensible KV cache by default](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 is now available, adding 10 new model architectures including Mistral Large 4, MiniMax-M3.1-Flash, and NVIDIA Nemotron-3.5-Transcribe, and enabling the extensible KV cache by default so the cache is sized from memory actually free after warmup rather than an estimate. The release removes Model Runner V1, making V2 the only GPU runner, and delivers measured speedups of up to 1.95× decode on 4×GB200 for Step5 NVFP4 MoE and 1.6× output throughput for GLM-5.3-Flash. Upgrading requires attention: the default block size is now 64 instead of 16, ROCm 7.2 images are no longer published, and huggingface\_hub &gt;= 2.0.0 is required. The extensible KV cache can raise per-token decode latency by 6–18% on some H200 models at concurrency 128, which users can opt out of with --gpu-memory-utilization 0.9 or --no-enable-extensible-kv-cache.

github · khluu · Nov 16, 23:22

**「Background」** vLLM is an open-source LLM inference engine that serves models through an OpenAI-compatible API. Its KV cache stores attention keys and values to avoid recomputation, and its size directly limits how many concurrent requests can be served. Model Runner V1 and V2 are two GPU execution paths; V2 added dual-batch overlap and was previously opt-in via VLLM\_USE\_V2\_MODEL\_RUNNER.

**「Impact」** Existing deployments must review the breaking changes before upgrading: setting VLLM\_USE\_V2\_MODEL\_RUNNER=0 now fails at startup, fp\_quant checkpoints no longer load, and Marlin W4A8 users must switch to --quantization humming with VLLM\_HUMMING\_INPUT\_QUANT\_CONFIG. Operators who want the previous KV cache sizing or block size must pass --gpu-memory-utilization 0.9 or --no-enable-extensible-kv-cache and --block-size 16 respectively.

**Tags**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#GPU`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Optimizely supply chain attack served malware on Zoom, GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely, a widely used third-party script provider, was compromised in a supply chain attack that served malware to visitors of major websites including Zoom and GitLab. The incident highlights the security risks of relying on third-party JavaScript and underscores the need for stronger web security measures such as Subresource Integrity.

hackernews · kristjansson · Nov 16, 23:00 · [Discussion](https://news.ycombinator.com/item?id=50524767)

**「Background」** Optimizely is a widely used A/B testing and personalization platform whose JavaScript snippet is embedded in many high-traffic websites, including Zoom, BBC, CNN, and GitLab. Because these third-party scripts execute with the same privileges as the host page, a compromise of the vendor&\#x27;s script delivery can propagate to every downstream site that loads it; the affected snippets were served from Optimizely&\#x27;s own CDN, not the result of a cache-poisoning attack.

**「Impact」** The incident reinforces the need for sites using third-party scripts to implement Subresource Integrity \(SRI\) and consider vendoring critical scripts, as the compromise of a single vendor can expose millions of users to malware.

**「Community Discussion」** Commenters argued that the attack was avoidable: one noted that Subresource Integrity has been available for over a decade and should now be implemented with these services, while another called for accountability and suggested that major sites should vendor critical scripts rather than serve them from third parties.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50524767">Optimizely compromised , served malware on Zoom , GitLab</a></li>
<li><a href="https://gizmodo.com/sprawling-malware-attack-reportedly-affects-zoom-cnn-fox-news-peacock-and-170-others-2000840831">Sprawling Malware Attack Reportedly Affects Zoom and Other Major...</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#third-party scripts`, `#web security`, `#subresource integrity`, `#malware`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0: A stable, opinionated Rust datetime library](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0, a new stable Rust datetime library by burntsushi, is now available, offering a modern, opinionated alternative to chrono. The release provides a stable API for date and time handling, with a design that explicitly acknowledges it is not the right tool for every use case. It has received strong community support, including positive feedback from a former chrono maintainer.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**「Background」** chrono has long been the de facto standard datetime library in Rust, but its API stability has made improvements difficult, as a former maintainer noted. Jiff 1.0 is a new stable library that offers a modern, opinionated alternative.

**「Impact」** Jiff 1.0 gives Rust developers a stable, opinionated datetime API that addresses the design constraints that led a former chrono maintainer to step down, offering a modern alternative for projects that have outgrown chrono&\#x27;s frozen interface. However, as the project itself notes, Jiff is not the right tool for every use case, so teams should evaluate it against their specific time-handling needs.

**「Community Discussion」** A former chrono maintainer, quodlibetor, said he took on maintenance because the API &\#x27;sucked&\#x27; and he hoped to improve it, but found that users valued stability and resisted changes, leading to burnout and his departure; he expressed gratitude to burntsushi for writing Jiff. Another commenter appreciated that Jiff&\#x27;s documentation calmly acknowledges it is not the right tool for every use case.

**Tags**: `#Rust`, `#datetime`, `#library`, `#chrono`, `#time handling`

---

<a id="item-tech-news-4"></a>
### [Atlas meta-analysis of 126k ML papers: 26% of ablation changes unhelpful](https://www.reddit.com/r/MachineLearning/comments/1xybvju/we_logged_621k_changes_from_127k_papers_ablations/) ⭐️ 8.0/10

A meta-analysis of 126,758 full-text machine learning papers \(ICML, NeurIPS, ICLR, CVPR, AAAI, ICCV, ECCV, TPAMI, IJCV, JMLR, 2016–2026\) extracted 621,064 ablation changes from 110,393 papers and found that 69% helped, 10% had no clear effect, and 16% made results worse, meaning 26% of changes did not help by the papers&\#x27; own reported numbers. 66% of papers reported at least one change that did not help. Among common changes, higher sampling temperature was unhelpful in 52% of 122 papers, larger LoRA rank in 46%, and larger learning rate in 46%, while adding a contrastive loss was unhelpful in only 4% of 1,317 papers. The results come from Latentic Labs&\#x27; Atlas, with the front page and &\#x27;usual suspects&\#x27; table publicly available at atlas.scime.ai/what-didnt-work-2026.

reddit · r/MachineLearning · /u/latenticlabs · Nov 17, 05:11

**「Background」** The Scime Atlas project, which this post follows up on, systematically catalogs reported results from machine learning papers. This analysis extends that effort by focusing on changes that did not help by the papers&\#x27; own numbers.

**「Impact」** For researchers and practitioners, the analysis implies that common tuning choices such as higher sampling temperature, larger LoRA rank, or larger learning rate frequently fail to improve results by the papers&\#x27; own reported numbers, so these changes should not be assumed beneficial without checking the public Atlas table at atlas.scime.ai/what-didnt-work-2026.

**Tags**: `#machine learning`, `#ablation studies`, `#research methodology`, `#meta-analysis`, `#reproducibility`

---

<a id="item-tech-news-5"></a>
### [Carnegie Mellon releases free CS course lectures on YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

Carnegie Mellon has launched CS Learn, releasing full-semester lecture videos from current computer science courses free on YouTube, with one course premiering each day this week and more courses in January. The initial lineup includes Tianqi Chen&\#x27;s ML Systems and 15-259 Probability and Computing. Student-built tools automate much of the production work, allowing a small team to produce the content.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**「Background」** Carnegie Mellon&\#x27;s School of Computer Science has maintained a YouTube channel for public lectures and outreach \(tool-1-2\); the new CS Learn channel \(tool-1-1\) builds on that by publishing complete semester-length course playlists.

**「Impact」** For learners, this provides free access to current CMU course content without tuition, but the initial release is lectures only; a commenter notes that without projects and feedback, lectures can fall flat, and courseware is expected next.

**「Community discussion」** Commenters welcomed the release, with one arguing that learning fundamentals properly makes AI a power tool rather than a replacement, while another cautioned that lectures without projects and feedback can fall flat and asked for courseware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://www.youtube.com/CMUComputerScience">CMU Kenneth C. Griffin School of Computer Science - YouTube</a></li>

</ul>
</details>

**Tags**: `#education`, `#computer science`, `#machine learning`, `#online learning`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Microsoft blames email outage on July fix defect](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft has attributed a major email outage to a software defect introduced in a July fix, according to the company&\#x27;s root-cause explanation. The defect reportedly caused the service to fail under normal load, complicating recovery. The incident highlights reliability challenges in cloud infrastructure, though specific affected services and outage scale were not detailed in the available report.

hackernews · Bender · Nov 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50517321)

**「Background」** Microsoft has traced a major email outage to a software defect that was introduced by a fix deployed in July. The company&\#x27;s explanation frames the outage as a follow-on failure of that earlier change, not a new external cause.

**「Impact on Microsoft 365 customers」** For Microsoft 365 customers, the outage disrupted Outlook, Teams, and Copilot across two workdays, with Microsoft apologizing after services were fully restored; the company attributed the failure to a software defect introduced in a July fix, and the incident also affected an online bail court in New South Wales, showing that even routine patches can cause cascading failures in cloud infrastructure.

**「Community Discussion」** Commenters debated the recovery strategy, with one comparing the restart to a power grid &quot;black start&quot; and another questioning whether AI-assisted development contributed to the defect and slow recovery. Another suggested load-shedding as a mitigation, while one expressed surprise that Windows is used for critical network infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook: Microsoft scrambles to fix email outage : NPR</a></li>
<li><a href="https://www.abc.net.au/news/2026-11-13/microsoft-outage-affects-users-worldwide/107381050">Microsoft outage hits users worldwide — as it happened</a></li>
<li><a href="https://abc7news.com/post/microsoft-outage-update-company-says-365-services-fully-restored-outlook-teams-ai-assistant-copilot-impacted/20039967/">Microsoft outage update: Company says Microsoft 365 services fully...</a></li>

</ul>
</details>

**Tags**: `#cloud computing`, `#reliability`, `#Microsoft`, `#software defects`, `#outage`

---

<a id="item-tech-news-7"></a>
### [Marimba: Lightweight Speech QA on Frozen Qwen3-ASR](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

A preprint describes Marimba, a lightweight speech question-answering system that runs one frozen Qwen3-ASR-0.6B encoder pass per 8-second audio window and returns calibrated probabilities for typed yes/no, choice, or score questions. The authors report it matches or beats Qwen3-Omni \(30B-A3B\) on 6 of 9 public-question tests, with 100% language ID on 300 FLEURS clips and speaker-change AUROC of 0.966-0.980 on AMI and VoxConverse, but the results are self-reported and not peer-reviewed. The turn-end readout was trained on Smart Turn data, so that comparison is in-distribution for Marimba only, and the system fails on unseen CochlScene scene classification.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Background」** This preprint is the follow-up to an earlier post that introduced the Marimba approach without the paper; the new release adds the arXiv paper, code, weights, and a demo. The approach builds on a frozen Qwen3-ASR-0.6B encoder, using its decoder hypotheses for zero-shot term spotting and intermediate-layer readouts for turn-end, speaker change, and speaker count tasks.

**「Impact」** Developers can try Marimba today via the Apache-2.0 weights on Hugging Face, the demo space, or \`pip install marimba-audio\`, but the preprint&\#x27;s turn-end and generalization caveats mean it should be validated on out-of-distribution data before replacing dedicated turn-end or keyword-spotting models.

**Tags**: `#speech recognition`, `#zero-shot`, `#efficient inference`, `#speech understanding`, `#preprint`

---

<a id="item-tech-news-8"></a>
### [Google to extend Fairwind AI cyber defense program to Japan](https://cn.nikkei.com/industry/itelectric-appliance/64742-2026-11-17-09-16-25.html) ⭐️ 7.0/10

Google Cloud plans to extend its Fairwind program to Japan, offering advanced AI models to the Japanese government and critical infrastructure operators for cyber defense. CEO Thomas Kurian expressed the intention during a November 16 visit to Tokyo, according to Nikkei. The program, launched in September, previously served only US government agencies and cybersecurity companies; the Japan expansion is a plan, not yet a shipped capability, and responds to Japan&\#x27;s sharp increase in cyber attack losses.

telegram · zaihuapd · Nov 17, 03:43

**「Background」** Google launched the Fairwind Program on September 2, 2026, as a proactive cyber-defense initiative for governments and enterprises, providing trusted partners with autonomous tools to repair systems faster and stay ahead of agentic-speed threats. The program initially targeted US government agencies and cybersecurity companies; the reported Japan expansion would extend it to a new government and critical-infrastructure audience.

**「Impact on Japan&\#x27;s cyber defense」** Google&\#x27;s announced plan to extend its Fairwind program to Japan would give the Japanese government and critical infrastructure operators access to advanced AI models for cyber defense, a capability that arrives as ransomware attacks against Japanese organizations rose 39% year-over-year in early 2026 and Japan logged 123 ransomware cases in the first eight months of 2026, with 82.8% of confirmed ransom demands involving double extortion and manufacturing hardest hit. The program, previously focused on US government agencies and cybersecurity companies, would now extend to a foreign government, raising questions about data sovereignty and reliance on a US vendor for national security.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/">Google ’s Fairwind Program : Cyber defense tools for trusted partners</a></li>
<li><a href="https://tmroreport.com/en/article/google-fairwind-program-proactive-cyber-defense">Google launches Fairwind Program for proactive cyber defense</a></li>
<li><a href="https://www.forescout.com/blog/japans-2026-cyber-threat-landscape-risks-threats-and-guidance/">Japan’s 2026 Cyber Threat Landscape: Risks, Threats, and Guidance</a></li>
<li><a href="https://www.cybersecurity-insiders.com/why-is-japan-seeing-an-extreme-surge-in-ransomware-cases/">Japan Logs 123 Ransomware Cases in Eight Months of 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#Google Cloud`, `#Japan`, `#cyber defense`

---

<a id="item-tech-news-9"></a>
### [California sues OpenAI over alleged AI safety misrepresentation](https://www.theregister.com/ai-and-ml/2026/11/16/california-sues-openai-for-misleading-public-about-ai-safety/5310297) ⭐️ 7.0/10

California Attorney General Rob Bonta has sued OpenAI, alleging unfair competition and public nuisance for testing potentially dangerous models without adequate regulation or safety measures and for misleading the public. The complaint cites the Hugging Face infrastructure breach and says 80 similar incidents are known, and Bonta says OpenAI did not substantively cooperate with a September investigative subpoena. OpenAI did not respond to a request for comment. The allegations are unproven.

telegram · zaihuapd · Nov 17, 06:00

**「Background」** The lawsuit follows a September investigative subpoena that California Attorney General Rob Bonta says OpenAI did not substantively cooperate with, and it cites the Hugging Face infrastructure breach as one of 80 similar incidents. Under California law, the attorney general can bring unfair competition and public nuisance claims against companies that allegedly mislead the public.

**「Impact」** For OpenAI, the lawsuit creates a concrete legal obligation to respond in court to California&\#x27;s allegations and to the September subpoena, and could result in injunctive relief or penalties if the claims are proven.

**Tags**: `#AI safety`, `#regulation`, `#OpenAI`, `#legal`, `#California`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia CEO resigns; other AI chipmakers gain as trade reshuffles](https://www.cnbc.com/2026/11/14/nvidia-ai-trade-data-centers-congress.html) ⭐️ 8.0/10

Nvidia CEO Jensen Huang resigned after a week of turmoil, sending the stock to $162.85 and prompting Yorkville Ives to cut its price target to $225 from $300, while AMD and Broadcom each gained about 13%.

rss · CNBC Finance · Nov 16, 12:13

**「Background」** The resignation follows Nvidia&\#x27;s longest losing streak since 2012; interim CEO and CFO Colette Kress will face investors at third-quarter earnings next Tuesday.

**「Impact」** A Democratic-controlled Congress could slow data-center buildout, with Dan Ives estimating 10% to 20% of planned projects may not materialize, though demand still outstrips supply four to one; experts say this could make existing compute more valuable and benefit Big Tech.

**Tags**: `#Nvidia`, `#AI trade`, `#CEO resignation`, `#ETFs`, `#data centers`

---

<a id="item-finance-news-2"></a>
### [Cantor Fitzgerald cut Nvidia stake by nearly 50% amid chip-export scrutiny](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

Cantor Fitzgerald cut its reported Nvidia stake by nearly 50% between September 2025 and March 2026, from 3.5 million shares worth $652 million to 1.78 million shares worth $310 million, according to a CNBC analysis of securities filings.

rss · CNBC Finance · Nov 16, 12:14

**「Background」** The firm, formerly run by Commerce Secretary Howard Lutnick and now led by his sons, had Nvidia as one of its largest reported stock positions; the cut came as U.S. officials pressed Lutnick to crack down on a Singapore company suspected of funneling Nvidia AI chips to China.

**Tags**: `#Nvidia`, `#Cantor Fitzgerald`, `#Howard Lutnick`, `#ethics`, `#export controls`

---