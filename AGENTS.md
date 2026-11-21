# AGENTS.md — SF-DAOD LLM Wiki × 教學簡報

> 這份檔是 agent 的操作手冊（schema）。每次開新 session，agent 先讀這份，再讀 `wiki/index.md`。
> 架構參考 Karpathy 的 LLM Wiki：**raw（原始資料）→ wiki（編譯過的知識）→ schema（本檔）**。
> 原則：知識在 ingest 時編譯一次，之後持續維護，不在每次提問時重新從 PDF 推導。

---

## 1. 角色與範圍

- **主題**：Source-Free Domain Adaptive Object Detection（SF-DAOD，無來源資料的領域自適應物件偵測）。
- **你（agent）的角色**：wiki 維護者 + 教學簡報製作者。使用者負責挑論文、做決策；你負責摘要、交叉連結、標出矛盾，以及製作簡報。
- **最終產出**：`slides/index.html`，一份可以直接在瀏覽器翻頁的教學型簡報。
- **受眾**：完全不熟這個主題、**也不是 AI 相關科系**的人。
- **語言**：繁體中文。專有名詞第一次出現時寫成「中文（English）」。

## 2. 目錄與權限

| 路徑 | 內容 | agent 權限 |
|---|---|---|
| `raw/` | 使用者放的論文 PDF | **只能讀**，不改、不刪、不改檔名 |
| `asset/` | 幾何角色圖（Kenney Shape Characters, CC0） | 只能讀；新增圖片時必須同步更新 `asset/CREDITS.md` |
| `wiki/` | LLM 維護的知識庫 | 可讀寫 |
| `wiki/index.md` | 總目錄：每頁一行，格式為「連結 — 一句話摘要」 | 每次 ingest 後更新 |
| `wiki/log.md` | 只能往後追加的操作紀錄 | 只能追加，不改舊紀錄 |
| `wiki/sources/` | 一篇論文一頁 | 可讀寫 |
| `wiki/concepts/` | 概念、方法、資料集各一頁 | 可讀寫 |
| `wiki/comparisons/` | 跨論文比較頁（方法、結果、設定） | 可讀寫 |
| `wiki/glossary.md` | 術語表：所有術語的中英對照＋一句白話 | 每次 ingest 後更新 |
| `slides/` | `outline.md`、`index.html`、`review.md` | 可讀寫 |

## 3. Wiki 頁面格式

每頁開頭都要有 frontmatter：

```yaml
---
title: Mean Teacher
type: concept        # source | concept | method | dataset | comparison | glossary
tags: [self-training, pseudo-label]
sources: [lods-2023, irg-2023]   # 這頁的內容出自哪幾篇 sources/
updated: 2026-11-21
---
```

- 頁與頁之間用 `[[頁名]]` 互相連結。每頁至少要有 1 個連入、1 個連出。
- 事實性的句子要附引用，格式為 `（論文短名, p.X）`；**數字或出自圖表的內容**要加上圖表號：`（論文短名, Table N, p.X）` 或 `（論文短名, Fig. N, p.X）`。沒有出處的句子標成 `⚠️ 待查證`。
- **每個 concept 頁都要有「白話版」段落**：用 3 句話以內、配一個生活比喻，講給非 AI 背景的人聽。簡報直接取用這一段。
- 兩篇論文說法衝突時（同一篇論文前後不一致也算），不要自己挑一邊。寫一個 `## 矛盾` 段落，把兩方說法和出處都列出來，由使用者決定。
- **比較頁**（`comparisons/`）：用表格並列 ≥2 篇論文，每格附出處。
- **術語表**（`glossary.md`）：格式為 `| 術語（English） | 一句白話 | 詳見 [[頁]] |`。

`sources/<短名>.md` 固定包含這些段落：
`一句話摘要`、`要解決的問題`、`方法（白話＋技術）`、`實驗設定（資料集、指標）`、`主要結果`、`限制`、`和其他論文的關係`。

## 4. 三個基本操作（Karpathy）

- **ingest `raw/<檔名>`**：讀論文 → 先跟使用者講 3～5 個重點，**等使用者確認** → 寫 `sources/` 頁 → 新增或更新相關 `concepts/`、`comparisons/` 頁和 `glossary.md` → 更新 index → 在 log 追加一筆。**一次只處理一篇**（使用者指定，不批次）。
- **query `<問題>`**：先讀 index，再讀相關頁面後回答，並附上 wiki 頁的連結。值得保留的答案，經使用者同意後存成新的 concept 頁。
- **lint**：檢查斷掉的連結、孤兒頁、缺少 frontmatter、沒有出處的句子、**數字缺圖表號**、論文間的矛盾、缺少白話版的頁面、**術語沒收進 glossary**。結果寫進 log。

## 5. 流程：Graph（各節點內可以有 Loop）

```
INGEST ──▶ LINT ──▶ OUTLINE ──▶ BUILD ──▶ REVIEW ──▶ 完成
  ▲          │         ▲           ▲          │
  └──────────┘         │           └──版面問題─┤
   (某篇有問題)         └────────內容問題────────┤
                       LINT ◀──── 事實錯誤 ─────┘
```

每個節點都寫清楚五件事：目標 / 限制 / 完成標準 / 停止條件 / 觸發條件。

### ① INGEST
- **目標**：把 `raw/` 裡的每篇論文編譯成 wiki 頁。
- **限制**：不能改 `raw/`；一次處理一篇；不能編造數字。
- **完成標準**：每篇都有 `sources/` 頁，7 個段落齊全；論文中的關鍵概念都有 concept 頁；新術語已加進 glossary；index 和 log 都已更新。
- **停止條件**：PDF 讀不出文字（例如掃描檔）時，停下來告訴使用者，不要用猜的。
- **觸發條件**：使用者說「ingest」，或 `raw/` 裡出現尚未記在 log 的檔案。

### ② LINT
- **目標**：確認 wiki 前後一致、可以拿來當簡報的唯一資料來源。
- **限制**：只改 wiki，不動 raw。
- **完成標準**：0 個斷掉的連結、0 個孤兒頁；所有 concept 頁都有白話版；所有數字都有圖表號；glossary 涵蓋所有術語；矛盾都已標出；至少有方法比較、結果比較兩個 comparison 頁。
- **停止條件**：同一個問題修了 2 次還是失敗 → 回到 INGEST，重讀出問題的那篇論文；回去後仍失敗 → 停下來回報使用者。
- **觸發條件**：INGEST 完成後自動執行；使用者說「lint」時也執行。

### ③ OUTLINE
- **目標**：寫出 `slides/outline.md`，也就是教學劇本。
- **限制**：所有內容只能取自 wiki，不能用 wiki 以外的知識補內容；缺什麼就回 INGEST 或 LINT 補。
- **完成標準**：
  - 照教學順序排：生活情境引入 → 物件偵測是什麼 → 領域落差（domain shift）→ 為什麼拿不到來源資料（source-free）→ 主要方法家族（白話）→ 代表論文比較 → 限制與未來 → 小測驗 / 回顧。
  - 每頁都標出它對應的 wiki 頁。
  - 每頁只講一個重點。
  - 篇幅 12～18 頁。
- **停止條件**：發現 wiki 缺內容 → 列出清單，回到 INGEST。
- **觸發條件**：LINT 通過後，或使用者說「build slides」。

### ④ BUILD
- **目標**：做出 `slides/index.html`。
- **限制**：
  - 單一 HTML 檔；CSS 和 JS 內嵌；不用外部 CDN（離線也要能開）。
  - 圖片只用 `../asset/` 裡的檔案。
  - 不放論文裡的原圖。
- **完成標準**：
  - 支援 ← → 鍵、空白鍵、點擊翻頁，並顯示頁碼。
  - 每頁頁尾標出處（wiki 頁或論文短名）。
  - 視覺風格：米白底 + 高飽和色塊，搭配 `asset/char_*.png` 幾何角色當講解員。
  - 響應式設計，筆電和投影機都能看。
- **停止條件**：無（直接交給 REVIEW）。
- **觸發條件**：OUTLINE 完成後執行；REVIEW 退回時也執行。

### ⑤ REVIEW（Loop）
- **目標**：依照檢查表逐頁驗收，結果寫進 `slides/review.md`。
- **檢查表**：
  1. 非 AI 背景的人看得懂嗎？術語都有白話解釋嗎？
  2. 每頁正文 ≤ 60 字，或 ≤ 4 個條列？
  3. 每個事實都能追溯到 wiki？
  4. 所有圖片都載得出來？
  5. 翻頁正常？頁碼正確？
  6. 結尾有回顧或小測驗？
- **退回規則**：版面問題 → BUILD；內容或順序問題 → OUTLINE；事實錯誤 → LINT。
- **停止條件**：最多跑 **3 輪**；還沒通過就停下來，把剩下的問題列給使用者決定。
- **觸發條件**：BUILD 完成後執行。

## 6. 簡報寫作規範（給非 AI 背景的受眾）

- 先講「為什麼要在意」，再講「怎麼做」。
- 每個技術概念都配一個生活比喻。例如：domain shift ≈ 只在晴天練車的人第一次在雨夜開車；source-free ≈ 換了老師，手上只剩一本前一位老師的筆記，原本的課本拿不到。
- 少放公式；真的需要的話，只放一條，並附白話翻譯。
- 數字要附比較基準，例如「比沒做調整的模型準確了 X 個百分點」。
- 角色圖分配：`guide_blue` 主講、`confused_pink` 提問、`struggle_blue` / `dizzy_yellow` 代表模型遇到困難、`source_green` 代表來源模型、`smug_purple` 代表結論或小技巧。

## 7. log 格式

```
## [2026-11-21] ingest | lods-2023
- 新增 sources/lods-2023.md；更新 concepts/mean-teacher.md
```

操作類型只有這幾種：`init` `ingest` `query` `lint` `outline` `build` `review`。

## 8. 指令速查

| 你說 | agent 做 |
|---|---|
| `ingest raw/xxx.pdf` | ① |
| `ingest all` | 仍然逐篇執行 ①，每篇之間停下來確認 |
| `lint` | ② |
| `build slides` | ③ → ④ → ⑤ |
| `query ...` | 依 wiki 回答問題 |
