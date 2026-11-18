---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 43 items, 12 important content pieces were selected

---

**Technology News**
1. [Java4Shell: OpenJDK Base64 RCE hits AVX-512 x86-64 CPUs](#item-tech-news-1) ⭐️ 8.0/10
2. [Phrack 73 released with Docker escape exploit and SSH1 RCE history](#item-tech-news-2) ⭐️ 8.0/10
3. [Solid 2.0 released with server RPC, live/broadcast, and better diagnostics](#item-tech-news-3) ⭐️ 8.0/10
4. [Microsoft releases MAI Code 2 and Code 2 Flash for GitHub Copilot](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI ships GPT-6.2 Astra and Sol with price cuts](#item-tech-news-5) ⭐️ 8.0/10
6. [Datasette Lite rewrite runs full Datasette in browser via service workers and Pyodide](#item-tech-news-6) ⭐️ 8.0/10
7. [Highly classified US national security network suffers outage](#item-tech-news-7) ⭐️ 7.0/10
8. [ONNX Runtime repo vanishes from GitHub, disrupting pipelines](#item-tech-news-8) ⭐️ 7.0/10
9. [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](#item-tech-news-9) ⭐️ 7.0/10
10. [External sandbox pattern for coding agents released](#item-tech-news-10) ⭐️ 7.0/10
11. [China&\#x27;s Q/V-band ground test hits 27 Gbps with 512QAM](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [China to assess 17 automakers&\#x27; 60-day supplier payment terms](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Java4Shell: OpenJDK Base64 RCE hits AVX-512 x86-64 CPUs](https://calif.io/java4shell/) ⭐️ 8.0/10

Java4Shell \(CVE-2026-114938\) is an unauthenticated remote code execution vulnerability in OpenJDK&\#x27;s Base64 processing, with a CVSS 4.0 score of 9.2 and a latency of nearly four years. It affects Java 17 \(17.0.6 and later in the 17 line\), 21, 25, and 27; standard Java 8/11 are usually unaffected, except Oracle Java 8 Performance Pack. The vulnerability only impacts x86-64 server processors with AVX-512 VBMI instructions, roughly Intel Ice Lake and newer Xeon \(2021+\) and AMD Zen 4 and newer EPYC/Ryzen \(2022+\); ARM64 is not affected.

hackernews · werrett · Nov 17, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50538240)

**「Background」** OpenJDK&\#x27;s Base64 decoding has an optimized HotSpot stub that uses the AVX-512 VBMI instruction set on x86-64 processors, and CVE-2026-114938 targets this path. The affected code has been present since Java 17.0.6 and affects the 17, 21, 25, and 27 lines on Intel Ice Lake-or-newer Xeon and AMD Zen 4-or-newer EPYC/Ryzen CPUs, while ARM64 and standard Java 8/11 are not affected.

**「Patch Java deployments on AVX-512 VBMI x86-64 servers」** Organizations running Java 17.0.6 and later in the 17 line, or Java 21, 25, or 27, on x86-64 servers with AVX-512 VBMI \(Intel Ice Lake and newer Xeon, AMD Zen 4 and newer EPYC/Ryzen\) face an unauthenticated remote code execution risk through the HotSpot Base64 decoder; ARM64 and standard Java 8/11 deployments are generally not affected, except Oracle Java 8 Performance Pack. Oracle released Java updates on November 17, and no exploitation has been reported as of the write-up, so operators should patch immediately. Until patched, Semgrep&\#x27;s detection scripts can identify vulnerable hosts, and the community-reported -XX:UseAVX=2 flag may disable the affected AVX-512 Base64 path, though this workaround is unconfirmed.

**「Community Discussion」** Commenters noted that Semgrep published free detection scripts for the five exploit conditions, including HotSpot VM builds \(OpenJDK, Oracle JDK, GraalVM JDK\) while OpenJ9, GCJ, and Azul Prime are not affected \(ievans\). Another commenter relayed an unconfirmed Twitter suggestion that running Java with -XX:UseAVX=2 may work around the AVX-512 Base64 decoding issue \(AgentME\), and the exploit is sensitive to network RTT and jitter \(lucasluitjes\).

<details><summary>References</summary>
<ul>
<li><a href="https://cycode.com/blog/java4shell-cve-2026-114938/">Java4Shell (CVE-2026-114938): Affected Versions, How to Check ...</a></li>
<li><a href="https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938/">Java4Shell: Remote Code Execution in OpenJDK (CVE-2026-114938)</a></li>
<li><a href="https://threatdefence.com/article/java4shell-cve-2026-114938-openjdk-rce-patching-hunting">Java4Shell CVE-2026-114938: Java 17 RCE Checks and Hunting</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#Java`, `#OpenJDK`, `#RCE`

---

<a id="item-tech-news-2"></a>
### [Phrack 73 released with Docker escape exploit and SSH1 RCE history](https://phrack.org/issues/73/introduction_md) ⭐️ 8.0/10

Phrack 73 has been released, featuring technical articles including a Docker escape exploit and a historical retrospective on the 2000 SSH1 RCE. The release continues the long-running hacker ezine&\#x27;s tradition of deep technical content for security researchers. The issue is available on the Phrack website.

hackernews · notmine1337 · Nov 17, 18:31 · [Discussion](https://news.ycombinator.com/item?id=50535992)

**「Background」** Phrack is a long-running hacker ezine that has published technical security articles since the late 1980s, serving as both a technical journal and a cultural document of the hacking scene. Docker escapes are a known class of container security vulnerability where an attacker breaks out of a container&\#x27;s isolation to access the host system, a topic that has been covered in security research for years.

**「Impact」** Security practitioners can review the Docker escape article for container escape techniques, which is directly relevant to container security assessments.

**「Community discussion」** One commenter asked whether the Docker escape exploit has been responsibly disclosed with a CVE or released without prior disclosure, while another recommended the SSH1 RCE history as a useful read for reflecting on how quickly vulnerability exploitation has evolved.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mindpatch.net/posts/docker-escape/">Docker Escape : Breaking Out of Containers | MindPatch</a></li>
<li><a href="https://phrack.org/">Phrack Magazine</a></li>

</ul>
</details>

**Tags**: `#security`, `#hacking`, `#phrack`, `#exploit`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Solid 2.0 released with server RPC, live/broadcast, and better diagnostics](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 8.0/10

Solid 2.0, the major release of the reactive UI framework, is now available, adding server RPC, live/broadcast features, and improved debugging diagnostics. The release targets SolidJS developers building full-stack applications, enabling reactive data flows between client and server without a separate API layer. The framework&\#x27;s new diagnostics are designed to make state and reactivity issues easier to trace.

hackernews · pier25 · Nov 17, 18:56 · [Discussion](https://news.ycombinator.com/item?id=50536387)

**「Background」** SolidJS is a reactive UI framework that uses fine-grained reactivity primitives \(signals, stores, effects\) instead of a virtual DOM. The 1.x line established this architecture, and 2.0 arrives after an extended development cycle as a major version release.

**「Impact」** For SolidJS developers, the release adds server RPC and live/broadcast capabilities, allowing reactive data to flow between client and server without a separate API layer, and improves debugging diagnostics.

**「Community discussion」** Commenters compared Solid 2.0&\#x27;s server RPC and live/broadcast features favorably to LiveView and htmx/datastar, with one noting Remix never fully closed the frontend-backend gap. Another observed that the &\#x27;Built to Be Written by Agents&\#x27; diagnostics are simply better debugging tools that would also benefit human developers.

**Tags**: `#SolidJS`, `#frontend`, `#reactive programming`, `#major release`, `#web development`

---

<a id="item-tech-news-4"></a>
### [Microsoft releases MAI Code 2 and Code 2 Flash for GitHub Copilot](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 8.0/10

Microsoft released MAI Code 2 and MAI Code 2 Flash, new coding models integrated into GitHub Copilot. Community reports indicate strong real-world performance comparable to leading models like Claude Opus, with one user reporting that MAI Code 2 resolved Python build issues in WSL/Ubuntu and Azure deployment problems. One user reported GitHub Copilot offered MAI Code 2 at 50% on the day of release.

hackernews · lemonish97 · Nov 17, 18:25 · [Discussion](https://news.ycombinator.com/item?id=50535885)

**「Background」** Microsoft&\#x27;s MAI Code models are coding-focused models offered through GitHub Copilot, and the new Code 2 and Code 2 Flash are the latest release in that line.

**「Copilot users get cheaper, comparable coding models」** GitHub Copilot users can now switch to MAI Code 2, which one user reported resolved Python build and Azure deployment issues without a noticeable difference from Claude Opus; Microsoft also claims MAI Code 2 Flash matches GPT-6 Luna and Claude Haiku 5.5 on routine coding benchmarks at 65% and 20% of their cost, respectively.

**「Community Discussion」** Commenters debated whether the rapid catch-up reflects distillation of OpenAI models or genuine progress, with one user reporting that MAI Code 2 resolved Python and Azure deployment issues and felt comparable to Claude Opus. Another user questioned the fate of Microsoft&\#x27;s Phi series, while a third said they cancelled their Copilot subscription, finding the current tier hard to justify.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models/">GitHub Copilot Fusion updates: more availability, benchmarks , and...</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at... | Microsoft AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding assistant`, `#Microsoft`, `#model release`, `#GitHub Copilot`

---

<a id="item-tech-news-5"></a>
### [OpenAI ships GPT-6.2 Astra and Sol with price cuts](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/) ⭐️ 8.0/10

OpenAI has released GPT-6.2 Astra and GPT-6.2 Sol, available in the API as gpt-6.2-astra and gpt-6.2-sol, with LLM 0.38 adding support for both. Astra&\#x27;s input/output price drops to $8/$40 per million tokens \(80% of GPT-6 Astra&\#x27;s $10/$50\) and its cached-input price falls from $1 to $0.40 per million, while Sol holds at $2/$10, half the price of GPT-5.6 Sol. Early reviews are mixed: Astra trails Claude Fable 5.2 on some benchmarks, and Theo Browne&\#x27;s pre-release feedback letter describes the model interrupting long tasks to ask users unanswerable internal implementation details.

rss · Simon Willison · Nov 17, 22:38

**「Background」** GPT-6 Astra and GPT-6.1 Sol were OpenAI&\#x27;s previous frontier and efficient models, priced at $10/$50 and $2/$10 per million tokens respectively; GPT-6.2 Astra cuts that to $8/$40 while Sol keeps the same price. Claude Fable 5.2, which Astra now matches in price, was itself 80% of its predecessor&\#x27;s cost.

**「Impact」** Developers evaluating GPT-6.2 models for complex 3D animation tasks should note that in Simon Willison&\#x27;s Yonkers mech benchmark, neither model matched Claude Fable 5.2 or Gemini 4 Carbon.

**「Community Discussion」** Commenters report mixed results: chriddyp reported large cost reductions in a data analytics exam \(Astra ~$20 to ~$4, Sol $2.6 to $1.2\) with similar accuracy, while Theo Browne&\#x27;s pre-release feedback letter describes Astra interrupting long tasks to ask users unanswerable internal implementation details. Topfi finds the new models&\#x27; office-work examples inferior to earlier models, and thefourthchime&\#x27;s PacBench results show Astra scoring 92 in 6.6 minutes for $2.04 versus Kimi K3.1 Pro&\#x27;s 93 in 11.5 minutes for $0.68.

**Tags**: `#OpenAI`, `#GPT-6.2`, `#LLM pricing`, `#AI models`, `#agentic AI`

---

<a id="item-tech-news-6"></a>
### [Datasette Lite rewrite runs full Datasette in browser via service workers and Pyodide](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison has released a complete rewrite of Datasette Lite that uses service workers and Pyodide to run the full server-side Datasette Python application in the browser, making it nearly indistinguishable from the real thing. The new version can load any SQLite database, JSON file, CSV file, or SQL script; select a released Datasette version from PyPI; load a specific commit, tag, or branch from the Datasette GitHub repository; pick from over 100 SQLite versions; and install additional Datasette plugins from PyPI or wheel URLs, including JavaScript visualization tools. The rewrite fixes the original 2022 version&\#x27;s hack, which used innerHTML injection and failed to execute JavaScript features. URLs to lite.datasette.io must point to files with open CORS headers, such as those hosted in Gists.

rss · Simon Willison · Nov 17, 16:48

**「Background」** Datasette Lite was first launched in 2022 as a port of the Datasette Python application to run in the browser using WebAssembly and Pyodide. The original version worked by running Datasette in a Pyodide web worker, simulating requests, and injecting the resulting HTML into the top-level page with innerHTML, which meant any feature using JavaScript failed to work. The new rewrite uses service workers instead, allowing the full server-side application to run in the browser.

**「Impact」** The ability to load specific Datasette references, plugins, and SQLite versions makes Datasette Lite a practical tool for linking to demos of work-in-progress features or bug reproductions without spinning up a web server. Willison has already used it in Datasette development, posting links to demonstrate a pagination bug and its fix in a GitHub issue. Users should note that database and metadata URLs must have open CORS headers, which Gists provide.

**Tags**: `#WebAssembly`, `#Pyodide`, `#Datasette`, `#service workers`, `#Python`

---

<a id="item-tech-news-7"></a>
### [Highly classified US national security network suffers outage](https://www.cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down) ⭐️ 7.0/10

A highly classified US national security communications network experienced an outage, according to Reuters reporting cited by CNN. The incident raised concerns about critical infrastructure resilience and prompted speculation about AI-related attacks and staffing cuts, though no official cause has been confirmed.

hackernews · monkeydust · Nov 17, 15:38 · [Discussion](https://news.ycombinator.com/item?id=50532849)

**「Background」** The affected system is a highly classified communications network used by US national security agencies. Such networks are expected to carry sensitive government traffic with high availability, so a full outage is unusual and raises questions about the resilience of critical national security infrastructure.

**「Impact」** For NSA personnel, the outage temporarily disrupted the agency&\#x27;s internal classified communications; the NSA described the disruption as a &quot;temporary degradation&quot; during scheduled work, and the network—known as NSA Net—carries classified communications and information sharing within the agency.

**「Community Discussion」** Commenters debated the public disclosure: some found it surprising that the NSA would announce the outage before restoring it, while others speculated it was a strategic move. Several commenters attributed the incident to AI-assisted attacks or staffing cuts, but these remain unverified opinions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/highly-classified-us-national-security-communications-network-is-down-cnn-2026-11-17/">Classified US national security communications network hit by ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-11-17/highly-classified-us-national-security-communications-network-is-down-cnn-reports">Highly Classified US National Security Communications Network ...</a></li>
<li><a href="https://www.cbsnews.com/news/nsa-network-down-classified-fort-meade/">NSA&#x27;s classified internal network goes down, sources say</a></li>

</ul>
</details>

**Tags**: `#national security`, `#critical infrastructure`, `#network outage`, `#IT operations`, `#cybersecurity`

---

<a id="item-tech-news-8"></a>
### [ONNX Runtime repo vanishes from GitHub, disrupting pipelines](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

Microsoft&\#x27;s ONNX Runtime repository has disappeared from GitHub, breaking CI/CD pipelines that depend on the widely used open-source inference engine. The 22k-star repo is no longer accessible, and a user reported that evals began failing this morning with no advance warning. The cause is not yet established; commenters speculate about a security-related takedown, but no official explanation has been provided.

hackernews · nvader · Nov 17, 23:18 · [Discussion](https://news.ycombinator.com/item?id=50539610)

**「Background」** ONNX Runtime is a cross-platform inference and training machine-learning accelerator used in Microsoft products \(tool-2-2, tool-2-3\). In March 2026, a commenter noted a parser flaw that could allow an ONNX model to read from arbitrary file paths or memory addresses without validation \(tool-2-1\). The repository&\#x27;s sudden disappearance comes after that security concern, though the cause has not been confirmed.

**「Impact」** Developers relying on the repository face broken builds and blocked updates; one commenter identified a fork at github.com/intel/onnxruntime with Intel OpenVINO modifications as a possible alternative while the cause is investigated.

**「Community Discussion」** Commenters disagree on the cause: one suspects a compromised package or cleanup, another points to potential backdoor attack vectors against models, and a third notes that ONNX telemetry exfiltrates application data unless disabled. A user whose evals failed reports no advance warning, while another suggests the Intel fork as a stopgap.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50539610">Microsoft &#x27;s ONNX Runtime has disappeared from GitHub</a></li>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft /onnxruntime: ONNX Runtime : cross-platform, high...</a></li>
<li><a href="https://onnxruntime.ai/docs/">ONNX Runtime is a cross-platform machine-learning model accelerator</a></li>

</ul>
</details>

**Tags**: `#ONNX Runtime`, `#Microsoft`, `#GitHub`, `#open source`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Quad9 has withdrawn its DNS service from France after a court ordered it to block certain domains, making its resolver unavailable to French users. Cloudflare discusses the withdrawal as a sign of broader concerns about court-ordered DNS blocking and internet governance. Quad9&\#x27;s CTO reports unanimous support for the organization&\#x27;s position at IETF 127, though Cloudflare does not commit to any action if its own appeal fails.

hackernews · subset · Nov 17, 22:13 · [Discussion](https://news.ycombinator.com/item?id=50538994)

**「Background」** Quad9, a Swiss non-profit that operates a free public DNS resolver, announced last month that it will stop serving French users on November 24, 2026, after a Paris court ordered it to block pirate sites and set penalties for non-compliance. The withdrawal follows a similar exit by another DNS resolver and comes as a Belgian court has ordered Cloudflare, Google, and Cisco to begin blocking websites through their public resolvers by early January 2027.

**「Impact on French users and DNS providers」** Quad9&\#x27;s withdrawal removes a privacy-focused DNS resolver from French users, and the court-ordered blocking that prompted it raises concerns about similar actions against other DNS providers. Quad9&\#x27;s CTO, johnhtodd, reported at IETF 127 that attendees showed unanimous support for the organization&\#x27;s position so far, while noting the IETF&\#x27;s contrarian culture. Community commenter driverdan pressed Cloudflare to commit to withdrawing from impacted countries if its own appeal fails, a question the blog post does not answer.

**「Community Discussion」** Quad9&\#x27;s CTO, commenting as johnhtodd, reports unanimous support at IETF 127 for the organization&\#x27;s position and says he has met no one outside the rightsholder industry who favors the court-ordered blocking. Another commenter, driverdan, criticizes Cloudflare for not committing to withdraw from affected countries if its own appeal fails, calling the article vague.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://reclaimthenet.org/quad9-leaving-france-over-dns-blocking-order">Quad9 to Leave France Over DNS Blocking Order - Reclaim The Net</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/">DNS Resolver Quad9 Will Leave France After Court Orders ...</a></li>
<li><a href="https://www.ietf.org/meeting/127/">IETF | IETF 127 San Francisco</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#internet governance`, `#Quad9`, `#Cloudflare`, `#censorship`

---

<a id="item-tech-news-10"></a>
### [External sandbox pattern for coding agents released](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison and Prime Radiant introduced the external sandbox pattern, in which code executed by a coding agent runs inside a dedicated sandbox while the agent itself lives outside that sandbox, reducing the risk that a prompt injection attack or mistake could cause damaging actions on the host machine. Three sandbox server implementations were released: external-sandbox-v86 \(a Node.js server using v86 to run Alpine Linux inside WebAssembly\), external-sandbox-container \(a Python web server running Alpine Linux inside an Apple Containers instance\), and external-sandbox-quicksand \(a Python web server using Microsoft&\#x27;s Quicksand library, which bundles QEMU and Alpine Linux\). All three expose the same localhost API and can be configured so that Pi, Claude Code, or Codex send API calls to the sandbox whenever they execute code. The sandboxes also include an optional HTTP/HTTPS allow-list proxy to control which hosts the agent&\#x27;s code can communicate with, plus a credential replacement mechanism for authenticated API calls without sharing a secret with the agent.

rss · Simon Willison · Nov 17, 22:52

**「Background」** Prompt injection attacks can trick LLM-based coding agents into executing harmful commands on a user&\#x27;s machine, a particular concern when running local models. The external sandbox pattern addresses this by keeping the agent itself outside the sandbox while routing the code it executes into a dedicated, isolated environment.

**「Impact」** Developers can now safely experiment with local models by routing agent-executed code to one of these external sandboxes, without worrying that a prompt injection attack or coding mistake could take damaging actions on their machine. The implementations are directly compatible with Pi, Claude Code, and Codex, and the optional proxy and credential replacement features give users fine-grained control over network access and authenticated API calls.

**Tags**: `#AI security`, `#prompt injection`, `#sandboxing`, `#coding agents`, `#LLM agents`

---

<a id="item-tech-news-11"></a>
### [China&\#x27;s Q/V-band ground test hits 27 Gbps with 512QAM](https://www.news.cn/tech/20261117/d6323540dccf4e2a976c48a762795956/c.html) ⭐️ 7.0/10

China&\#x27;s Aerospace Information Research Institute and partners completed a Q/V-band high-order modulation, high-code-rate bidirectional communication experiment at the Lijiang China Remote Sensing Satellite Ground Station, achieving the country&\#x27;s highest code rate in that band. The test systematically covered 64QAM to 512QAM for the first time; at 512QAM, a single channel reached 6.75 Gbps in each direction, and dual-carrier plus polarization multiplexing raised the aggregate to 27 Gbps, a domestic record. The team said key indicators are domestically leading and internationally advanced, and it plans to pursue more than 50 Gbps. The result is an experimental ground-station validation, not an in-orbit satellite link.

telegram · zaihuapd · Nov 17, 08:45

**「Background」** Q/V band \(roughly 40–50 GHz\) sits above the Ka band and offers wider spectrum for satellite links, but it suffers higher rain and atmospheric attenuation. High-order modulation such as 512QAM packs more bits per symbol, while dual-carrier and polarization multiplexing multiply capacity by using separate carriers and orthogonal polarizations. The Lijiang experiment tested these techniques together to push the domestic record, supporting research on 6G satellite interconnect.

**「Impact」** For 6G and high-throughput satellite research, the experiment provides a measured demonstration that Q/V-band ground equipment can sustain 27 Gbps using 512QAM with dual-carrier and polarization multiplexing, supporting the feasibility of future satellite-ground interconnect designs. The ground-station setting means the result does not yet prove performance over an actual satellite link, and the &\#x27;international advanced level&\#x27; characterization is the team&\#x27;s own assessment rather than an independently benchmarked comparison.

**Tags**: `#wireless-communication`, `#satellite-communication`, `#6G`, `#QV-band`, `#high-throughput-communication`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China to assess 17 automakers&\#x27; 60-day supplier payment terms](http://www.caam.org.cn/chn/5/cate_68/con_5237404.html) ⭐️ 7.0/10

China&\#x27;s Ministry of Industry and Information Technology has commissioned the China Association of Automobile Manufacturers to assess whether 17 major automakers, including BYD, Li Auto, NIO, XPeng, Xiaomi Auto and FAW, pay suppliers within 60 days, as required by the 2020 regulation protecting small and medium-sized enterprises. The evaluation, announced on Nov. 16, also checks that non-SME suppliers receive at least 80% of payments in cash or bank acceptance bills.

telegram · zaihuapd · Nov 18, 01:15

**「Background」** The evaluation follows a June 2025 pledge by at least 17 automakers, including FAW, GAC, Dongfeng, Geely, and BYD, to cut supplier payment terms to within 60 days after the Regulation on Guaranteeing Payment of Small and Medium Enterprises&\#x27; Funds took effect on June 1, 2025.

**「Impact」** If enforced, the assessment could improve cash flow for small and medium-sized auto parts suppliers, which often face long payment delays from large automakers.

<details><summary>References</summary>
<ul>
<li><a href="https://m.bjnews.com.cn/detail/1749644188168851.html">从“百日煎熬”到“ 60 天 承诺”： 车 企 账 期 瘦身，供应商解压</a></li>

</ul>
</details>

**Tags**: `#汽车行业`, `#政策监管`, `#供应链`, `#中小企业`, `#账期管理`

---