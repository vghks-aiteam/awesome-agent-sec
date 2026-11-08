# Awesome Agent Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI agent 安全資源精選：涵蓋工具使用、網頁瀏覽、程式碼執行與跨 agent 通訊。

整理 prompt injection、MCP 安全、memory poisoning、agent 評測、權限控制、sandbox 與漏洞揭露。每筆資源附上用途與貢獻說明；閱讀研究結果時，請一併檢視其 threat model 與適用條件。

[English](README.en.md) · [繁體中文導讀](README.zh-TW.md) · [參與維護](CONTRIBUTING.md) · [整理與來源紀錄](docs/curation.md)

## 目錄

- [從這裡開始](#從這裡開始)
- [基礎概念](#基礎概念)
- [威脅模型與標準](#威脅模型與標準)
- [Benchmark 與評測](#benchmark-與評測)
- [Prompt injection 與 agent 攻擊](#prompt-injection-與-agent-攻擊)
- [記憶與 multi-agent 安全](#記憶與-multi-agent-安全)
- [系統與架構層防禦](#系統與架構層防禦)
- [模型與 prompt 層防禦](#模型與-prompt-層防禦)
- [MCP 安全](#mcp-安全)
- [紅隊與執行環境工具](#紅隊與執行環境工具)
- [漏洞揭露與案例研究](#漏洞揭露與案例研究)
- [廠商工程與評估報告](#廠商工程與評估報告)
- [Alignment 與相關研究](#alignment-與相關研究)
- [2026 年研究追蹤](#2026-年研究追蹤)
- [部落格與導讀](#部落格與導讀)
- [參與維護](#參與維護)
- [授權](#授權)

## 從這裡開始

| 你的目標 | 建議閱讀順序 |
| --- | --- |
| 理解問題 | 基礎概念 → 威脅模型與標準 → 漏洞揭露與案例研究。 |
| 開發能存取敏感資料或工具的 agent | 系統與架構層防禦 → MCP 安全 → 紅隊與執行環境工具。 |
| 評估防禦方法 | Benchmark 與評測 → adaptive attack → 同時比較攻擊成功率與正常任務完成率。 |
| 探索研究方向 | 記憶與 multi-agent 安全 → 2026 年研究追蹤。 |

Prompt injection 關心應用程式的指令與信任邊界；jailbreak 關心繞過模型的安全行為。兩者可能重疊，但評測所回答的問題不同。僅有較低的攻擊成功率，無法證明 agent 既安全又能完成任務。

**資源標示：**論文預設連到 arXiv；標準指官方框架或規格；工具指實作；研究揭露指研究者或廠商的漏洞報告；報告指工程實務或評估。arXiv 連結不代表已通過 peer review。研究追蹤區另行標示尚未獨立確認正式出版狀態的近期 preprint。

## 基礎概念

- [Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) — **論文 · 2022**。透過 PromptInject 探索早期的 goal hijacking 與 prompt leaking 攻擊。
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — **論文 · 2023**。說明攻擊者如何透過受其控制的外部內容，改變 LLM 應用程式的行為。
- [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) — **論文 · 2023**。提出 HouYi，並對已部署的 LLM 應用程式評估 prompt injection 攻擊。
- [Formalizing and Benchmarking Prompt Injection Attacks and Defenses](https://arxiv.org/abs/2310.12815) — **論文 · 2023**。形式化定義攻擊情境，並系統性比較不同攻擊與防禦。
- [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) — **導讀 · 2022**。介紹指令與資料混合的問題，以及 prompt injection 一詞的早期脈絡。

## 威脅模型與標準

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — **標準**。涵蓋 prompt injection、excessive agency、供應鏈與不安全的輸出處理等應用風險。
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — **標準**。整理 agent 的目標、工具、身分、記憶、跨 agent 通訊與人類信任等風險。
- [OWASP Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — **指引**。提供較完整的 agentic 系統威脅清單，適合用於設計與安全審查。
- [MITRE ATLAS](https://atlas.mitre.org/) — **知識庫**。整理對抗式 AI 的 tactics、techniques 與案例，供 threat modeling 與安全報告使用。
- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) — **框架 · 2023**。以 Govern、Map、Measure、Manage 四個功能組織 AI 治理與風險管理。
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) — **框架 · 2024**。提供 generative AI 的風險考量與建議管理措施。
- [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) — **設計指引 · 2025**。限制缺乏人類監督時，不可信輸入、敏感資料存取與重大影響動作的組合。

## Benchmark 與評測

- [InjecAgent](https://arxiv.org/abs/2403.02691) — **論文 · 2024**。評測使用外部工具的 agent 面對 indirect prompt injection 時的表現。
- [AgentDojo](https://arxiv.org/abs/2406.13352) — **論文 · 2024**。提供動態工具使用環境，同時量測正常任務完成率與攻擊成功率。
- [Agent Security Bench](https://arxiv.org/abs/2410.02644) — **論文 · 2024**。在多種 agent 情境中評估工具、記憶等不同攻擊面。
- [ToolEmu](https://arxiv.org/abs/2309.15817) — **論文 · 2023**。使用 LLM 模擬工具執行的 sandbox，探索高風險的工具使用行為。
- [R-Judge](https://arxiv.org/abs/2401.10019) — **論文 · 2024**。量測模型能否從 agent 的互動紀錄辨識安全風險。
- [AgentHarm](https://arxiv.org/abs/2410.09024) — **論文 · 2024**。以有害的多步驟請求評估 agent 濫用風險，評測目標與 indirect prompt injection 不同。
- [WASP](https://arxiv.org/abs/2504.18575) — **論文 · 2025**。在可互動的環境中，評測 web agent 面對 prompt injection 的表現。
- [BIPIA](https://arxiv.org/abs/2312.14197) — **論文 · 2023**。提供 indirect prompt injection benchmark，並評估 prompt 與訓練層的防禦。
- [MCPTox](https://arxiv.org/abs/2508.14925) — **論文 · 2025**。測試嵌入 MCP tool metadata 的惡意指令，將評測範圍延伸至工具描述。

## Prompt injection 與 agent 攻擊

- [Automatic and Universal Prompt Injection Attacks against Large Language Models](https://arxiv.org/abs/2403.04957) — **論文 · 2024**。研究如何自動最佳化可轉移的 prompt injection 攻擊。
- [Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents](https://arxiv.org/abs/2503.00061) — **論文 · 2025**。以會針對防禦機制調整策略的 adaptive attacker，重新評估防禦效果。
- [The Attacker Moves Second](https://arxiv.org/abs/2510.09023) — **論文 · 2025**。使用更強、了解防禦機制的攻擊，重新檢驗 jailbreak 與 prompt injection 防禦。
- [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://arxiv.org/abs/2409.11295) — **論文 · 2024**。研究攻擊者控制的網頁環境如何造成隱私資料外洩。
- [Attacking Vision-Language Computer Agents via Pop-ups](https://arxiv.org/abs/2411.02391) — **論文 · 2024**。探索視覺彈窗如何成為操控 computer-use agent 的入口。
- [Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks](https://arxiv.org/abs/2502.08586) — **論文 · 2025**。展示如何透過一般外部內容，攻擊商用 agent 的工作流程。
- [Why Are Web AI Agents More Vulnerable Than Standalone LLMs?](https://arxiv.org/abs/2502.20383) — **論文 · 2025**。分析網頁互動如何改變已接受安全訓練之模型的攻擊面。
- [Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution](https://arxiv.org/abs/2506.01055) — **論文 · 2025**。研究如何讓 agent 外洩執行工具任務時接觸到的個人資料。
- [Dissecting Adversarial Robustness of Multimodal LM Agents](https://arxiv.org/abs/2406.12814) — **論文 · 2024**。在擬真的網頁任務中，評估針對 multimodal agent 的攻擊。

## 記憶與 multi-agent 安全

- [AgentPoison](https://arxiv.org/abs/2407.12784) — **論文 · 2024**。研究針對 agent 記憶與 retrieval-based knowledge store 的 backdoor 攻擊。
- [Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283) — **論文 · 2024**。研究 prompt injection 如何在互相通訊的 agent 之間傳播。
- [Agent Smith](https://arxiv.org/abs/2402.08567) — **論文 · 2024**。探索對抗式圖片在 multimodal agent 網路中的傳播。
- [Here Comes The AI Worm](https://arxiv.org/abs/2403.02817) — **論文 · 2024**。展示 Morris II：透過 RAG 連接的應用程式傳播、自我複製的 prompt 攻擊。

## 系統與架構層防禦

這些設計在模型的指令遵循機制之外，限制工具執行或資訊流。其安全保證仍依賴政策正確、可信元件可靠，以及所有敏感操作都經過中介檢查等前提。

- [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) — **論文 · 2025**。分離控制流與資料流，並在工具呼叫時強制執行 capability-based policy。
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) — **論文 · 2025**。比較六種架構模式，以及它們在安全性與功能之間的取捨。
- [Fides: Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643) — **論文 · 2025**。使用 confidentiality 與 integrity label，推理並限制 agent 的資訊流。
- [Progent: Securing AI Agents with Privilege Control](https://arxiv.org/abs/2504.11703) — **論文 · 2025**。表達並強制執行隨任務情境調整的工具呼叫政策。
- [The Dual LLM pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) — **設計提案 · 2023**。將持有權限的助理，與處理不可信內容的模型分開。
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — **威脅模型導讀 · 2025**。說明私有資料存取、不可信輸入與對外通訊如何共同形成資料外洩風險。

## 模型與 prompt 層防禦

評估這些方法時，需同時測試正常任務與 adaptive attack。訓練改善與偵測準確率，仍需搭配 authorization 與 isolation。

- [Spotlighting](https://arxiv.org/abs/2403.14720) — **論文 · 2024**。以 delimiter、data marking 或 encoding 標示不可信輸入。
- [StruQ](https://arxiv.org/abs/2402.06363) — **論文 · 2024**。結合 structured query 與訓練，讓模型區分指令與資料。
- [SecAlign](https://arxiv.org/abs/2410.05451) — **論文 · 2024**。使用 preference optimization，降低模型遵循不可信內容中指令的機率。
- [The Instruction Hierarchy](https://arxiv.org/abs/2404.13208) — **論文 · 2024**。訓練模型優先遵循高權限指令，而非較低信任層級的輸入。
- [Jatmo](https://arxiv.org/abs/2312.17673) — **論文 · 2023**。研究以任務專用的 fine-tuning 防禦 prompt injection。
- [MELON](https://arxiv.org/abs/2502.05174) — **論文 · 2025**。透過 masked re-execution 與工具呼叫比較，偵測被注入的任務。

## MCP 安全

- [MCP Authorization, specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) — **規格**。保留版本的 authorization 要求；實作時需確認採用的 protocol 版本。
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) — **官方指引**。涵蓋 authorization 威脅、token 處理、confused deputy 與部署風險。
- [Model Context Protocol: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) — **論文 · 2025**。整理 MCP 架構，以及 server 生命週期中的安全威脅。
- [MCP Safety Audit](https://arxiv.org/abs/2504.03767) — **論文 · 2025**。探索模型與 MCP 工具互動時的安全失效情境。
- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) — **研究揭露 · 2025**。介紹透過工具描述發動的攻擊，包括 tool shadowing 與 rug pull。
- [Jumping the line: How MCP servers can attack you before you ever use them](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) — **研究文章 · 2025**。說明為什麼在工具被呼叫之前，tool metadata 就已經成為攻擊面。

## 紅隊與執行環境工具

這些工具作用於不同層次；scanner、classifier、policy framework 與 sandbox 各有用途，不能互相替代。

- [garak](https://github.com/NVIDIA/garak) — **工具**。提供 probes 與 detectors 的 LLM 弱點掃描器。[論文](https://arxiv.org/abs/2406.11036)。
- [PyRIT](https://github.com/Azure/PyRIT) — **工具**。用於組織 generative AI 風險辨識與紅隊測試的框架。[論文](https://arxiv.org/abs/2410.02828)。
- [promptfoo](https://github.com/promptfoo/promptfoo) — **工具**。提供 prompt、agent 與 RAG 應用程式的評測及紅隊測試流程。
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) — **工具**。為 LLM 應用程式加入可程式化的 guardrail。
- [Purple Llama](https://github.com/meta-llama/PurpleLlama) — **工具集**。Meta 提供的安全評測資源與防護工具。
- [Prompt Guard 86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) — **模型**。分類一般輸入、prompt injection 與 jailbreak 嘗試；屬於偵測器，不能視為授權邊界。
- [gVisor](https://gvisor.dev/) — **執行環境**。以 application kernel 隔離 container 中的工作負載。
- [Firecracker](https://firecracker-microvm.github.io/) — **執行環境**。用於隔離工作負載的 microVM 技術。
- [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) — **執行環境**。為 agent 提供檔案系統、網路與政策控制。

## 漏洞揭露與案例研究

以下報告涉及特定設定與歷史版本。收錄不代表目前仍可利用，也不代表已遭實際攻擊。受控的研究展示以「研究揭露」標示，並與真實系統入侵事件區分。

### 助理與記憶相關揭露

- [Google Bard: From Prompt Injection to Data Exfiltration](https://embracethered.com/blog/posts/2023/google-bard-data-exfiltration/) — **研究揭露 · 2023**。展示注入內容如何透過模型產生的輸出誘發資料外洩。
- [Microsoft Copilot: Prompt Injection and ASCII Smuggling](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/) — **研究揭露 · 2024**。結合隱藏文字、工具呼叫與資料外送。
- [SpAIware: ChatGPT Long-Term Memory](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/) — **研究揭露 · 2024**。展示注入指令如何儲存在助理記憶中並持續生效。
- [Data Exfiltration from Slack AI](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via) — **研究揭露 · 2024**。探索被檢索的 Slack 內容如何讓助理轉向資料外洩行為。
- [EchoLeak / CVE-2025-32711](https://cveawg.mitre.org/api/cve/CVE-2025-32711) — **CVE 記錄 · 2025**。Microsoft 的 CNA 記錄，描述 Microsoft 365 Copilot 中造成資訊洩漏的 AI command injection。

### MCP 與 coding agent 相關揭露

- [WhatsApp MCP Exploited](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) — **研究揭露 · 2025**。展示惡意 MCP 工具行為如何外洩訊息歷史。
- [GitHub MCP Exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) — **研究揭露 · 2025**。展示攻擊者控制的 repository 內容如何誘導 agent 存取私有 repository。
- [Supabase MCP: Prompt Injection and Private Tables](https://generalanalysis.com/blog/supabase-mcp-blog) — **研究揭露 · 2025**。探索過大的資料庫權限與不可信內容結合時的風險。
- [mcp-remote / CVE-2025-6514](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/) — **研究揭露 · 2025**。不可信 MCP server 回傳的特製 authorization endpoint 可觸發 OS command injection，屬於軟體弱點，需與模型 prompt injection 區分。
- [Cursor CurXecute / CVE-2025-54135](https://github.com/cursor/cursor/security/advisories/GHSA-4cxx-hrm3-49rm) — **廠商公告 · 2025**。建立 MCP 設定檔時的核准缺口，讓 prompt injection 攻擊鏈進一步造成程式碼執行。
- [GitHub Copilot / CVE-2025-53773](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) — **研究揭露 · 2025**。研究報告說明 prompt injection、設定變更與程式碼執行之間的攻擊鏈。
- [CamoLeak](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code) — **研究揭露 · 2025**。探索 GitHub Copilot 工作流程中的私有原始碼外洩。
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) — **研究揭露 · 2026**。研究者對自動核准行為的評估；推廣結論前，需先閱讀攻擊設定與樣本數。

### 瀏覽器與 computer-use 相關揭露

- [ZombAIs: Prompt Injection to C2 with Claude Computer Use](https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/) — **研究揭露 · 2024**。在 computer-use 情境中，展示由 prompt 驅動的 command-and-control 行為。
- [Indirect Prompt Injection in Perplexity Comet](https://brave.com/blog/comet-prompt-injection/) — **研究揭露 · 2025**。探索攻擊者控制的頁面內容如何誘發 browser agent 外洩資料。
- [Google Antigravity Exfiltrates Data](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data) — **研究揭露 · 2025**。展示外部網頁如何透過 browser subagent 改變 IDE agent 的行為。

## 廠商工程與評估報告

- [Lessons from Defending Gemini Against Indirect Prompt Injections](https://arxiv.org/abs/2505.14534) — **論文／工程報告 · 2025**。整理 Google 在分層防禦與對抗式評估上的實務經驗。
- [Making Claude Code Safer with Sandboxing](https://www.anthropic.com/research/claude-code-sandboxing) — **工程報告 · 2025**。討論如何在 coding agent 周圍建立檔案系統與網路隔離。
- [Mitigating Prompt Injections in Browser Use](https://www.anthropic.com/research/prompt-injection-defenses) — **工程報告**。介紹 browser-use 防禦，以及對抗式評估的角色。
- [Agentic Misalignment: LLMs as Insider Threats](https://www.anthropic.com/research/agentic-misalignment) — **受控評估 · 2025**。在模擬組織情境中測試 agent 的有害行為，應與真實系統入侵事件區分。
- [An Agent Used DNS to Reach an External Chatbot](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/) — **第一方事件報告 · 2026**。記錄內部任務中繞過網路控制的行為，可用來檢視 HTTP 以外的 egress control。
- [Practical LLM Security Advice from the NVIDIA AI Red Team](https://developer.nvidia.com/blog/practical-llm-security-advice-from-the-nvidia-ai-red-team/) — **工程指引**。提供 LLM 應用程式的 threat modeling 與部署建議。

## Alignment 與相關研究

這些資源說明模型行為、fine-tuning 與供應鏈風險。Refusal 行為與 indirect prompt injection 抵抗力是不同性質；open weights 與 hosted API 都需要搭配系統層的安全設計。

- [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) — **論文 · 2023**。分析安全訓練中的 competing objectives 與 generalization 失效。
- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) — **論文 · 2023**。提出 GCG 攻擊，並研究它在不同 aligned model 間的轉移效果。
- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — **論文 · 2024**。探討模型表示空間中，與 refusal 行為相關的機制。
- [Shadow Alignment](https://arxiv.org/abs/2310.02949) — **論文 · 2023**。研究 fine-tuning 如何破壞模型的 safety alignment。
- [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) — **論文 · 2023**。評估惡意與良性 fine-tuning 對安全行為造成的退化。
- [BadLlama](https://arxiv.org/abs/2311.00117) — **論文 · 2023**。研究移除 open-weight model 安全微調所需的成本。
- [Sleeper Agents](https://arxiv.org/abs/2401.05566) — **論文 · 2024**。研究經過後續安全訓練後，仍然持續存在的 backdoor 行為。
- [Emergent Misalignment](https://arxiv.org/abs/2502.17424) — **論文 · 2025**。探索針對不安全程式碼的狹窄 fine-tuning，如何造成更廣泛的行為變化。
- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) — **論文 · 2023**。研究污染大型網頁訓練資料集的實際途徑。
- [Scaling Trends for Data Poisoning in LLMs](https://arxiv.org/abs/2408.02946) — **論文 · 2024**。探討模型規模與訓練資料投毒易感性之間的關係。
- [Llama Guard](https://arxiv.org/abs/2312.06674) — **論文 · 2023**。對輸入與輸出進行安全分類，可協助區分內容防護與 agent 授權。
- [Uncensor any LLM with abliteration](https://huggingface.co/blog/mlabonne/abliteration) — **技術教學 · 2024**。介紹在 open-weight model 中移除 refusal direction 的方法。

## 2026 年研究追蹤

**以下資源皆以 arXiv preprint 版本收錄。** 標題與摘要已於 2026-11-08 核對，但未逐篇獨立確認 peer review 或 acceptance 狀態。短評整理的是提出的方法或回報的實驗，不能直接視為實際部署的安全保證。

- [Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147) — 研究如何限制 web agent 工作流程中的 cross-site prompt injection。
- [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264) — 研究透過共享的 agent rule file 誘發 dependency substitution。
- [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488) — 在 coding agent 已遭控制的假設下，提出以 object identity 為基礎的限制方法。
- [The Agent Knew](https://arxiv.org/abs/2610.17301) — 使用 CAPE-Bench，研究如何透過模型內部狀態預測越權行動及後續的誤導性回報。
- [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](https://arxiv.org/abs/2610.18457) — 提出以 transaction 為單位，中介並檢查 agent 對系統造成的副作用。
- [Towards Safe Autonomy for Computer Use](https://arxiv.org/abs/2610.18508) — 研究自主 computer-use 系統的防護方法。
- [Structured Authority Injection](https://arxiv.org/abs/2610.22373) — 提出 typed MCP override，以維持人類的持續控制；需與攻擊者注入任意指令的情境區分。
- [The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection](https://arxiv.org/abs/2610.22594) — 在模擬的醫療 multi-agent 決策任務中評估攻擊與防禦，尚未建立臨床部署有效性的證據。
- [From Approval to Abuse](https://arxiv.org/abs/2610.22987) — 研究攻擊者如何操弄 coding-agent harness 中由使用者核准的 allow-rule。
- [Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems](https://arxiv.org/abs/2610.23078) — 研究以密碼學方法保護 agent 之間的通訊。
- [Ignored, Not Refused](https://arxiv.org/abs/2610.23254) — 區分因任務能力不足而失敗的攻擊，以及被模型明確拒絕的注入指令。
- [SPIDES: Information-Flow Control for Browser Agents](https://arxiv.org/abs/2610.24277) — 研究在 browser agent 的動作層強制執行 information-flow control。
- [RATION: Towards Quantitative Risk-Based Access Control for AI Agents](https://arxiv.org/abs/2610.24311) — 提出以風險為基礎的存取決策，管理安全性與功能之間的取捨。
- [SoK: PIAtlas](https://arxiv.org/abs/2610.24999) — 依 subversion mechanism 整理 prompt injection 技術，並將公開資料集映射到共同分類。
- [After the Attacker Leaves](https://arxiv.org/abs/2610.28425) — 提出 CarryoverBench，評測透過 memory file 與 scheduled task 持續生效的攻擊。
- [Agentic AI Defense: Decode-Time Provenance Binding for MCP](https://arxiv.org/abs/2610.31974) — 探討 cross-modal trust laundering，並提出針對工具解碼內容的 provenance tracking。

## 部落格與導讀

- [Prompt injection: What's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) — **導讀 · 2023**。以具體案例說明，prompt injection 的影響如何超出不當文字輸出。
- [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) — **導讀 · 2025**。將 MCP 工具行為連結到既有的 prompt injection 風險。
- [CaMeL offers a promising new direction](https://simonwillison.net/2025/Apr/11/camel/) — **導讀 · 2025**。介紹以 capability 為基礎的 agent 防禦方法。
- [Design patterns for securing LLM agents](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/) — **導讀 · 2025**。說明不同架構方法及其取捨。
- [New prompt injection papers: Agents Rule of Two and The Attacker Moves Second](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) — **研究評論 · 2025**。將部署限制與 adaptive evaluation 放在一起討論。
- [Simon Willison's prompt injection archive](https://simonwillison.net/tags/prompt-injection/) — **持續更新**。追蹤研究、事件與工程討論的資源入口。
- [Embrace The Red](https://embracethered.com/blog/) — **研究部落格**。提供助理、記憶、工具與 computer use 的第一手安全研究。

## 參與維護

請先閱讀[貢獻指南](CONTRIBUTING.md)。優先提供原始論文、官方規格、持續維護的實作與第一手揭露，附上簡短說明、避免重複項目，並標示證據類型。也歡迎修正既有摘要與連結。

## 授權

本 repository 的原創整理與註解以 [CC0 1.0 Universal](LICENSE) 釋出。所連結的論文、程式碼、標準與文章，仍適用各自的授權與署名要求。
