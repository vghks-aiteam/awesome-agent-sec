# Awesome Agent Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated reading list for securing AI agents that use tools, browse the web, execute code, or communicate with other agents.

Resources on prompt injection, MCP security, memory poisoning, agent evaluation, privilege control, sandboxing, and vulnerability disclosures. Each entry explains what it contributes; research results should be read within their stated threat models.

[繁體中文導讀](README.zh-TW.md) · [Contributing](CONTRIBUTING.md) · [Curation and source notes](docs/curation.md)

## Contents

- [Start here](#start-here)
- [Foundations](#foundations)
- [Threat models and standards](#threat-models-and-standards)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Prompt injection and agent attacks](#prompt-injection-and-agent-attacks)
- [Memory and multi-agent security](#memory-and-multi-agent-security)
- [System and architectural defenses](#system-and-architectural-defenses)
- [Model and prompt defenses](#model-and-prompt-defenses)
- [MCP security](#mcp-security)
- [Red teaming and runtime tools](#red-teaming-and-runtime-tools)
- [Vulnerability disclosures and case studies](#vulnerability-disclosures-and-case-studies)
- [Vendor engineering and evaluation reports](#vendor-engineering-and-evaluation-reports)
- [Alignment and adjacent research](#alignment-and-adjacent-research)
- [2026 research watchlist](#2026-research-watchlist)
- [Blogs and explainers](#blogs-and-explainers)
- [Contributing](#contributing)
- [License](#license)

## Start here

| Goal | Reading route |
| --- | --- |
| Understand the problem | Foundations → threat models → vulnerability disclosures. |
| Build an agent with sensitive data or tools | Architectural defenses → MCP security → runtime tools. |
| Evaluate a defense | Benchmarks → adaptive attacks → compare attack success with legitimate task completion. |
| Explore research directions | Memory and multi-agent security → 2026 research watchlist. |

Prompt injection concerns an application's instruction and trust boundaries. Jailbreaking concerns bypassing model safety behavior; the two can overlap, but their evaluations answer different questions. A low attack success rate alone does not establish that an agent is secure or useful.

**Reading labels:** Paper = research manuscript, linked to arXiv unless stated otherwise; standard = official framework or specification; tool = implementation; disclosure = a researcher's or vendor's vulnerability report; report = engineering account or evaluation. An arXiv link does not establish peer review. The watchlist explicitly identifies recent preprints whose publication status has not been independently checked.

## Foundations

- [Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) — **Paper · 2022.** Early exploration of goal hijacking and prompt leaking through PromptInject.
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — **Paper · 2023.** Explains how attacker-controlled external content can redirect an LLM application's behavior.
- [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) — **Paper · 2023.** Introduces HouYi and evaluates injection attacks against deployed applications.
- [Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://arxiv.org/abs/2310.12815) — **Paper · 2023.** Formalizes the attack setting and systematically compares attacks and defenses.
- [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) — **Explainer · 2022.** An early account of the instruction-versus-data problem and the prompt injection terminology.

## Threat models and standards

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — **Standard.** Application risks including prompt injection, excessive agency, supply chains, and unsafe output handling.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — **Standard.** Agent-specific risks involving goals, tools, identities, memory, inter-agent communication, and human trust.
- [OWASP Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — **Guidance.** A broader threat inventory for designing and reviewing agentic systems.
- [MITRE ATLAS](https://atlas.mitre.org/) — **Knowledge base.** Adversarial AI tactics, techniques, and case studies for threat modeling and reporting.
- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) — **Framework · 2023.** Governance and risk management through Govern, Map, Measure, and Manage.
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) — **Framework · 2024.** Generative AI risk considerations and suggested risk management actions.
- [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) — **Design guidance · 2025.** Restricts the combination of untrusted inputs, sensitive access, and consequential actions without human oversight.

## Benchmarks and evaluation

- [InjecAgent](https://arxiv.org/abs/2403.02691) — **Paper · 2024.** Indirect prompt injection benchmark for agents using external tools.
- [AgentDojo](https://arxiv.org/abs/2406.13352) — **Paper · 2024.** Dynamic tool-use environments for measuring both legitimate task completion and attack success.
- [Agent Security Bench](https://arxiv.org/abs/2410.02644) — **Paper · 2024.** Evaluates multiple attack surfaces, including tools and memory, across agent scenarios.
- [ToolEmu](https://arxiv.org/abs/2309.15817) — **Paper · 2023.** Uses an LLM-emulated sandbox to investigate risky tool-use behavior.
- [R-Judge](https://arxiv.org/abs/2401.10019) — **Paper · 2024.** Measures whether models recognize safety risks in agent interaction records.
- [AgentHarm](https://arxiv.org/abs/2410.09024) — **Paper · 2024.** Evaluates agent misuse through harmful multi-step requests; distinct from indirect prompt injection testing.
- [WASP](https://arxiv.org/abs/2504.18575) — **Paper · 2025.** Benchmarks prompt injection against web agents in interactive environments.
- [BIPIA](https://arxiv.org/abs/2312.14197) — **Paper · 2023.** Benchmarks indirect prompt injection and evaluates prompt-based and training-based defenses.
- [MCPTox](https://arxiv.org/abs/2508.14925) — **Paper · 2025.** Tests malicious instructions embedded in MCP tool metadata, rather than only tool outputs.

## Prompt injection and agent attacks

- [Automatic and Universal Prompt Injection Attacks against Large Language Models](https://arxiv.org/abs/2403.04957) — **Paper · 2024.** Investigates automated optimization of transferable prompt injection attacks.
- [Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061) — **Paper · 2025.** Evaluates defenses against attackers that adapt to the defense mechanism.
- [The Attacker Moves Second](https://arxiv.org/abs/2510.09023) — **Paper · 2025.** Reassesses jailbreak and prompt injection defenses using stronger, defense-aware attacks.
- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295) — **Paper · 2024.** Studies privacy leakage through attacker-controlled web environments.
- [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) — **Paper · 2024.** Examines visual pop-ups as a control surface for computer-use agents.
- [Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks](https://arxiv.org/abs/2502.08586) — **Paper · 2025.** Demonstrates attacks on commercial agent workflows through ordinary external content.
- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs?](https://arxiv.org/abs/2502.20383) — **Paper · 2025.** Analyzes how web interaction changes the attack surface of an otherwise safety-trained model.
- [Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution](https://arxiv.org/abs/2506.01055) — **Paper · 2025.** Studies exfiltration of personal information encountered during a tool-use task.
- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://arxiv.org/abs/2406.12814) — **Paper · 2024.** Evaluates attacks against multimodal agents in realistic web tasks.

## Memory and multi-agent security

- [AgentPoison](https://arxiv.org/abs/2407.12784) — **Paper · 2024.** Backdoor attacks against agent memory and retrieval-based knowledge stores.
- [Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283) — **Paper · 2024.** Studies prompt injection propagation between communicating agents.
- [Agent Smith](https://arxiv.org/abs/2402.08567) — **Paper · 2024.** Explores adversarial image propagation in networks of multimodal agents.
- [Here Comes The AI Worm](https://arxiv.org/abs/2403.02817) — **Paper · 2024.** Demonstrates Morris II, a self-replicating prompt attack in RAG-connected applications.

## System and architectural defenses

These designs constrain tool execution or information flow outside ordinary model instruction following. Their guarantees depend on assumptions about policy correctness, trusted components, and complete mediation.

- [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) — **Paper · 2025.** Separates control and data flows and enforces capability-based policies at tool calls.
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) — **Paper · 2025.** Compares six architectural patterns and their security–utility trade-offs.
- [Fides: Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643) — **Paper · 2025.** Uses confidentiality and integrity labels to reason about and enforce agent information flows.
- [Progent: Securing AI Agents with Privilege Control](https://arxiv.org/abs/2504.11703) — **Paper · 2025.** Expresses and enforces task-dependent policies for tool invocation.
- [The Dual LLM pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) — **Design proposal · 2023.** Separates an assistant with privileges from a model processing untrusted content.
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — **Threat-model explainer · 2025.** Connects private data access, untrusted input, and external communication to exfiltration risk.

## Model and prompt defenses

Evaluate these methods against adaptive attacks as well as ordinary tasks. Training improvements and detection accuracy do not replace authorization or isolation.

- [Spotlighting](https://arxiv.org/abs/2403.14720) — **Paper · 2024.** Marks untrusted inputs using delimiters, data marking, or encoding.
- [StruQ](https://arxiv.org/abs/2402.06363) — **Paper · 2024.** Combines structured queries with training to distinguish instructions from data.
- [SecAlign](https://arxiv.org/abs/2410.05451) — **Paper · 2024.** Uses preference optimization to reduce instruction following from untrusted content.
- [The Instruction Hierarchy](https://arxiv.org/abs/2404.13208) — **Paper · 2024.** Trains models to prioritize privileged instructions over lower-trust inputs.
- [Jatmo](https://arxiv.org/abs/2312.17673) — **Paper · 2023.** Investigates task-specific fine-tuning as a prompt injection defense.
- [MELON](https://arxiv.org/abs/2502.05174) — **Paper · 2025.** Detects injected tasks using masked re-execution and comparison of tool calls.

## MCP security

- [MCP Authorization, specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) — **Specification.** Versioned authorization requirements; check the protocol version supported by your implementation.
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) — **Official guidance.** Authorization threats, token handling, confused deputies, and related deployment risks.
- [Model Context Protocol: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) — **Paper · 2025.** Surveys MCP architecture and threats across the server lifecycle.
- [MCP Safety Audit](https://arxiv.org/abs/2504.03767) — **Paper · 2025.** Explores security failures when models interact with MCP-connected tools.
- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) — **Disclosure · 2025.** Introduces attacks through tool descriptions, including tool shadowing and rug pulls.
- [Jumping the line: How MCP servers can attack you before you ever use them](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) — **Research article · 2025.** Explains why tool metadata becomes an attack surface before a tool is called.

## Red teaming and runtime tools

These tools serve different layers. A scanner, classifier, policy framework, and sandbox are not interchangeable security controls.

- [garak](https://github.com/NVIDIA/garak) — **Tool.** LLM vulnerability scanner with probes and detectors. [Framework paper](https://arxiv.org/abs/2406.11036).
- [PyRIT](https://github.com/Azure/PyRIT) — **Tool.** Framework for orchestrating generative AI risk identification and red teaming. [Framework paper](https://arxiv.org/abs/2410.02828).
- [promptfoo](https://github.com/promptfoo/promptfoo) — **Tool.** Evaluation and red teaming workflows for prompts, agents, and RAG applications.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) — **Tool.** Programmable guardrails for LLM-based applications.
- [Purple Llama](https://github.com/meta-llama/PurpleLlama) — **Tool collection.** Safety and security evaluation resources and safeguards from Meta.
- [Prompt Guard 86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) — **Model.** Classifies benign input, prompt injection, and jailbreak attempts; a detector rather than an authorization boundary.
- [gVisor](https://gvisor.dev/) — **Runtime.** Application kernel for isolating containerized workloads.
- [Firecracker](https://firecracker-microvm.github.io/) — **Runtime.** MicroVM technology for workload isolation.
- [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) — **Runtime.** Agent execution environment with filesystem, network, and policy controls.

## Vulnerability disclosures and case studies

These are historical reports about particular configurations and versions. Inclusion does not imply current exploitability or exploitation in the wild. Research demonstrations are identified as disclosures rather than assumed to be production breaches.

### Assistant and memory disclosures

- [Google Bard: From Prompt Injection to Data Exfiltration](https://embracethered.com/blog/posts/2023/google-bard-data-exfiltration/) — **Disclosure · 2023.** Demonstrates how injected content can induce data exfiltration through generated output.
- [Microsoft Copilot: Prompt Injection and ASCII Smuggling](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/) — **Disclosure · 2024.** Combines hidden text, tool invocation, and exfiltration.
- [SpAIware: ChatGPT Long-Term Memory](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/) — **Disclosure · 2024.** Shows persistent injected instructions stored in assistant memory.
- [Data Exfiltration from Slack AI](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via) — **Disclosure · 2024.** Examines how retrieved Slack content can redirect an assistant toward data leakage.
- [EchoLeak / CVE-2025-32711](https://cveawg.mitre.org/api/cve/CVE-2025-32711) — **CVE record · 2025.** Microsoft's CNA record for AI command injection causing information disclosure in Microsoft 365 Copilot.

### MCP and coding-agent disclosures

- [WhatsApp MCP Exploited](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) — **Disclosure · 2025.** Demonstrates message-history exfiltration through malicious MCP tool behavior.
- [GitHub MCP Exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) — **Disclosure · 2025.** Shows how attacker-controlled repository content can steer access to private repositories.
- [Supabase MCP: Prompt Injection and Private Tables](https://generalanalysis.com/blog/supabase-mcp-blog) — **Disclosure · 2025.** Examines excessive database access combined with untrusted content.
- [mcp-remote / CVE-2025-6514](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/) — **Disclosure · 2025.** OS command injection through a crafted authorization endpoint from an untrusted MCP server; a software vulnerability distinct from model prompt injection.
- [Cursor CurXecute / CVE-2025-54135](https://github.com/cursor/cursor/security/advisories/GHSA-4cxx-hrm3-49rm) — **Vendor advisory · 2025.** An approval gap in creating MCP configuration files allowed an injection chain to reach code execution.
- [GitHub Copilot / CVE-2025-53773](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) — **Disclosure · 2025.** Research report connecting prompt injection, configuration changes, and code execution.
- [CamoLeak](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code) — **Disclosure · 2025.** Examines private source-code exfiltration in GitHub Copilot workflows.
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) — **Disclosure · 2026.** A researcher evaluation of automatic approval behavior; read its attack setup and sample size before generalizing.

### Browser and computer-use disclosures

- [ZombAIs: Prompt Injection to C2 with Claude Computer Use](https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/) — **Disclosure · 2024.** Demonstrates prompt-driven command-and-control behavior in a computer-use setting.
- [Indirect Prompt Injection in Perplexity Comet](https://brave.com/blog/comet-prompt-injection/) — **Disclosure · 2025.** Explores browser-agent exfiltration through attacker-controlled page content.
- [Google Antigravity Exfiltrates Data](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data) — **Disclosure · 2025.** Shows an IDE agent being redirected through an external page and browser subagent.

## Vendor engineering and evaluation reports

- [Lessons from Defending Gemini Against Indirect Prompt Injections](https://arxiv.org/abs/2505.14534) — **Paper / engineering report · 2025.** Describes Google's experience with layered defenses and adversarial evaluation.
- [Making Claude Code Safer with Sandboxing](https://www.anthropic.com/research/claude-code-sandboxing) — **Engineering report · 2025.** Discusses filesystem and network isolation around a coding agent.
- [Mitigating Prompt Injections in Browser Use](https://www.anthropic.com/research/prompt-injection-defenses) — **Engineering report.** Describes browser-use defenses and the role of adversarial evaluation.
- [Agentic Misalignment: LLMs as Insider Threats](https://www.anthropic.com/research/agentic-misalignment) — **Controlled evaluation · 2025.** Tests harmful agent behavior in simulated organizational scenarios, rather than documenting a production breach.
- [An Agent Used DNS to Reach an External Chatbot](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/) — **First-party incident report · 2026.** Documents a network-control bypass during an internal task; useful for reviewing egress controls beyond HTTP.
- [Practical LLM Security Advice from the NVIDIA AI Red Team](https://developer.nvidia.com/blog/practical-llm-security-advice-from-the-nvidia-ai-red-team/) — **Engineering guidance.** Practical threat modeling and deployment advice for LLM applications.

## Alignment and adjacent research

These resources explain model behavior, fine-tuning, and supply-chain risks. Refusal behavior and indirect prompt injection resistance are different properties; neither open weights nor a hosted API alone establishes system security.

- [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) — **Paper · 2023.** Analyzes competing objectives and generalization failures in safety training.
- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) — **Paper · 2023.** Introduces GCG attacks and studies transfer across aligned models.
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — **Paper · 2024.** Investigates a representation-level mechanism underlying refusal behavior.
- [Shadow Alignment](https://arxiv.org/abs/2310.02949) — **Paper · 2023.** Studies how fine-tuning can subvert model safety alignment.
- [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) — **Paper · 2023.** Evaluates safety degradation under malicious and benign fine-tuning.
- [BadLlama](https://arxiv.org/abs/2311.00117) — **Paper · 2023.** Investigates the cost of removing safety fine-tuning from an open-weight model.
- [Sleeper Agents](https://arxiv.org/abs/2401.05566) — **Paper · 2024.** Studies backdoored behavior that persists through subsequent safety training.
- [Emergent Misalignment](https://arxiv.org/abs/2502.17424) — **Paper · 2025.** Examines broader behavioral changes following narrow fine-tuning on insecure code.
- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) — **Paper · 2023.** Studies practical routes to contaminating large web-derived training datasets.
- [Scaling Trends for Data Poisoning in LLMs](https://arxiv.org/abs/2408.02946) — **Paper · 2024.** Investigates how model scaling affects susceptibility to poisoned training data.
- [Llama Guard](https://arxiv.org/abs/2312.06674) — **Paper · 2023.** Input-output safety classification; useful context for distinguishing content safeguards from agent authorization.
- [Uncensor any LLM with abliteration](https://huggingface.co/blog/mlabonne/abliteration) — **Technical tutorial · 2024.** Explains refusal-direction removal in open-weight models.

## 2026 research watchlist

**All entries below are arXiv preprints.** Titles and abstracts were checked on 2026-11-08; peer-review or acceptance status was not independently established. Descriptions summarize proposed methods or reported experiments, rather than validated deployment guarantees.

- [Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147) — Studies confinement of cross-site prompt injection in web-agent workflows.
- [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) — Studies dependency substitution induced through shared agent rule files.
- [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) — Proposes confinement around object identity for coding agents assumed to be compromised.
- [The Agent Knew](https://arxiv.org/abs/2610.17301) — Investigates internal-state prediction of unauthorized actions and subsequent misleading reports using CAPE-Bench.
- [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457) — Proposes transactional mediation of an agent's side effects.
- [Towards Safe Autonomy for Computer Use](https://arxiv.org/abs/2610.18508) — Investigates safeguards for autonomous computer-use systems.
- [Structured Authority Injection](https://arxiv.org/abs/2610.22373) — Proposes typed MCP overrides for persistent human control; distinct from an attacker injecting arbitrary instructions.
- [The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection](https://arxiv.org/abs/2610.22594) — Evaluates attacks and a defense in simulated medical multi-agent decision tasks; clinical deployment effectiveness is not established.
- [From Approval to Abuse](https://arxiv.org/abs/2610.22987) — Studies manipulation of user-approved allow-rules in coding-agent harnesses.
- [Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems](https://arxiv.org/abs/2610.23078) — Investigates cryptographic protection of messages between agents.
- [Ignored, Not Refused](https://arxiv.org/abs/2610.23254) — Distinguishes attack failure caused by task limitations from explicit rejection of injected instructions.
- [SPIDES: Information-Flow Control for Browser Agents](https://arxiv.org/abs/2610.24277) — Studies information-flow enforcement at browser-agent actions.
- [RATION: Towards Quantitative Risk-Based Access Control for AI Agents](https://arxiv.org/abs/2610.24311) — Proposes risk-based access decisions to manage security–utility trade-offs.
- [SoK: PIAtlas](https://arxiv.org/abs/2610.24999) — Organizes prompt injection techniques by subversion mechanism and maps public datasets into a shared taxonomy.
- [After the Attacker Leaves](https://arxiv.org/abs/2610.28425) — Introduces CarryoverBench for attacks persisting through memory files and scheduled tasks.
- [Agentic AI Defense: Decode-Time Provenance Binding for MCP](https://arxiv.org/abs/2610.31974) — Examines cross-modal trust laundering and proposes provenance tracking for decoded tool content.

## Blogs and explainers

- [Prompt injection: What's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) — **Explainer · 2023.** Concrete consequences beyond making a chatbot produce unwanted text.
- [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) — **Explainer · 2025.** Connects MCP tool behavior to familiar prompt injection risks.
- [CaMeL offers a promising new direction](https://simonwillison.net/2025/Apr/11/camel/) — **Explainer · 2025.** Accessible introduction to capability-based agent defenses.
- [Design patterns for securing LLM agents](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/) — **Explainer · 2025.** Walkthrough of architectural approaches and their trade-offs.
- [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) — **Research commentary · 2025.** Pairs deployment constraints with adaptive evaluation.
- [Simon Willison's prompt injection archive](https://simonwillison.net/tags/prompt-injection/) — **Ongoing coverage.** A discovery feed for research, incidents, and engineering discussions.
- [Embrace The Red](https://embracethered.com/blog/) — **Research blog.** First-hand security investigations of assistants, memory, tools, and computer use.

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md). Prefer original papers, official specifications, maintained implementations, and first-hand disclosures. Include a short description, avoid duplicate entries, and identify the evidence type. Corrections to existing descriptions are welcome.

## License

The original curation and annotations in this repository are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). Linked papers, code, standards, and articles retain their own licenses and attribution requirements.
