---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21
lang: en
---

> From 40 items, 19 important content pieces were selected

---

**Technology News**
1. [Claimed proof of finite-time blow-up for unforced Navier–Stokes equations](#item-tech-news-1) ⭐️ 10.0/10
2. [Tao Links Unforced Navier-Stokes Singularity to Generalized Riemann Hypothesis](#item-tech-news-2) ⭐️ 9.0/10
3. [Signal details technical measures to restrict AI agents from capturing data](#item-tech-news-3) ⭐️ 8.0/10
4. [Inkling 2 Mini: open-weights looped transformer with strong local performance](#item-tech-news-4) ⭐️ 8.0/10
5. [TSMC halts 16nm-and-below chip orders for Chinese firms under US export rules](#item-tech-news-5) ⭐️ 8.0/10
6. [Alessandro Masullo claims proof of Generalized Riemann Hypothesis](#item-tech-news-6) ⭐️ 7.0/10
7. [AI coding tools shift developers into architect roles](#item-tech-news-7) ⭐️ 7.0/10
8. [Aaronson blog post: AI &\#x27;stochastic parrots&\#x27; and the Riemann Hypothesis](#item-tech-news-8) ⭐️ 7.0/10
9. [US SEC probes Nvidia over potential accounting issues](#item-tech-news-9) ⭐️ 7.0/10
10. [US Tightens Chip Exports; India&\#x27;s Yotta Plans 100,000 GPUs](#item-tech-news-10) ⭐️ 7.0/10
11. [OpenAI background mode: 8-hour async tasks, up to 40% token discount](#item-tech-news-11) ⭐️ 7.0/10
12. [Tesla&\#x27;s assisted driving approved in Italy at €99/month](#item-tech-news-12) ⭐️ 7.0/10
13. [Linux KVM Flaw CVE-2026-99312 Exposes AMD Host Memory](#item-tech-news-13) ⭐️ 7.0/10

**Technology Blog**
1. [Why Caching LLM Outputs Is Not Worth It](#item-tech-blog-1) ⭐️ 8.0/10

**Financial News**
1. [Prediction market odds for S&amp;P 500 hitting 8,000 in 2026 collapse to 6%](#item-finance-news-1) ⭐️ 7.0/10
2. [Fed officials speak more as Warsh avoids forward guidance](#item-finance-news-2) ⭐️ 7.0/10
3. [Companies shift from buybacks to equity issuance, adding supply to bull market](#item-finance-news-3) ⭐️ 7.0/10
4. [Alibaba faces shareholder lawsuit over alleged export control concealment](#item-finance-news-4) ⭐️ 7.0/10
5. [Beijing proposes to bar deposit deductions for normal rental wear and tear](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Claimed proof of finite-time blow-up for unforced Navier–Stokes equations](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 10.0/10

A claimed proof of finite-time blow-up for the unforced Navier–Stokes equations has been posted, potentially resolving a Millennium Prize Problem. The result, associated with Tristan Buckmaster and Alpoge, is presented as a claim and has not been independently verified. It addresses the unforced case, in contrast to the forced version previously reported by OpenAI.

hackernews · trotro · Nov 20, 15:34 · [Discussion](https://news.ycombinator.com/item?id=50576232)

**「Background」** The Navier–Stokes equations describe the motion of viscous fluids, and the unforced Millennium Prize formulation asks whether smooth solutions exist for all time in three dimensions. A finite-time blow-up would mean a solution becomes singular in finite time. Earlier work reported a blow-up for a forced version, where an external force drives the singularity, but the unforced case is the original open problem.

**「Verification needed」** If verified, this claimed proof would resolve the unforced Millennium Prize statement, but the related OpenAI result had gaps with the original problem, so the mathematical community will need to verify whether this unforced proof avoids those gaps.

**「Community Discussion」** Commenters note that the unforced version is more physically realistic than the forced case previously reported by OpenAI, and some express interest in a physical demonstration or simulation of the blow-up. Others discuss the timing and competition with OpenAI&\#x27;s earlier result.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy">Navier–Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>

</ul>
</details>

**Tags**: `#Navier-Stokes`, `#mathematics`, `#fluid dynamics`, `#millennium problem`, `#PDE`

---

<a id="item-tech-news-2"></a>
### [Tao Links Unforced Navier-Stokes Singularity to Generalized Riemann Hypothesis](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 9.0/10

In a blog post published November 20, 2026, Terry Tao proposes a connection between the unforced Navier-Stokes singularity and the generalized Riemann hypothesis, suggesting that resolving one may inform the other. The post reportedly draws on modern developments in the Langlands program and arithmetic geometry, and has sparked discussion on Hacker News about AI-assisted proof verification and the Lean theorem prover. The result is presented as a blog post rather than a peer-reviewed proof, so its status remains informal.

hackernews · archon1410 · Nov 20, 17:21 · [Discussion](https://news.ycombinator.com/item?id=50578358)

**「Background」** The Navier–Stokes existence and smoothness problem is one of the Clay Mathematics Institute&\#x27;s Millennium Prize Problems, asking whether smooth solutions to the incompressible Navier–Stokes equations can develop singularities in finite time. Tao&\#x27;s post addresses the unforced case and connects it to the generalized Riemann hypothesis, with the Euler case distinguished by forced versus unforced results.

**「Lean verification of AI Riemann proof nears completion」** For mathematicians and the formal verification community, the AI-generated proof of the Riemann hypothesis is now being verified in Lean, with independent mathematicians attesting that the proof is almost certainly true. However, as one commenter notes, a passing Lean build does not by itself guarantee that the formalized statement matches the intended theorem, so verification must include checking the theorem statement, not just the proof script.

**「Community Discussion」** Commenters debated the reliability of AI-assisted formal verification: one noted that two independent Lean kernels accept the result, while another questioned whether a passing Lean build actually verifies the intended statement rather than a trivial one.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity , unforced Navier - Stokes singularity , and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean ( proof assistant) - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/">The AI Riemann hypothesis proof is almost... | Scientific American</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#AI`, `#proof verification`, `#Lean`, `#Riemann hypothesis`

---

<a id="item-tech-news-3"></a>
### [Signal details technical measures to restrict AI agents from capturing data](https://signal.org/blog/protecting-your-privacy/) ⭐️ 8.0/10

Signal has published a technical deep-dive on restricting AI agents from capturing data on mobile operating systems, addressing the concern that AI apps can access sensitive device data. The post describes technical measures Signal is developing to prevent AI apps from accessing Signal chats. The approach is concrete and timely, though not a paradigm shift.

hackernews · dotcoma · Nov 20, 09:42 · [Discussion](https://news.ycombinator.com/item?id=50572348)

**「Background」** Signal has long warned that OS-level AI agents, which can capture screen content, pose an existential threat to app-layer privacy because they can read messages even from apps that encrypt data at rest. The company&\#x27;s new screenshot restrictions are a direct response to this threat, with Reuters reporting that Signal announced the measure on Friday to stop AI agents from reading private chats on phones.

**「Impact」** Even without an AI app installed, a user&\#x27;s contacts could leak their chats, meaning the privacy risk extends beyond individual device control.

**「Community Discussion」** Commenters report Signal is &\#x27;cautiously optimistic&\#x27; about progress, while ada-h00k argues that relying on apps to prevent screenshots won&\#x27;t work long-term and users need to regain control over their operating system, suggesting alternatives like GrapheneOS. cimnine asks Signal to publish its forensics investigation findings so other developers with fewer resources could benefit.

<details><summary>References</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal &gt;&gt; Blog &gt;&gt; Signal is Serious About Protecting...</a></li>
<li><a href="https://www.reuters.com/legal/litigation/signal-restricts-screenshots-block-ai-agents-reading-messages-2026-11-20/">EXCLUSIVE: Signal restricts screenshots to block AI agents ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#AI agents`, `#mobile operating systems`, `#Signal`, `#data security`

---

<a id="item-tech-news-4"></a>
### [Inkling 2 Mini: open-weights looped transformer with strong local performance](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines has released Inkling 2 Mini, an open-weights looped transformer model trained end-to-end in nvfp4, with community benchmarks placing it near Qwen3.8-27B. A GGUF build is available for Ollama/llama.cpp, and early local tests report 27 tokens/s decode on a Ryzen 395 with Vulkan and about 10 t/s on an M1 Pro MacBook \(32GB, q4 xl\). The model is shipped, but real-world performance remains unverified; one user reported a failed coin-identification test after 12,000 tokens.

hackernews · jasondavies · Nov 20, 20:12 · [Discussion](https://news.ycombinator.com/item?id=50581260)

**「Background」** Inkling 2 Mini uses a looped transformer architecture, which reuses a set of layers across multiple passes rather than stacking distinct layers, a design that can reduce parameter count while preserving capability. It is Thinking Machines Lab&\#x27;s 26.4B-parameter mixture-of-experts model \(5.4B active\) released in November 2026, and it is an open-weights model.

**「Impact」** For local inference users, the GGUF release means Inkling 2 Mini can run on Ollama/llama.cpp today, but the required llama.cpp patches \(PRs 32694, 32657, 32429, 32704\) are unmerged, and a small patch is needed for a ~30% speed boost.

**「Community Discussion」** Commenters are cautiously optimistic: hedgehog reports promising coding tests and a ~30% speed patch, while dgacmu found the model nailed a CSV-sorting task but failed a coin-identification test after 12,000 tokens, and montroser cautions that benchmarks need to hold up in real-world scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling-2-mini">Inkling 2 Mini - Intelligence, Performance &amp; Price... | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#looped-transformer`, `#local-inference`, `#benchmarks`

---

<a id="item-tech-news-5"></a>
### [TSMC halts 16nm-and-below chip orders for Chinese firms under US export rules](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 8.0/10

TSMC has paused orders for Chinese companies at 16nm and below advanced process nodes, requiring customers to obtain prior US export licenses or exemptions under tightened semiconductor export rules. The change replaces TSMC&\#x27;s previous self-assessment of whether designs met exemption conditions with mandatory customer pre-application. Chinese firms are now limited to older nodes such as 28nm and 40nm, cutting off access to HBM needed for AI data centers. The US approved list includes Apple, AMD, and Nvidia, with no Chinese companies yet.

telegram · zaihuapd · Nov 21, 02:01

**「Prior export rule」** Previously, TSMC could evaluate on its own whether a customer&\#x27;s chip design met the conditions for a US export exemption. Under the tightened rules, Chinese customers must now apply in advance for a US export license or exemption before TSMC can supply 16nm and below processes.

**「Impact」** For Chinese chip designers and AI data center operators, the immediate consequence is that TSMC&\#x27;s pause on 16nm-and-below orders forces them to fall back to 28nm/40nm nodes and blocks access to HBM needed for AI data centers; lengthy US approval procedures could also disrupt production schedules. Chinese customers must now obtain US export licenses or exemptions before TSMC can resume 16nm-and-below orders.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trendforce.com/news/2026/11/20/news-tsmc-samsung-reportedly-pause-china-consumer-chip-shipments-under-new-u-s-rules-16nm-orders-affected/">[News] TSMC, Samsung Reportedly Pause China Consumer Chip ...</a></li>
<li><a href="https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls">TSMC has suspended some chip orders amid tighter export controls</a></li>
<li><a href="https://www.reuters.com/world/china/tsmc-tightens-china-ai-chip-curbs-new-us-rules-close-manufacturing-loophole-2026-11-19/">TSMC tightens China AI chip curbs as new US rules close ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#export controls`, `#TSMC`, `#AI hardware`, `#chip supply chain`

---

<a id="item-tech-news-6"></a>
### [Alessandro Masullo claims proof of Generalized Riemann Hypothesis](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 7.0/10

Ravi Vakil announced that Alessandro Masullo has a proposed proof of the Generalized Riemann Hypothesis, with Brian Conrad having reviewed it for months and provided extensive feedback that is being incorporated. The 940-page draft is being released early, reportedly because of the recent Anthropic AI discovery, and Vakil states the work is entirely human with no AI involvement. The proof is unverified and the draft is unfinished—section 1.1.1 is empty—so the claim remains a proposal rather than a confirmed result.

hackernews · jasondavies · Nov 20, 18:33 · [Discussion](https://news.ycombinator.com/item?id=50579568)

**「Background」** The Generalized Riemann Hypothesis \(GRH\) extends the Riemann Hypothesis to Dirichlet L-functions and is a central open problem in analytic number theory. The source links to a separate claimed proof of GRH by Levent Alpöge, and community comments describe an Anthropic announcement as the immediate context for this hurried release.

**「Impact」** Because Conrad says the proof is &quot;credible without major gaps&quot; but still &quot;undergoing major revision,&quot; the claim is not yet a theorem: mathematicians working on GRH-dependent results cannot rely on it, and the community now faces two competing proof claims \(Masullo&\#x27;s human draft and Anthropic&\#x27;s AI-assisted approach\) that both require verification.

**「Community discussion」** Commenters noted Masullo reportedly worked on the problem for 12 years and that the hurried release appears aimed at claiming credit alongside the Anthropic AI discovery, while others flagged the 940-page draft&\#x27;s unfinished state—section 1.1.1 is empty—and suggested mathematicians timestamp in-progress work to secure partial credit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/dueling-claims-of-riemann-hypothesis-proofs-emerge/">Dueling claims of Riemann hypothesis proofs ... | Scientific American</a></li>
<li><a href="https://www.nytimes.com/2026/11/20/science/anthropic-ai-math-riemann-hypothesis.html">Anthropic Mathematician Claims to Solve Riemann Hypothesis With...</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#generalized-riemann-hypothesis`, `#ai`, `#proof`, `#anthropic`

---

<a id="item-tech-news-7"></a>
### [AI coding tools shift developers into architect roles](https://manidoraisamy.com/developer-to-architect.html) ⭐️ 7.0/10

AI coding tools are shifting software engineers from hands-on coding into architect-like oversight roles, according to a blog post discussed on Hacker News. The post argues that as LLM-based coding agents take over implementation, developers increasingly focus on requirements, design, and review rather than writing code themselves. Commenters disagree sharply on whether this shift is a promotion or a downgrade, with some noting that architects are typically few per team and others warning of lower pay and reduced job satisfaction.

hackernews · QueensGambit · Nov 20, 18:17 · [Discussion](https://news.ycombinator.com/item?id=50579331)

**「Background」** Mani Doraisamy, the author of the post, is a developer-turned-founder who still writes code for a living and has built products for Google Workspace customers for over 15 years, according to a 2025 profile. This background frames his argument that AI coding tools are shifting developers from hands-on coding to architect-like oversight roles.

**「Impact」** Developers using AI coding agents may need to review generated code for leftover debugging infrastructure. One commenter reported that Claude left debugging tooling unflagged in an IPA IME keyboard project, effectively turning the program into a key-logger, suggesting that oversight of AI-generated code is becoming a necessary part of the role.

**「Community Discussion」** Commenters disagree on whether the shift is a promotion. whycombinetor argues that software engineering jobs have always required pushing back on requirements and designing data models, so engineers remain engineers even without hands-on coding, while uptrails counters that no one is actually being promoted and the likely outcome is lower pay and less enjoyable work as developers become a &\#x27;liability sink&\#x27; for LLM decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.skmurphy.com/blog/2025/06/09/build-a-cannon-to-kill-a-mosquito-with-mani-doraisamy/">Build a Cannon to Kill a Mosquito with Mani Doraisamy - SKMurphy, Inc.</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#developer roles`, `#LLM`, `#architecture`

---

<a id="item-tech-news-8"></a>
### [Aaronson blog post: AI &\#x27;stochastic parrots&\#x27; and the Riemann Hypothesis](https://scottaaronson.blog/?p=10344) ⭐️ 7.0/10

Scott Aaronson&\#x27;s blog post, published November 20, 2026, discusses the provocative idea that AI &\#x27;stochastic parrots&\#x27; may have proved the Riemann Hypothesis, framing it as a debate about machine understanding and mathematical discovery rather than a confirmed result. The post&\#x27;s actual content is not available for verification, and the title is sensational, so the claim should be treated as an opinion piece from a theoretical computer scientist, not a demonstrated proof. For readers, the discussion highlights the gap between AI-generated outputs and human-understandable explanations.

hackernews · stratos123 · Nov 20, 20:03 · [Discussion](https://news.ycombinator.com/item?id=50581084)

**「Background」** The Riemann hypothesis, first proposed in 1859 by Bernhard Riemann, claims that the locations of the prime numbers along the number line, which appear random at first blush, are actually determined by an intricate, meaningful order. Recent AI-assisted work, including a claim by an Anthropic mathematician and other machine-learning approaches, has renewed attention on the problem and set the stage for Aaronson&\#x27;s discussion of whether a &\#x27;stochastic parrot&\#x27; system can be said to have proved it.

**「Community discussion」** Commenters draw parallels to chess AI, where Stockfish&\#x27;s NNUE evaluator yields explanations that are aggregates of calculations, leaving an unsatisfying position for &\#x27;why&\#x27; questions \(janalsncm\), and question whether humans can be content with not understanding increasingly complex systems \(jstummbillig\).

<details><summary>References</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis , most...</a></li>
<li><a href="https://www.youtube.com/watch?v=ljFZfYZLHj8">AI Closes In on the Riemann Hypothesis | World Science... - YouTube</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#Riemann Hypothesis`, `#stochastic parrots`, `#theoretical computer science`

---

<a id="item-tech-news-9"></a>
### [US SEC probes Nvidia over potential accounting issues](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627) ⭐️ 7.0/10

The US Securities and Exchange Commission has opened an investigation into Nvidia&\#x27;s accounting practices, according to sources. The probe is examining potential accounting issues related to the company&\#x27;s financing and chip sales. No findings have been confirmed; the investigation is ongoing.

hackernews · ftchd · Nov 20, 20:22 · [Discussion](https://news.ycombinator.com/item?id=50581438)

**「Background」** The probe follows scrutiny of Nvidia&\#x27;s financing role for neoclouds after the company&\#x27;s CEO exit, with Reuters reporting that the SEC is examining accounting practices and adding to the chipmaker&\#x27;s legal woes.

**「Community discussion」** Commenters debated whether the probe reflects long-standing circular financing and questionable chip sales. One argued the investigation is a continuation of issues that have plagued Nvidia for years, while another questioned how the CFO-turned-acting-CEO could have been unaware of alleged blackmarket chip sales.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investing.com/news/economy-news/exclusiveus-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-5042460">Nvidia ’s accounting is a focus of US SEC investigation, sources say...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/nvidia-financing-role-neoclouds-faces-181433179.html">Nvidia ’s financing role for neoclouds faces scrutiny after CEO exit</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#SEC`, `#accounting`, `#AI hardware`, `#regulation`

---

<a id="item-tech-news-10"></a>
### [US Tightens Chip Exports; India&\#x27;s Yotta Plans 100,000 GPUs](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 7.0/10

The US is tightening advanced chip exports to Malaysia, Thailand, and Singapore, and Indian AI firms expect spillover demand. Yotta says it will add about 100,000 GPUs over the next year, roughly 10% of India&\#x27;s current compute capacity. India has 153 data centers, ranking 14th globally, while Reliance has pledged up to $110 billion and Adani $100 billion for AI infrastructure, though shortages and capital constraints persist.

telegram · zaihuapd · Nov 20, 07:31

**「Background」** India currently operates 153 data centers, ranking 14th globally, and has been constrained by compute infrastructure shortages and limited capital. This existing limitation is the context for India&\#x27;s AI industry seeking to absorb demand redirected by US export controls on advanced chips to Southeast Asia.

**「Impact」** For Indian AI developers, the export curbs may redirect GPU supply to India, but the country&\#x27;s limited data-center capacity and capital constraints mean the added compute cannot be deployed quickly.

**Tags**: `#AI infrastructure`, `#chip export controls`, `#India`, `#GPU`, `#data centers`

---

<a id="item-tech-news-11"></a>
### [OpenAI background mode: 8-hour async tasks, up to 40% token discount](https://developers.openai.com/api/docs/guides/background) ⭐️ 7.0/10

OpenAI has launched a public beta of background mode for its API, which turns long-running requests into asynchronous jobs. Developers set background: true and choose a 2h or 8h completion window via background\_options.completion\_window, receiving 30% or 40% lower token rates respectively; omitting the window defaults to soonest with no discount. The discount applies to GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, and GPT-6 Luna. Background mode also temporarily stores response data even when store is false or zero data retention is enabled.

telegram · zaihuapd · Nov 20, 11:15

**「Background」** OpenAI&\#x27;s API requests are synchronous by default, so a long-running task holds the connection until it finishes. Background mode instead queues the work and returns control to the client, allowing the task to complete within a chosen 2–8 hour window.

**「Impact」** Developers must explicitly set background: true and choose a 2h or 8h window to get the discount; the default soonest mode offers no savings. The temporary response storage, even with store: false or zero data retention, is a data-handling consideration for compliance-sensitive applications.

**Tags**: `#OpenAI`, `#API`, `#background mode`, `#cost optimization`, `#async processing`

---

<a id="item-tech-news-12"></a>
### [Tesla&\#x27;s assisted driving approved in Italy at €99/month](https://www.ilfattoquotidiano.it/2026/11/20/tesla-assisted-driving-arriva-in-italia-via-libera-alla-guida-assistita-avanzata/8578482/) ⭐️ 7.0/10

Tesla&\#x27;s advanced driver assistance system has been approved by Italian regulators and will roll out via over-the-air update, with a €99/month subscription. Italy becomes the 12th European market for the feature, which first launched in the Netherlands in April 2026. The system handles city roads, intersections, and lane changes, but requires the driver to monitor and remain responsible. Tesla claims over 200 million km driven in Europe and collision rates as low as one-seventh of manual driving, though these figures come from the company&\#x27;s own methodology and are not independently verified.

telegram · zaihuapd · Nov 20, 12:14

**「Background」** The system is a supervised advanced driver assistance feature, not fully autonomous driving. It was first launched in the Netherlands in April 2026, and Italy is now the 12th European market to approve it.

**「Impact」** For Italian Tesla owners, the approval means they can subscribe to the feature for €99/month and receive it via OTA, but they must keep their hands on the wheel and remain legally responsible for the vehicle at all times.

**Tags**: `#autonomous driving`, `#Tesla`, `#regulatory approval`, `#AI systems`, `#Europe`

---

<a id="item-tech-news-13"></a>
### [Linux KVM Flaw CVE-2026-99312 Exposes AMD Host Memory](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 7.0/10

A Linux KVM vulnerability \(CVE-2026-99312\) lets virtual machines read host memory on AMD hosts with nested virtualization enabled. Researchers demonstrated reading roughly 127 GB of host memory from inside a VM on DigitalOcean infrastructure. The upstream fix shipped November 18 with stable kernel 7.3.5 and related releases, but Debian and Ubuntu distribution kernels remain unpatched. Until patches arrive, administrators should disable nested virtualization on affected AMD hosts.

telegram · zaihuapd · Nov 20, 14:23

**「Background」** KVM \(Kernel-based Virtual Machine\) is a Linux kernel module that turns the kernel into a hypervisor, running virtual machines as isolated processes with separate memory address spaces. Nested virtualization allows a VM to run its own hypervisor and guest VMs inside it, which requires the host to expose AMD-V hardware virtualization features to the guest. CVE-2026-99312 breaks the memory isolation that normally prevents a guest from reading host memory.

**「Impact on AMD KVM hosts」** Operators of AMD KVM hosts with nested virtualization enabled face a host-memory disclosure risk: a guest VM can read host RAM, with researchers demonstrating roughly 127 GB read on DigitalOcean. Because Debian and Ubuntu distribution kernels remain unpatched, disabling nested virtualization is the immediate mitigation until patched kernels are deployed; Intel-based KVM hosts are unaffected since the vulnerable code is AMD-specific.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE - 2026 - 99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization, Responsible Disclosure , and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to- Host Escape | Terra Security Research</a></li>

</ul>
</details>

**Tags**: `#security`, `#KVM`, `#AMD`, `#virtualization`, `#Linux kernel`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Why Caching LLM Outputs Is Not Worth It](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 8.0/10

rss · Sean Goedecke · Nov 21, 00:00

**「Background」** LLM inference economics depends on caching inputs so the conversation history isn&\#x27;t recomputed each turn. But agents also repeat content in their visible output—quoting files, restating evidence, or replaying sample outputs—and output tokens are far more expensive than input tokens. That repetition looks like an obvious waste worth eliminating.

**「Solution」** Sean Goedecke considers fixing this by fine-tuning or prompting models to reference segments of their own history instead of repeating them, with the harness expanding those references transparently. The problem is that this only optimizes visible output. From his own agent histories, visible output is roughly 6% of total output tokens, while reasoning tokens account for about 50% and tool calls about 44%. Under Amdahl&\#x27;s law, even an unrealistically optimistic two-thirds reduction in visible output saves only 4% of total output tokens. The real savings lie in the invisible 94%, which depends mostly on model intelligence: smarter models need fewer reasoning tokens and tool calls to reach the right answer. That is why a model that is 5x more expensive per token can still be cheaper overall if it uses 6x fewer tokens.

**「Takeaway」** The author&\#x27;s conclusion is that output caching is a bad investment: it targets a tiny fraction of total tokens. Instead, teams should focus on reducing reasoning and tool-call tokens through smarter models and better harnesses, since that is where the dominant cost lies.

**Tags**: `#LLM caching`, `#Amdahl&\#x27;s law`, `#output tokens`, `#reasoning tokens`, `#agent economics`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Prediction market odds for S&amp;P 500 hitting 8,000 in 2026 collapse to 6%](https://www.cnbc.com/2026/11/20/sp-500-8000-kalshi-odds-ai-selloff.html) ⭐️ 7.0/10

Odds on Kalshi that the S&amp;P 500 will cross 8,000 in 2026 fell to 6% from 72% on Oct. 13, as an AI-led sell-off pushed the Nasdaq negative for the year and the Dow and S&amp;P 500 into correction territory, leaving the S&amp;P 500 up just over 2% year to date.

rss · CNBC Finance · Nov 20, 19:59

**「Background」** The sell-off follows Anthropic&\#x27;s record-breaking IPO, which failed to stem losses in AI-linked companies, and a hawkish Federal Reserve that signaled more interest-rate hikes.

**「Impact on investors」** Investors in U.S. equities, particularly tech and AI-exposed names, face continued volatility as markets price in a Federal Reserve rate hike in December, a scenario the Stock Trader&\#x27;s Almanac says could push the market&\#x27;s low to mid- or late December.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off">Global stock markets slump as Anthropic IPO fails to stem AI sell - off</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-19/gold-set-for-worst-week-since-march-on-hawkish-fed-ai-selloff">Gold Set for Worst Week Since March on Hawkish Fed, AI Selloff</a></li>
<li><a href="https://www.fool.com/investing/2026/11/08/markets-are-pricing-in-a-fed-rate-hike-in-december/">Markets Are Pricing in a Fed Rate Hike in December. Here&#x27;s ...</a></li>

</ul>
</details>

**Tags**: `#stock market`, `#prediction markets`, `#AI sell-off`, `#Federal Reserve`, `#S&amp;P 500`

---

<a id="item-finance-news-2"></a>
### [Fed officials speak more as Warsh avoids forward guidance](https://www.cnbc.com/2026/11/20/warsh-fed-forward-guidance-rate-hikes.html) ⭐️ 7.0/10

Fed officials have been speaking more frequently and with conflicting views as Chairman Kevin Warsh avoids forward guidance, with Bank of America recording the most Fedspeak in two weeks since early 2025 and markets pricing a 100% chance of a quarter-point rate hike in December.

rss · CNBC Finance · Nov 20, 21:10

**「Background」** The Fed held its benchmark rate at the October meeting, and minutes showed some officials would have accepted a hold if the Fed had clearly communicated further tightening, highlighting the tension over Warsh&\#x27;s refusal to provide forward guidance.

**「Impact」** Bank of America said the back-and-forth could cause undue rate volatility in already turbulent times, affecting investors and businesses as markets price a likely December hike.

**Tags**: `#Federal Reserve`, `#monetary policy`, `#forward guidance`, `#inflation`, `#interest rates`

---

<a id="item-finance-news-3"></a>
### [Companies shift from buybacks to equity issuance, adding supply to bull market](https://www.cnbc.com/2026/11/20/equity-issuance-bull-market-problem.html) ⭐️ 7.0/10

U.S. companies have shifted from buying back shares to issuing them, with net new issuance equal to 3.1% of total market capitalization as of late last week, according to Acadian Asset Management analysis. The reversal follows 2024, when firms were net repurchasers.

rss · CNBC Finance · Nov 20, 14:15

**「Background」** The shift adds to the supply of shares that the four-year-old bull market must absorb, reversing a trend that had helped boost prices by shrinking the number of shares available. The Baker-Wurgler equity share, which measures equity issuance as a share of total stock and bond issuance, peaked at about 18% in 2021 and has risen recently but remains below that peak.

**「Impact」** The increased supply could act as a headwind on the bull market, affecting equity investors broadly, as recent deals from Oracle, Meta, Alphabet, SpaceX, and Anthropic add shares to the market.

**Tags**: `#equity issuance`, `#stock buybacks`, `#market structure`, `#IPO activity`, `#bull market`

---

<a id="item-finance-news-4"></a>
### [Alibaba faces shareholder lawsuit over alleged export control concealment](https://www.zaobao.com.sg/news/china/story20261120-10029652) ⭐️ 7.0/10

Alibaba was sued by shareholders in Manhattan federal court on Nov 19, alleging it concealed business relationships with Alice Huang and Singapore firm Chaosu International and underestimated export control risks in its 2024-2026 annual reports to boost its stock price. The complaint says the stock fell 14% over four trading days last week; the claim amount is unspecified, and CEO Wu Yongming is also a defendant.

telegram · zaihuapd · Nov 20, 09:32

**「Background」** The suit follows reports that linked Alibaba to Megaspeed, an Nvidia cloud partner controlled by Alice Huang, who was linked to Nvidia CEO Jensen Huang.

<details><summary>References</summary>
<ul>
<li><a href="https://www.freemalaysiatoday.com/category/business/2026/11/20/alibaba-accused-of-hiding-ties-to-suspected-spy-in-nvidia-scandal">Alibaba accused of hiding ties to suspected spy in Nvidia scandal | FMT</a></li>
<li><a href="https://www.zerohedge.com/political/gpus-capri-sunsets-and-detained-husband-who-alice-huang">GPUs, Capri Sunsets, And A Detained Husband: Who Is Alice ...</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#shareholder lawsuit`, `#class action`, `#export controls`, `#stock decline`

---

<a id="item-finance-news-5"></a>
### [Beijing proposes to bar deposit deductions for normal rental wear and tear](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

Beijing&\#x27;s housing and market-regulation agencies proposed on Nov. 20 to revise the city&\#x27;s model rental contract, clarifying that landlords cannot deduct deposits for normal wear and tear from a tenant&\#x27;s ordinary use. The draft, open for public comment, also requires subletting companies to place rent and deposits in supervised accounts.

telegram · zaihuapd · Nov 20, 13:46

**「Background」** The draft, issued jointly by Beijing&\#x27;s housing and market-regulation agencies, revises the city&\#x27;s standard rental contract and is open for public comment.

**「Impact」** If adopted, the change would protect Beijing renters from deposit deductions for ordinary use and tighten oversight of subletting companies, which would have to move rent and deposits to regulated accounts.

**Tags**: `#housing policy`, `#rental market`, `#consumer protection`, `#Beijing`, `#regulation`

---