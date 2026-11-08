# 資源狀態與版本 / Resource status and versions

[繁體中文目錄](README.md) · [English catalog](README.en.md) · [來源紀錄](docs/curation.md)

本表由 `resources.json` 產生。更新資料後執行 `python3 check_catalog.py --write-status`。 / Generated from `resources.json`.

收錄 139 個來源 URL；其中 68 篇 arXiv 論文有 8 篇已找到正式出版紀錄，其餘明列未確認。 / 8 of 68 papers have verified publication records.

- 「未確認 / Unverified」表示未獨立確認正式出版狀態，不代表已被拒絕或沒有通過 peer review。
- Publisher index 表示核對官方搜尋索引中的出版 metadata；當時直接讀取頁面可能遇到 403 或 timeout。未進行論文結果重現。
- 未封存 / Not archived 不等於積極維護；release 為查核當日 GitHub `releases/latest` 的回傳值，並非部署建議。
- Living document 的內容會變更；導入前應另外 pin 實際採用的版本或 revision。
- Dates describe metadata checks, not continuous monitoring. Publication, release, and archive status can change.

## 論文出版狀態 / Publication status

| 論文 / Paper | 狀態 / Status | Venue | 證據 / Evidence | 查核日期 / Checked |
| --- | --- | --- | --- | --- |
| [Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2211.09527) | 2026-11-08 |
| [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2302.12173) | 2026-11-08 |
| [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2306.05499) | 2026-11-08 |
| [Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://arxiv.org/abs/2310.12815) | 已出版 / Published | USENIX Security 2024 | [Publisher](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei) (index) | 2026-11-08 |
| [InjecAgent](https://arxiv.org/abs/2403.02691) | 已出版 / Published | Findings of ACL 2024 | [Publisher](https://aclanthology.org/2024.findings-acl.624/) | 2026-11-08 |
| [AgentDojo](https://arxiv.org/abs/2406.13352) | 已出版 / Published | NeurIPS 2024 Datasets and Benchmarks | [Publisher](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) (index) | 2026-11-08 |
| [Agent Security Bench](https://arxiv.org/abs/2410.02644) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2410.02644) | 2026-11-08 |
| [ToolEmu](https://arxiv.org/abs/2309.15817) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2309.15817) | 2026-11-08 |
| [R-Judge](https://arxiv.org/abs/2401.10019) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2401.10019) | 2026-11-08 |
| [AgentHarm](https://arxiv.org/abs/2410.09024) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2410.09024) | 2026-11-08 |
| [WASP](https://arxiv.org/abs/2504.18575) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2504.18575) | 2026-11-08 |
| [BIPIA](https://arxiv.org/abs/2312.14197) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2312.14197) | 2026-11-08 |
| [MCPTox](https://arxiv.org/abs/2508.14925) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2508.14925) | 2026-11-08 |
| [Automatic and Universal Prompt Injection Attacks against Large Language Models](https://arxiv.org/abs/2403.04957) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2403.04957) | 2026-11-08 |
| [Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061) | 已出版 / Published | Findings of NAACL 2025 | [Publisher](https://aclanthology.org/2025.findings-naacl.395/) | 2026-11-08 |
| [The Attacker Moves Second](https://arxiv.org/abs/2510.09023) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2510.09023) | 2026-11-08 |
| [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2409.11295) | 2026-11-08 |
| [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2411.02391) | 2026-11-08 |
| [Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks](https://arxiv.org/abs/2502.08586) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2502.08586) | 2026-11-08 |
| [Why Are Web AI Agents More Vulnerable Than Standalone LLMs?](https://arxiv.org/abs/2502.20383) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2502.20383) | 2026-11-08 |
| [Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution](https://arxiv.org/abs/2506.01055) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2506.01055) | 2026-11-08 |
| [Dissecting Adversarial Robustness of Multimodal LM Agents](https://arxiv.org/abs/2406.12814) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2406.12814) | 2026-11-08 |
| [AgentPoison](https://arxiv.org/abs/2407.12784) | 已出版 / Published | NeurIPS 2024 | [Publisher](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html) (index) | 2026-11-08 |
| [Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2410.07283) | 2026-11-08 |
| [Agent Smith](https://arxiv.org/abs/2402.08567) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2402.08567) | 2026-11-08 |
| [Here Comes The AI Worm](https://arxiv.org/abs/2403.02817) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2403.02817) | 2026-11-08 |
| [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2503.18813) | 2026-11-08 |
| [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2506.08837) | 2026-11-08 |
| [Fides: Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2505.23643) | 2026-11-08 |
| [Progent: Securing AI Agents with Privilege Control](https://arxiv.org/abs/2504.11703) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2504.11703) | 2026-11-08 |
| [Spotlighting](https://arxiv.org/abs/2403.14720) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2403.14720) | 2026-11-08 |
| [StruQ](https://arxiv.org/abs/2402.06363) | 已出版 / Published | USENIX Security 2025 | [Publisher](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe) (index) | 2026-11-08 |
| [SecAlign](https://arxiv.org/abs/2410.05451) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2410.05451) | 2026-11-08 |
| [The Instruction Hierarchy](https://arxiv.org/abs/2404.13208) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2404.13208) | 2026-11-08 |
| [Jatmo](https://arxiv.org/abs/2312.17673) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2312.17673) | 2026-11-08 |
| [MELON](https://arxiv.org/abs/2502.05174) | 已出版 / Published | ICML 2025 / PMLR 267 | [Publisher](https://proceedings.mlr.press/v267/zhu25z.html) | 2026-11-08 |
| [Model Context Protocol: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2503.23278) | 2026-11-08 |
| [MCP Safety Audit](https://arxiv.org/abs/2504.03767) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2504.03767) | 2026-11-08 |
| [garak: A Framework for Security Probing Large Language Models](https://arxiv.org/abs/2406.11036) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2406.11036) | 2026-11-08 |
| [PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI System](https://arxiv.org/abs/2410.02828) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2410.02828) | 2026-11-08 |
| [Lessons from Defending Gemini Against Indirect Prompt Injections](https://arxiv.org/abs/2505.14534) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2505.14534) | 2026-11-08 |
| [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2307.02483) | 2026-11-08 |
| [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2307.15043) | 2026-11-08 |
| [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) | 已出版 / Published | NeurIPS 2024 | [Publisher](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f545448535dfde4f9786555403ab7c49-Abstract-Conference.html) | 2026-11-08 |
| [Shadow Alignment](https://arxiv.org/abs/2310.02949) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2310.02949) | 2026-11-08 |
| [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2310.03693) | 2026-11-08 |
| [BadLlama](https://arxiv.org/abs/2311.00117) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2311.00117) | 2026-11-08 |
| [Sleeper Agents](https://arxiv.org/abs/2401.05566) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2401.05566) | 2026-11-08 |
| [Emergent Misalignment](https://arxiv.org/abs/2502.17424) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2502.17424) | 2026-11-08 |
| [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2302.10149) | 2026-11-08 |
| [Scaling Trends for Data Poisoning in LLMs](https://arxiv.org/abs/2408.02946) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2408.02946) | 2026-11-08 |
| [Llama Guard](https://arxiv.org/abs/2312.06674) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2312.06674) | 2026-11-08 |
| [Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2607.08147) | 2026-11-08 |
| [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.09264) | 2026-11-08 |
| [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.14488) | 2026-11-08 |
| [The Agent Knew](https://arxiv.org/abs/2610.17301) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.17301) | 2026-11-08 |
| [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.18457) | 2026-11-08 |
| [Towards Safe Autonomy for Computer Use](https://arxiv.org/abs/2610.18508) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.18508) | 2026-11-08 |
| [Structured Authority Injection](https://arxiv.org/abs/2610.22373) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.22373) | 2026-11-08 |
| [The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection](https://arxiv.org/abs/2610.22594) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.22594) | 2026-11-08 |
| [From Approval to Abuse](https://arxiv.org/abs/2610.22987) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.22987) | 2026-11-08 |
| [Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems](https://arxiv.org/abs/2610.23078) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.23078) | 2026-11-08 |
| [Ignored, Not Refused](https://arxiv.org/abs/2610.23254) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.23254) | 2026-11-08 |
| [SPIDES: Information-Flow Control for Browser Agents](https://arxiv.org/abs/2610.24277) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.24277) | 2026-11-08 |
| [RATION: Towards Quantitative Risk-Based Access Control for AI Agents](https://arxiv.org/abs/2610.24311) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.24311) | 2026-11-08 |
| [SoK: PIAtlas](https://arxiv.org/abs/2610.24999) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.24999) | 2026-11-08 |
| [After the Attacker Leaves](https://arxiv.org/abs/2610.28425) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.28425) | 2026-11-08 |
| [Agentic AI Defense: Decode-Time Provenance Binding for MCP](https://arxiv.org/abs/2610.31974) | 未確認 / Unverified | — | [arXiv](https://arxiv.org/abs/2610.31974) | 2026-11-08 |

## 工具與模型 / Tools and models

| 資源 / Resource | 狀態 / Status | Release / revision | 發布或修改日期 / Date | 查核日期 / Checked |
| --- | --- | --- | --- | --- |
| [SPIRE](https://github.com/spiffe/spire) | 未封存 / Not archived | [v1.16.0](https://github.com/spiffe/spire/releases/tag/v1.16.0) | 2026-11-05 | 2026-11-08 |
| [OpenFGA](https://github.com/openfga/openfga) | 未封存 / Not archived | [v1.22.1](https://github.com/openfga/openfga/releases/tag/v1.22.1) | 2026-10-28 | 2026-11-08 |
| [Open Policy Agent](https://github.com/open-policy-agent/opa) | 未封存 / Not archived | [v1.22.2](https://github.com/open-policy-agent/opa/releases/tag/v1.22.2) | 2026-11-06 | 2026-11-08 |
| [OpenBao](https://github.com/openbao/openbao) | 未封存 / Not archived | [v2.7.2](https://github.com/openbao/openbao/releases/tag/v2.7.2) | 2026-10-26 | 2026-11-08 |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | 未封存 / Not archived | [v8.30.1](https://github.com/gitleaks/gitleaks/releases/tag/v8.30.1) | 2026-03-21 | 2026-11-08 |
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | 未封存 / Not archived | [v3.99.8](https://github.com/trufflesecurity/trufflehog/releases/tag/v3.99.8) | 2026-11-02 | 2026-11-08 |
| [gVisor](https://gvisor.dev/) | 未封存 / Not archived | [release-20261102.0](https://github.com/google/gvisor/releases/tag/release-20261102.0) | 2026-11-02 | 2026-11-08 |
| [Firecracker](https://firecracker-microvm.github.io/) | 未封存 / Not archived | [v1.17.0](https://github.com/firecracker-microvm/firecracker/releases/tag/v1.17.0) | 2026-09-10 | 2026-11-08 |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) | 未封存 / Not archived | [v0.1.7](https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.7) | 2026-11-03 | 2026-11-08 |
| [Sigstore Cosign](https://github.com/sigstore/cosign) | 未封存 / Not archived | [v3.1.4](https://github.com/sigstore/cosign/releases/tag/v3.1.4) | 2026-10-20 | 2026-11-08 |
| [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) | 未封存 / Not archived | [v0.165.0](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.165.0) | 2026-11-06 | 2026-11-08 |
| [Falco](https://github.com/falcosecurity/falco) | 未封存 / Not archived | [0.45.2](https://github.com/falcosecurity/falco/releases/tag/0.45.2) | 2026-10-29 | 2026-11-08 |
| [garak](https://github.com/NVIDIA/garak) | 未封存 / Not archived | [v0.17.1](https://github.com/NVIDIA/garak/releases/tag/v0.17.1) | 2026-10-16 | 2026-11-08 |
| [PyRIT](https://github.com/microsoft/PyRIT) | 未封存 / Not archived | [v1.1.0](https://github.com/microsoft/PyRIT/releases/tag/v1.1.0) | 2026-09-04 | 2026-11-08 |
| [promptfoo](https://github.com/promptfoo/promptfoo) | 未封存 / Not archived | [0.125.1](https://github.com/promptfoo/promptfoo/releases/tag/0.125.1) | 2026-10-25 | 2026-11-08 |
| [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 未封存 / Not archived | [v0.24.1](https://github.com/NVIDIA-NeMo/Guardrails/releases/tag/v0.24.1) | 2026-09-16 | 2026-11-08 |
| [Purple Llama](https://github.com/meta-llama/PurpleLlama) | 未封存 / Not archived | latest release 未取得 / Not available | — | 2026-11-08 |
| [Prompt Guard 86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) | 模型 revision / Model revision | `1209add6ca7d9c1d815171b8e5571587fe3e7b03` | 2025-11-12 | 2026-11-08 |

### 來源搬遷 / Source migrations

- [PyRIT](https://github.com/Azure/PyRIT) → [目前來源 / Current source](https://github.com/microsoft/PyRIT)。搬遷證據見 `resources.json`。

## 規格版本 / Specification versions

| 資源 / Resource | 版本 / Version | 查核日期 / Checked |
| --- | --- | --- |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | Living edition index; edition not pinned | 2026-11-08 |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | 2026 edition | 2026-11-08 |
| [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) | AI RMF 1.0 / AI 100-1 (2023) | 2026-11-08 |
| [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) | AI 600-1 (2024) | 2026-11-08 |
| [MCP Authorization, specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) | 2025-06-18 | 2026-11-08 |
| [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | 2026-07-28 | 2026-11-08 |
| [OAuth 2.0 Security Best Current Practice — RFC 9700](https://www.rfc-editor.org/rfc/rfc9700) | RFC 9700 / BCP 240 (2025) | 2026-11-08 |
| [Resource Indicators for OAuth 2.0 — RFC 8707](https://www.rfc-editor.org/rfc/rfc8707) | RFC 8707 (2020) | 2026-11-08 |
| [OAuth 2.0 Token Exchange — RFC 8693](https://www.rfc-editor.org/rfc/rfc8693) | RFC 8693 (2020) | 2026-11-08 |
| [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/) | Living specification overview | 2026-11-08 |
| [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) | Rolling documentation; deployment profile version not pinned | 2026-11-08 |
| [SLSA Specification v1.2](https://slsa.dev/spec/v1.2/) | SLSA v1.2 (Approved) | 2026-11-08 |
| [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) | Living conventions; verify per-field stability | 2026-11-08 |
| [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | SP 800-61 Rev. 3 (2025) | 2026-11-08 |

本表不包含所有文章的 metadata；完整來源清單與證據 URL 請查 `resources.json`。 / The JSON registry also includes the remaining references and evidence URLs.
