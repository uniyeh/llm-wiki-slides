---
title: 簡報大綱（OUTLINE）v3
type: outline
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-22
---
# 換了環境，AI 還認得出來嗎？——SF-DAOD 入門（24 頁）

v2 依使用者回饋（2026-11-22）：每個方法改為「概要＋架構與設計討論」2 頁；第 6 頁箭頭加說明；第 7 頁改為「來源偏差 vs 領域落差」；吉祥物台詞不得複述內文；CGA 改為延伸發想；結尾改為「做到了什麼、還差什麼」。

| # | 段落 | 標題 | 對應 wiki | 吉祥物提醒 |
|---|---|---|---|---|
| 1 | 引入 | 換了環境，AI 還認得出來嗎？ | [[index]] | —（幾何圖形） |
| 2 | 引入 | 新手駕駛的霧夜 | [[domain-shift]] | confused_pink「咦？這是車還是霧？」 |
| 3 | 基礎 | 物件偵測：有什麼、在哪裡 | [[object-detection]] | — |
| 4 | 問題 | 換了環境，分數就掉 | [[domain-shift]] · [[benchmarks]] | — |
| 5 | 問題 | 舊資料拿不到了 | [[source-free-adaptation]] | — |
| 6 | 基本做法 | 自己出題、自己練習（箭頭：把知識傳給學生／吸收學生進步） | [[mean-teacher]] · [[pseudo-label]] | — |
| 7 | 問題 | 來源偏差：和領域落差差在哪？ | [[source-bias]] | bored_yellow「接下來的方法，都在幫我放下舊習慣！」 |
| 8 | 地圖 | 研究者的三條路 | [[sfod-method-families]] | — |
| 9 | 路線 1 | DSOD 概要 | [[dsod-2026]] | — |
| 10 | 路線 1 | DSOD 架構與設計討論 | [[dsod-2026]] | — |
| 11 | 路線 1 | FALCON 概要 | [[falcon-sfod-2026]] | determined_red「常見的汽車、行人幾乎沒變，難的反而進步最多！」 |
| 12 | 路線 1 | FALCON 架構與設計討論 | [[falcon-sfod-2026]] · [[attention-map]] | — |
| 13 | 比較 | 比進步，不比分數 | [[results-comparison]] | — |
| 14 | 路線 2 | SFUOD 概要 | [[sfuod-2025]] | confused_pink「我只學過車，行人、腳踏車對我都是『不認識』！」 |
| 15 | 路線 2 | SFUOD 架構與設計討論 | [[collaborative-tuning-paul]] | — |
| 16 | 路線 3 | 另一條路：邊用邊學 | [[test-time-adaptation]] | — |
| 17 | 路線 3 | TTAOD-F 概要 | [[ttaod-f-2025]] | struggle_blue「上線即時用的系統，速度也是成績的一部分。」 |
| 18 | 路線 3 | TTAOD-F 架構與設計討論 | [[ttaod-f-2025]] · [[prompt-tuning]] | — |
| 19 | 路線 3 | VLOD-TTA 概要 | [[vlod-tta-2026]] | — |
| 20 | 路線 3 | VLOD-TTA 架構與設計討論 | [[vlod-tta-2026]] · [[entropy-minimization]] | — |
| 21 | 延伸 | 把「容易搞混」的點子帶回偵測（CGA；發想 X1 騎士↔行人、X6） | [[ideas]] · [[cga-ideas-for-detection]] | guide_blue「你還想得到哪些『長得很像』的東西？」 |
| 22 | 延伸 | 還可以怎麼做？三個有根據的發想（X2 遮罩×小物體、X3 免重新訓練、X5 放大解析度） | [[ideas]] | — |
| 23 | 總結 | 這個領域：做到了什麼、還差什麼 | [[results-comparison]] | — |
| 24 | 回顧 | 小測驗（4 題） | [[glossary]] | — |

## 數字使用決策
- DSOD 晴→霧用表格 48.1，不與 Oracle 比較；講者備註註明各類平均 46.4。
- TTAOD-F 延遲用 TTAOD-F 自己量的數字；VLOD-TTA 比較只用其 Table 5。
- 論文數字錯誤只記在 wiki，不上簡報（使用者決策）。

## v3（2026-11-22）
- 依 SYNTHESIZE 產出 `wiki/comparisons/ideas.md`：第 21 頁換成最有根據的發想（騎士被推成行人 × CGA 有方向的混淆），新增第 22 頁。
