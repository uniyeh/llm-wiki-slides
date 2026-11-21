---
title: 延伸發想總表（SYNTHESIZE 產出）
type: comparison
tags: [synthesis, ideas, open-problems]
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-22
summary: （SYNTHESIZE）延伸發想總表：作者未來方向、交叉發想、共同盲點、建議加讀論文
order: 30
---
# 延伸發想總表

> ⚠️ 本頁由 SYNTHESIZE 節點自動產生，內容是**跨論文的發想**，不是任何一篇論文的結論。每條都列出根據的事實與出處；找不到事實根據的發想不收錄。

## 白話版
發想從三個地方來：①作者自己說還沒做好的地方；②拿 A 論文的方法去套 B 論文的難題；③好幾篇論文都卡住的共同盲點。最後列出各篇常引用、但還不在 raw/ 的論文，給使用者決定要不要加入。

## ① 作者自己提到的限制與未來方向
| 論文 | 作者說的 | 出處 |
|---|---|---|
| [[vlod-tta-2026]] | 小物體多、框重疊少時 IWE 較弱；仍比 zero-shot 慢；未來做免梯度調整 | VLOD-TTA, p.15 |
| [[vlod-tta-2026]] | 騎士常被當成行人，IWE 還會加重這個傾向 | VLOD-TTA, Table 12–13, p.22–23 |
| [[dsod-2026]] | 可受益於更大的 VFM 與更高解析度；可與 DDT 結合 | DSOD, p.7 |
| [[sfuod-2025]] | 「仍有改進空間」 | SFUOD, p.8 |
| [[cga-2026]] | 混淆提示每句約 29 MB 記憶體 | CGA, p.10 |
| [[falcon-sfod-2026]]、[[ttaod-f-2025]] | 未列限制 | FALCON, p.8；TTAOD-F, p.18 |

## ② 交叉發想：A 的方法 × B 的難題
| # | 發想（問題形式） | A 的方法 | B 的難題 | 張力／風險 |
|---|---|---|---|---|
| X1 | 邊用邊學時，能否用「有方向的混淆」保護騎士不被推成行人？例如加入「看起來像行人的騎士」描述 | CGA 有方向的混淆提示（CGA, p.4–5） | VLOD-TTA 讓 rider AP 6.3 → 1.9（VLOD-TTA, Table 12, p.22–23） | 混淆提示會增加記憶體（CGA, p.10）；TTA 本來就在意資源 |
| X2 | 小物體重疊框少時，能否改用「物體遮罩」判斷哪裡有東西？ | FALCON 的不分類別遮罩（FALCON, p.3） | IWE 依重疊群加權，小物體不易成群（VLOD-TTA, p.15） | FALCON 的遮罩是離線算的；TTA 沒有「訓練前」，即時跑分割模型會更慢 |
| X3 | 能否組合「免訓練」的零件，做出作者想要的免梯度 TTA？ | TTAOD-F 的記憶校正單獨用即 44.8 → 46.1（TTAOD-F, Table 3, p.8）；VLOD-TTA 的提示挑選 | VLOD-TTA 未來方向：免梯度（VLOD-TTA, p.15） | 記憶校正需 DINOv2 特徵（TTAOD-F, p.6），也有成本；提示挑選單獨效果需另驗證 |
| X4 | 圖文偵測器叫得出名字的交給文字，叫不出名字的交給 PAUL 找「物體性」？ | SFUOD 的 PAUL（SFUOD, p.5–6） | TTAOD-F 雖不限類別，但仍要先寫出類別名稱（TTAOD-F, p.4） | 兩者設定不同（離線 vs 即時），需重新設計 |
| X5 | SFOD 在行車場景是否也該試更高解析度？ | VLOD-TTA：1024 輸入讓 Cityscapes 從 19.4 → 31.2（VLOD-TTA, Table 14, p.23） | DSOD 跨場景未達 SOTA、作者也說更大輸入可能更好（DSOD, p.7） | 訓練負擔增加（DSOD, p.7） |
| X6 | 偵測的難類別（卡車、公車）能否也用混淆提示補強？ | CGA 混淆提示（CGA, p.5） | FALCON 中 truck、bus 是少見類別（FALCON, Table 8, p.8） | 詳見 [[cga-ideas-for-detection]] |

## ③ 共同盲點
| 盲點 | 根據 |
|---|---|
| 各篇起點（基礎偵測器）不同，缺少公平比較 | [[results-comparison]]；DSOD 29.5 vs FALCON 25.2（各自 Table 1） |
| 行車場景的小物體仍難 | VLOD-TTA, p.9, p.15；DSOD 跨場景未達 SOTA（p.7） |
| 「沒見過的東西」只有 SFUOD 處理，且只找回約 1/10 | SFUOD, Table 1, p.6 |
| 相似類別互相誤認（卡車↔公車、騎士↔行人） | CGA, p.2；VLOD-TTA, p.22–23 |

## ④ 建議加入 raw/ 的論文（由使用者決定）
| 論文 | 被哪些 raw 論文引用／比較 | 為什麼值得讀 |
|---|---|---|
| DRU | DSOD、FALCON、SFUOD（SFUOD 以它為基線） | 三篇共同比較對象 |
| PETS / PET | DSOD、FALCON、SFUOD | 多老師框架的代表 |
| IRG | DSOD、FALCON | 實例關係圖＋對比學習 |
| Simple-SFOD | FALCON（基線） | 證明簡單自我訓練就很強 |
| DDT | DSOD | 晴→霧表格中的強對手 |
| STFAR、CTTOD | TTAOD-F | 舊 TTA 偵測方法（需來源統計量） |
| TPT、DPE | VLOD-TTA | 分類用 TTA 方法搬到偵測的基線 |
| DIFO、ProDe | CGA | 用 CLIP 做 SFDA 的前作 |

## 相關
[[cga-ideas-for-detection]] · [[results-comparison]] · [[method-comparison]] · [[sfod-method-families]]
