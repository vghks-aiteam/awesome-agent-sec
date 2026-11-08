# Awesome Agent Security：繁體中文導讀

這是一份以 AI agent 系統安全為主題的資源清單，涵蓋 prompt injection、MCP、工具權限、長期記憶、multi-agent、sandbox 與評測。完整資源與繁體中文摘要見[主目錄](README.md)，也可切換至 [English 版](README.en.md)。

本導讀提供閱讀路徑與判讀方式，資源目錄以繁體中文首頁為主，並提供完整 English 版。[資源狀態表](RESOURCE_STATUS.md)另記錄出版狀態、工具 release、規格版本與查核日期。

## 從哪裡開始

| 你的目標 | 建議閱讀順序 |
| --- | --- |
| 第一次接觸 agent security | 基礎概念 → 威脅模型與標準 → 漏洞揭露與案例研究。 |
| 正在開發能讀私有資料、呼叫工具的 agent | 系統與架構層防禦 → MCP 安全 → Runtime 隔離與供應鏈安全。 |
| 想評估模型或防禦方法 | Benchmark 與評測 → Prompt injection 與 agent 攻擊 → 同時檢查正常任務完成率。 |
| 想找研究題目 | 記憶與 multi-agent 安全 → 2026 年研究追蹤。 |

## 建議先讀的六份材料

1. [Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)：理解外部文件、網頁與工具結果，如何跨越應用程式的信任邊界。
2. [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)：檢查「私有資料、不可信內容、對外通訊」是否在同一條流程相遇。
3. [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)：將風險映射到目標、工具、身分、記憶與人類核准。
4. [Design Patterns](https://arxiv.org/abs/2506.08837)：比較不同架構如何限制攻擊後果，以及功能上的代價。
5. [CaMeL](https://arxiv.org/abs/2503.18813)：理解控制流、資料流與 capability policy 如何在模型之外落實。
6. [The Attacker Moves Second](https://arxiv.org/abs/2510.09023)：理解防禦為什麼需要面對知道其機制、會調整手法的 adaptive attacker。

## 閱讀時先分清楚的概念

**Prompt injection 與 jailbreak。** 前者關心應用程式是否把不可信內容當成指令，導致越權行動或資料外洩；後者關心能否繞過模型的安全行為。兩者可能重疊，但拒答率不能直接代表 agent 的權限安全。

**模型表現與系統邊界。** 更好的 instruction following、classifier 或 guardrail，可以降低部分攻擊的成功率；授權、sandbox、egress control 與工具政策則直接限制系統能做的事情。架構方法的保證仍有前提，例如政策正確、所有敏感操作都經過 enforcement，以及可信元件沒有被繞過。

**攻擊失敗與有效拒絕。** Agent 可能因為能力不足而沒完成攻擊，也可能連正常任務都做不好。評測要一起看 attack success rate、正常任務完成率、攻擊者能力與成本，並區分靜態測試與 adaptive attack。

**研究揭露與實際事件。** Researcher disclosure 可能是受控環境中的重現；CVE 記錄描述特定產品與版本；vendor evaluation 可能使用模擬情境。不能僅因為有展示或 CVE，就推論已發生大規模入侵，也不能據此判定目前版本仍然可利用。

**arXiv 與 peer review。** arXiv 是論文公開平台，不等於通過同儕審查。2026 watchlist 已核對標題與摘要，但沒有逐篇確認 acceptance 或 publication status；閱讀時請另查正式出版資訊。

## 用一條資料流理解風險

假設某個 agent 會讀取使用者上傳的 PDF、查詢內部資料庫，並使用寄信工具輸出結果。PDF 是不可信輸入；資料庫查詢與寄信則是有權限的動作。需要檢查的邊界包括：

- 上傳內容能否改變查詢對象、收件人或工具參數。
- 資料庫帳號是否限制資料範圍，而非直接沿用使用者的全部權限。
- 對外目的地是否由可信政策決定，並由模型之外的元件驗證。
- 寫入、寄信與其他敏感動作是否有清楚的授權條件。
- Audit log 能否重建資料來源、工具呼叫與實際結果。

這些問題可搭配[系統與架構層防禦](README.md#系統與架構層防禦)、[MCP 安全](README.md#mcp-安全)與[Runtime 隔離與供應鏈安全](README.md#runtime-隔離與供應鏈安全)閱讀。這是一個示意 threat model，不代表任何單一產品已具備完整防護。

## 醫療與高敏感資料場景

原始筆記包含醫療應用的關注點。這份 repo 保留了 [medical multi-agent prompt injection 研究](https://arxiv.org/abs/2610.22594)，並將其列入 2026 preprint watchlist。該研究的測試情境與 benchmark 結果，不能直接推論成真實醫院的攻擊發生率或臨床有效性。

若要評估實際工作流程，先界定可存取的資料、可執行的動作、對外通訊管道與核准責任，再選擇相符的 benchmark。模型在本地執行可以改變資料處理與部署條件，但仍需要工具授權、來源追蹤與執行隔離。

## 參與維護

新增資源、修正摘要或回報失效連結前，請參考 [CONTRIBUTING.md](CONTRIBUTING.md)。原始資料的整理方式、連結調整與未收錄項目，記錄於 [curation notes](docs/curation.md)。
