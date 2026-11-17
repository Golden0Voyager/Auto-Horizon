---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 47 items, 14 important content pieces were selected

---

**Technology News**
1. [vLLM v0.34.0 adds 10 models, enables extensible KV cache by default](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely supply-chain compromise served malware to Zoom and GitLab](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0: A new datetime library for Rust](#item-tech-news-3) ⭐️ 8.0/10
4. [Meta-analysis of 621k ML changes finds 31% null or negative in ML venues](#item-tech-news-4) ⭐️ 8.0/10
5. [Shandong University team claims first conditional proof of binary Goldbach conjecture](#item-tech-news-5) ⭐️ 8.0/10
6. [Alibaba, Tencent, Moonshot Limit Cyber Capabilities in New AI Models](#item-tech-news-6) ⭐️ 8.0/10
7. [Carnegie Mellon releases free CS course lectures on YouTube](#item-tech-news-7) ⭐️ 7.0/10
8. [Microsoft blames email outage on defect from July fix](#item-tech-news-8) ⭐️ 7.0/10
9. [Marimba: Frozen 0.6B ASR Encoder with Readouts Answers Audio Queries](#item-tech-news-9) ⭐️ 7.0/10
10. [US Commerce, DOJ clarify Megaspeed export-control and criminal probe timeline](#item-tech-news-10) ⭐️ 7.0/10
11. [California sues OpenAI over AI safety misrepresentation](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [Nvidia board not considering Huang&\#x27;s return, investigating his conduct: report](#item-finance-news-1) ⭐️ 8.0/10
2. [Berkshire raises Delta stake, trims Bank of America in Q3](#item-finance-news-2) ⭐️ 7.0/10
3. [U.S. crude oil falls to $85.39 as Middle East exports recover](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 adds 10 models, enables extensible KV cache by default](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 ships 10 new model architectures, including Mistral Large 4, MiniMax-M3.1-Flash, and Nemotron-3.5-Transcribe, and enables extensible KV cache by default, sizing the cache from memory free after warmup. Model Runner V1 is removed, making V2 the only GPU runner, and the default block size changes from 16 to 64. Breaking changes for production users include dropped ROCm 7.2 artifacts, a new requirement for huggingface\_hub &gt;= 2.0.0, and removal of QuTLASS/fp\_quant and Marlin W4A8. vLLM reports up to 1.95× decode on 4×GB200 and 1.6× output throughput on NVIDIA hardware, though these are vendor benchmarks on specific hardware.

github · khluu · Nov 16, 23:22

**「Background」** vLLM&\#x27;s Model Runner V2 was previously an opt-in alternative to the default Model Runner V1, and the KV cache was sized from an estimated memory figure rather than measured free memory after warmup. This release makes V2 the sole GPU runner and switches the KV cache to post-warmup sizing, while also raising the default block size from 16 to 64.

**「Impact」** Production users upgrading must remove VLLM\_USE\_V2\_MODEL\_RUNNER=0, pass --block-size 16 to preserve old behavior, and move to ROCm 10.0 wheels, since ROCm 7.2 images are no longer published.

**Tags**: `#vllm`, `#llm-inference`, `#performance`, `#open-source`, `#gpu-computing`

---

<a id="item-tech-news-2"></a>
### [Optimizely supply-chain compromise served malware to Zoom and GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely, a widely used A/B testing platform, was compromised and served malware to visitors of major websites, including Zoom and GitLab, according to a Report URI blog post. The incident highlights the risk of third-party JavaScript loaded from vendor domains, where a single compromised vendor can affect many sites at once. The report does not specify the exact malware payload or the number of affected sites, but the named victims show the reach of the supply-chain compromise.

hackernews · kristjansson · Nov 16, 23:00 · [Discussion](https://news.ycombinator.com/item?id=50524767)

**「Background」** Optimizely is a widely used A/B testing platform that injects third-party JavaScript into client websites. This incident highlights the inherent risk of relying on third-party scripts and the importance of Subresource Integrity \(SRI\) to verify the integrity of external resources.

**「Impact on affected sites」** The malicious JavaScript injected into Optimizely Web reached visitors of 178 organizations&\#x27; sites on 16 November, including Zoom, BBC, CNN, Salesforce, GitLab, IKEA, HSBC, Equifax, and Air France; affected organizations should audit their sites for the injected script and review how third-party scripts are loaded.

**「Community Discussion」** Commenters argued that the incident is avoidable with existing defenses: jdorfman noted that Subresource Integrity has been available for over a decade and should now be implemented with these services, while mcoliver called for vendor-side controls such as internal cooldowns, phased rollouts, and automatic security checks, and suggested that large sites should vendor the scripts rather than serve them from third-party domains. stickfigure added that the Google Tag Manager model, which lets marketing add tags without engineering, is what led to heavy third-party JavaScript in the first place.

<details><summary>References</summary>
<ul>
<li><a href="https://shiftdelete.net/en/optimizely-malware">Optimizely Malware Hit 178 Sites: What It Stole and What to Do</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/optimizely-supply-chain-attack-delivers-malware-to-cnn-fox-news-bbc-salesforce-sites/">Optimizely supply chain attack infects major brands&#x27; sites ...</a></li>
<li><a href="https://cybersecuritynews.com/optimizely-websites-hijacked/">Hackers Infect 178 Major Websites via Optimizely to Steal ...</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#third-party scripts`, `#web security`, `#malware`, `#Optimizely`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0: A new datetime library for Rust](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0, a new datetime library for Rust by burntsushi, has been released with a detailed design document. The library offers an alternative to existing crates like chrono and time, with a focus on ergonomics and correctness, though the author notes it is not the right tool for every use case.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**「Rust&\#x27;s datetime ecosystem and chrono&\#x27;s legacy」** Rust&\#x27;s datetime ecosystem has long centered on chrono, whose stable API was both its main draw and a source of friction: a former chrono maintainer reported that every attempt at improvement met resistance, contributing to maintenance burnout. Jiff, by burntsushi \(Andrew Gallant\), is a new datetime library designed as an opinionated alternative to chrono, with a design document that explicitly acknowledges it is not the right tool for every use case.

**「Impact」** For Rust developers, Jiff 1.0 provides a maintained, actively developed alternative to chrono and time, with high-level datetime primitives designed to be difficult to misuse and to have reasonable performance. However, the project&\#x27;s own design documentation notes that Jiff is not always the right tool for every use case, so teams should evaluate migration against their specific requirements before adopting it.

**「Community Discussion」** A former chrono maintainer explains that they took on maintenance hoping to improve the API but faced resistance from users who valued stability, and expresses gratitude to burntsushi for writing Jiff. Another commenter appreciates the project&\#x27;s candid acknowledgment that it is not the right tool for every use case.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.rs/jiff/latest/jiff/">jiff - Rust - Docs.rs</a></li>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/_documentation/design/index.html">jiff::_documentation::design - Rust - Docs.rs</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#datetime`, `#library`, `#open source`, `#software engineering`

---

<a id="item-tech-news-4"></a>
### [Meta-analysis of 621k ML changes finds 31% null or negative in ML venues](https://www.reddit.com/r/MachineLearning/comments/1xybvju/we_logged_621k_changes_from_127k_papers_ablations/) ⭐️ 8.0/10

A meta-analysis of 126,758 machine learning papers \(2016–2026\) extracted 621,064 reported changes and found 69% helped, 10% had no clear effect, 16% were worse, and 5% were mixed. Across ML venues, 31% of changes reported null or negative results, versus 22% in vision venues, and 66% of papers included at least one change that did not help. Among common practices, higher sampling temperature \(52% of 122 papers\), larger LoRA rank \(46%\), and larger learning rate \(46%\) were most often unhelpful, while adding a contrastive loss was least \(4% of 1,317\). The analysis is self-reported by Latentic Labs and not peer-reviewed, but the methodology and public dataset are transparent.

reddit · r/MachineLearning · /u/latenticlabs · Nov 17, 05:11

**「Background」** This analysis follows up on the Scime Atlas posts from earlier this month. The prerequisite concept is that machine learning papers report individual changes—such as adding a layer, a loss, or a larger learning rate—along with the effect they measured; this work aggregates those reported changes across 126,758 papers to quantify how often common practices fail.

**「Impact」** For practitioners, the results suggest that common hyperparameter increases—sampling temperature, LoRA rank, and learning rate—frequently fail to improve performance, so these changes should be validated on a case-by-case basis rather than assumed beneficial. The public dataset at atlas.scime.ai allows further investigation.

**Tags**: `#machine learning`, `#meta-analysis`, `#ablation studies`, `#research methodology`, `#reproducibility`

---

<a id="item-tech-news-5"></a>
### [Shandong University team claims first conditional proof of binary Goldbach conjecture](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 8.0/10

Shandong University mathematicians Li Jiamin and Liu Jianya claim the first conditional proof of the binary Goldbach conjecture for all sufficiently large even numbers, assuming the Generalized Riemann Hypothesis for Dirichlet L-functions plus one of two additional spectral hypotheses. Under those assumptions, every sufficiently large even number is the sum of two primes, with both primes lying between one-third and two-thirds of the even number. The result is conditional, not unconditional, and the Generalized Riemann Hypothesis alone is not enough; the method differs from classical sieve and circle methods. The claim is reported in a university announcement and has not been independently verified.

telegram · zaihuapd · Nov 16, 16:01

**「Background」** The binary Goldbach conjecture states that every even integer greater than 2 can be written as the sum of two primes, and classical attempts to prove it have relied on sieve methods and the circle method. The new work instead claims a conditional proof for all sufficiently large even numbers, assuming the generalized Riemann hypothesis for Dirichlet L-functions together with one of two additional spectral hypotheses, and the authors state that their approach is fundamentally different from the classical sieve and circle methods.

**「Impact」** For number theorists, the result offers a new conditional route to Goldbach but does not resolve the conjecture unconditionally; the two extra spectral hypotheses and lack of independent verification mean the proof must be checked before it can be relied upon.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.05224">[2606.05224] Theorem $ (1+1.9)$ on the Goldbach Conjecture</a></li>
<li><a href="https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf">A CONDITIONAL PROOF OF THE GOLDBACH CONJECTURE</a></li>

</ul>
</details>

**Tags**: `#number theory`, `#Goldbach conjecture`, `#Riemann hypothesis`, `#mathematics`, `#research`

---

<a id="item-tech-news-6"></a>
### [Alibaba, Tencent, Moonshot Limit Cyber Capabilities in New AI Models](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 8.0/10

Chinese AI leaders including Alibaba, Tencent, and Moonshot AI have reduced offensive cyber capabilities in their latest models while improving defensive performance. Alibaba&\#x27;s newest flagship Qwen model has withheld its open weights, preventing users from downloading and customizing the full version. This follows the Ministry of Commerce&\#x27;s draft export control rules announced last month, which would prohibit exporting AI tools capable of attacking critical infrastructure or government networks. Tencent also reduced network capabilities in its Hy4 model released this month.

telegram · zaihuapd · Nov 17, 02:20

**「Regulatory backdrop」** China&\#x27;s Ministry of Commerce published an export control draft last month that would prohibit the export of AI tools capable of attacking critical infrastructure or government networks. This regulatory proposal is the backdrop for the decisions by Alibaba, Tencent, and Moonshot to reduce offensive cyber capabilities in their latest models.

**「Impact」** Developers and enterprises that rely on Alibaba&\#x27;s Qwen open-weight models face a concrete change: the latest flagship release withheld open weights, so users can no longer download and customize the full version.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models">China’s Top AI Firms Limit Cyber Capabilities in Latest ...</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#export controls`, `#open-source AI`, `#cybersecurity`, `#Chinese AI`

---

<a id="item-tech-news-7"></a>
### [Carnegie Mellon releases free CS course lectures on YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

Carnegie Mellon&\#x27;s Griffin School of Computer Science launched CS Learn, publishing full-semester lecture videos from current courses on YouTube for free, with one course premiering each day this week and more scheduled for January. The initial lineup includes Tianqi Chen&\#x27;s Machine Learning Systems and 15-259 Probability and Computing. Student-built tools automate much of the production work, letting a small team publish the lectures.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**「Context」** Open courseware has a long precedent: the launch author notes MIT began publishing course materials online about 25 years ago. CMU&\#x27;s version differs by releasing full lecture videos from currently-running courses rather than static materials, and by using student-built automation to cut production overhead.

**「Impact」** For self-learners, the release offers free access to current top-tier CS instruction, though the author says courseware \(slides, projects, and feedback\) is coming next; commenters caution that lectures without projects and feedback can fall flat.

**「Community discussion」** One commenter argued that learning fundamentals properly turns AI into a power tool, while skipping them risks replacement, framing the courses&\#x27; value in the AI era. Another welcomed the promised courseware, noting lectures alone can fall flat without projects and feedback.

**Tags**: `#computer science education`, `#free courses`, `#Carnegie Mellon`, `#machine learning systems`, `#online learning`

---

<a id="item-tech-news-8"></a>
### [Microsoft blames email outage on defect from July fix](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft has attributed a major email outage to a software defect introduced in a July fix, according to The Register. The defect is a regression from the earlier fix and affected Microsoft email users. The incident has sparked technical discussion about recovery and operational practices.

hackernews · Bender · Nov 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50517321)

**「Background」** Microsoft&\#x27;s email outage began on Thursday, November 12, when millions of Outlook users lost access; after more than 12 hours, Microsoft reported only &quot;marginal success&quot; in restoring service. The company has now traced the incident to a software defect introduced in a July fix, which caused its servers to become overwhelmed and unresponsive.

**「Community Discussion」** In the Hacker News discussion, commenters debated recovery tactics, with one drawing an analogy to power grid black starts and another suggesting Microsoft could have limited connections to reduce load. Another commenter questioned whether AI-assisted patching contributed to the defect and slower recovery.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/16/microsoft-global-outage-cause">Microsoft identifies months-old bug as a root cause of global outage</a></li>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook: Microsoft scrambles to fix email outage : NPR</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#email outage`, `#software defect`, `#reliability`, `#root cause analysis`

---

<a id="item-tech-news-9"></a>
### [Marimba: Frozen 0.6B ASR Encoder with Readouts Answers Audio Queries](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

A frozen 0.6B Qwen3-ASR encoder with lightweight readouts answers typed questions about audio windows, returning calibrated probabilities for term spotting, language ID, turn-end, speaker change, and speaker count. On 1,000 public questions, it matches or beats Qwen3-Omni \(30B-A3B\) on 6 of 9 tests, though Qwen3-Omni remains better on Speech Commands. The turn-end readout was trained on Smart Turn data, so that result is in-distribution for Marimba only, and all heads perform at chance on CochlScene scene classification, showing no generalization to unseen tasks.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Background」** The paper is a follow-up to a previously posted approach, now formalizing a frozen Qwen3-ASR-0.6B encoder as a general-purpose audio feature extractor for zero-shot queries.

**「Impact」** For developers, the released Apache-2.0 weights and pip package \(marimba-audio\) enable efficient zero-shot audio queries with a 0.6B encoder, but the chance-level performance on CochlScene means it is not a drop-in replacement for dedicated models on unseen tasks.

**Tags**: `#speech understanding`, `#efficient models`, `#ASR`, `#zero-shot`, `#audio`

---

<a id="item-tech-news-10"></a>
### [US Commerce, DOJ clarify Megaspeed export-control and criminal probe timeline](https://www.commerce.gov/sites/default/files/2026-11/DOC-DOJ-Joint-Statement.pdf) ⭐️ 7.0/10

On November 16, 2026, the US Commerce Department and Department of Justice issued a joint statement clarifying the timeline of the export-control and criminal investigation into Singapore-based Megaspeed, saying it was meant to rebut inaccurate reports from the past week. The statement says Commerce opened a case against Megaspeed in 2024, requested Nvidia&\#x27;s sales records in May 2025, and that Nvidia placed Megaspeed on a no-sale list in June 2025. It also says the Bureau of Industry and Security conducted on-site verification with Singapore authorities and interviewed Megaspeed&\#x27;s CEO, and that the case has been transferred to the DOJ for criminal investigation.

telegram · zaihuapd · Nov 17, 05:00

**「Earlier developments」** The US Commerce Department&\#x27;s Bureau of Industry and Security opened an export control case against Singapore-based Megaspeed in 2024. In May 2025, the department requested sales records from Nvidia, and in June 2025 Nvidia placed Megaspeed on its restricted sales list, after which BIS conducted on-site verification with Singapore authorities and interviewed Megaspeed&\#x27;s CEO.

**「Impact」** For Nvidia and AI hardware supply-chain participants, the joint statement confirms that the Megaspeed matter is now a DOJ-led criminal investigation and that Nvidia&\#x27;s June 2025 no-sale listing remains part of the record.

**Tags**: `#export controls`, `#semiconductors`, `#Nvidia`, `#government investigation`, `#AI hardware`

---

<a id="item-tech-news-11"></a>
### [California sues OpenAI over AI safety misrepresentation](https://www.theregister.com/ai-and-ml/2026/11/16/california-sues-openai-for-misleading-public-about-ai-safety/5310297) ⭐️ 7.0/10

California Attorney General Rob Bonta has sued OpenAI, alleging the company engaged in unfair competition and harmed the public interest by testing potentially dangerous AI models without adequate regulation or safety measures. The complaint cites the Hugging Face infrastructure breach and says 80 similar incidents are known, and alleges OpenAI failed to substantially cooperate with a subpoena issued in September. OpenAI did not respond to a request for comment.

telegram · zaihuapd · Nov 17, 06:00

**「Background」** California Attorney General Rob Bonta issued a subpoena to OpenAI in September 2026 as part of an investigation into its AI safety practices, and the new lawsuit alleges that OpenAI did not substantially cooperate with that inquiry. The complaint cites a breach of Hugging Face&\#x27;s infrastructure as an example of the kind of incident it says has occurred 80 times.

**「Legal exposure for OpenAI」** California&\#x27;s suit could lead to court-ordered injunctions or penalties under the state&\#x27;s unfair competition law, and it may become the first major test of California&\#x27;s new framework for independent AI safety auditors, established through more than two dozen AI-related bills. The case also adds to legal pressure on OpenAI over the July 2026 Hugging Face breach, which a separate nonprofit lawsuit also challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://www.latimes.com/california/story/2026-11-16/california-sues-openai-alleging-it-endangered-public-by-developing-ai-without-safeguards">California sues OpenAI , alleges it endangered the public by building...</a></li>
<li><a href="https://www.bbc.com/news/articles/c6wy4xv2mxglo">California sues OpenAI over Hugging Face attack</a></li>
<li><a href="https://www.wired.com/story/openai-sued-over-the-hugging-face-hack/">OpenAI Gets Sued Over the Hugging Face Hack | WIRED</a></li>

</ul>
</details>

**Tags**: `#legal`, `#AI safety`, `#OpenAI`, `#regulation`, `#California`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia board not considering Huang&\#x27;s return, investigating his conduct: report](https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html) ⭐️ 8.0/10

Nvidia&\#x27;s board is not considering reinstating Jensen Huang as CEO and is instead investigating his conduct over potential national security and company-secret risks, people familiar with the matter told CNBC. The board has hired law firm Wachtell Lipton to review the matter.

telegram · zaihuapd · Nov 17, 01:39

**「Background」** Huang resigned as CEO last week amid scrutiny of his ties to a suspected Chinese spy and of chip exports to China; CFO Colette Kress is serving as interim CEO.

**「Impact」** The investigation adds uncertainty for Nvidia investors, who have already seen the stock fall after Huang&\#x27;s exit; Kress is set to report third-quarter earnings next Tuesday.

**Tags**: `#Nvidia`, `#corporate governance`, `#CEO investigation`, `#national security`, `#semiconductors`

---

<a id="item-finance-news-2"></a>
### [Berkshire raises Delta stake, trims Bank of America in Q3](https://www.cnbc.com/2026/11/16/berkshire-hathaway-raised-its-stake-in-delta-air-in-the-third-quarter.html) ⭐️ 7.0/10

Berkshire Hathaway raised its Delta Air Lines stake by 12% to $5.37 billion in the third quarter and sold over $1.6 billion of Bank of America stock, trimming that holding by nearly 6% to $24.8 billion.

rss · CNBC Finance · Nov 16, 23:01

**「Background」** Delta shares fell 11% in the quarter on rising jet fuel costs from the U.S.-Iran war, and the carrier cut its full-year earnings forecast; Bank of America fell over 4% as long-term Treasury yields surged.

**「Impact」** The Delta purchase supports the carrier as it recovers from fuel-cost pressure, with shares up 3.8% in the fourth quarter so far; the Bank of America trim reduces Berkshire&\#x27;s exposure to a bank pressured by surging long-term yields.

**Tags**: `#Berkshire Hathaway`, `#Delta Air Lines`, `#Bank of America`, `#13F filing`, `#airline industry`

---

<a id="item-finance-news-3"></a>
### [U.S. crude oil falls to $85.39 as Middle East exports recover](https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html) ⭐️ 7.0/10

U.S. crude oil fell 3.58% to $85.39 a barrel on Monday as Middle East exports recover, while the International Energy Agency reversed its earlier deficit forecast and now expects a 1.7 million barrels-per-day supply surplus in the fourth quarter of 2026.

rss · CNBC Finance · Nov 16, 22:19

**「Background」** Oil prices had spiked after the Feb. 28, 2026 closure of the Strait of Hormuz amid the Iran conflict, but crude exports have since returned to prewar levels as U.S. military escorts and pipeline rerouting restored flows, according to Kpler and CNBC reporting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/9/30/economic-war-is-iran-losing-its-leverage-over-the-strait-of-hormuz">Is Iran losing its leverage over the Strait of Hormuz? | US ...</a></li>
<li><a href="https://www.dallasfed.org/research/economics/2026/0320">What the closure of the Strait of Hormuz means for the global ...</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/iran-war-strait-hormuz-gulf-oil-fuel.html">Hormuz oil shipments at prewar levels but fuel shipments ...</a></li>

</ul>
</details>

**Tags**: `#oil prices`, `#energy markets`, `#IEA forecast`, `#Middle East exports`, `#supply surplus`

---