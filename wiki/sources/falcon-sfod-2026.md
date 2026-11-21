---
title: FALCON-SFOD — Foundation Model Priors Enhance Object Focus in Feature Space for SFOD
type: source
tags: [sfod, vfm, ov-sam, mean-teacher, noisy-label, long-tail]
sources: [falcon-sfod-2026]
raw: raw/FALCON-SFOD_Foundation_Model_Priors_Object_Focus_SFOD_arXiv2026_[AW].pdf
venue: arXiv 2512.17514v3（2026-02）
updated: 2026-11-22
summary: 用 OV-SAM 遮罩把注意力拉回物體＋抗雜訊、顧及少數類別的損失
order: 20
---
# FALCON-SFOD（2026）

## 一句話摘要
換環境後模型的「注意力」會散到背景上；FALCON 用基礎模型事先畫好的物體遮罩把注意力拉回物體，並用抗雜訊、顧及少數類別的損失函數穩定自我訓練。（FALCON, p.1）

## 要解決的問題
- 主流 SFOD 用 [[mean-teacher]]，老師只在來源領域訓練過，產生的[[pseudo-label|偽標籤]]不可靠且雜訊會傳給學生。（FALCON, p.1）
- 作者觀察到更根本的問題：[[domain-shift]] 讓偵測器的[[attention-map|注意力]]變得分散、延伸到背景雜物，物體邊界模糊 → 偵測頭拿到的特徵不夠清楚 → 偽標籤更差。（FALCON, Fig. 1, p.1–2）
- 以往方法多在「修偽標籤」，忽略「修特徵空間本身」。（FALCON, p.1）

## 方法（白話＋技術）
**白話**：模型在霧裡「東張西望」，FALCON 事先請一位擅長描輪廓的通才（OV-SAM）把每張新照片「哪裡是東西」塗成黑白圖，訓練時要求模型的目光落在白色區域；同時改變計分方式：簡單題少練、難題照練、冷門類別多照顧。

**技術**（建立在 Simple-SFOD 基線上，p.6）：
1. **SPAR（Spatial Prior-Aware Regularization）**：取骨幹最後一層特徵的通道平均圖 A_S，與 [[segmentation-model|OV-SAM]] 產生的「不分類別二值遮罩」A_G 對齊，損失 = λ1·L1 + λ2·Dice（λ1=1、λ2=2）。（FALCON, Eq. 3, p.3–4）
   - 遮罩在訓練前**離線算一次**，訓練與推論都不再呼叫基礎模型 → 推論零額外負擔。（FALCON, p.2–3）
2. **IRPL（Imbalance-aware Noise Robust Pseudo-Labeling）**：取代交叉熵的分類損失。（FALCON, Eq. 4–6, p.4）
   - peak-adjust：師生意見一致的框梯度被縮小（像自動提早停止），不一致的框保留完整修正訊號。
   - 前景／背景加權 w_ĉ：處理背景框遠多於物體框的[[class-imbalance|不平衡]]。
   - 熵正則 D_KL：避免常見類別主導。
3. **理論**：推導 SFOD 的偵測風險上界，說明 IRPL 讓分類誤差項變緊、SPAR 降低定位誤差項（η_reg、ζ）。（FALCON, Theorem 1–2, p.4–5）→ 不放進簡報。

## 實驗設定（資料集、指標）
- 任務：Cityscapes→Foggy（C→F）、Sim10k→Cityscapes（S→C）、KITTI→Cityscapes（K→C，跨相機）、Cityscapes→BDD100k。另測[[extreme-domain-shift|極端落差]]：Pascal VOC→Clipart、FLIR 可見光↔紅外線。（FALCON, p.5–6）
- 指標 mAP@0.5；EMA 衰減 0.9996、信心門檻 0.8；單張 RTX A6000。（FALCON, p.6）
- 見 [[benchmarks]]。

## 主要結果（已驗算：各類別平均與 mAP 欄一致）
| 任務 | Source only | 基線 Simple-SFOD | FALCON | 來源 |
|---|---|---|---|---|
| C→F | 25.2 | 45.0 | **46.9** | Table 1, p.6 |
| S→C（car AP） | 32.0 | 55.4 | **58.8** | Table 1, p.6 |
| K→C（car AP） | 33.9 | 46.2 | **50.1** | Table 1, p.6 |
| C→BDD | 19.1 | 34.3 | **36.9** | Table 2, p.7 |

- 消融（C→F）：基線 45.0 → +SPAR 46.1 → +IRPL 45.8 → 兩者 46.9。（Table 5, p.8）
- 遮罩來源比較（C→F）：源模型自己的注意力圖 45.8 < GSAM 46.2 < ESC-Net 46.5 < OV-SAM 46.9。（Table 6, p.8）
- 只拿遮罩篩偽標籤（不加 SPAR 損失）進步有限 → 進步來自 SPAR 本身。（Fig. 2, p.7–8）
- 少見類別進步最多：train +4.1、truck +4.0、bus +2.9；car −0.2、person +0.1；類別頻率與進步幅度相關係數 r = −0.90。（Table 8, p.8）
- 極端落差約 +2 mAP，如 VOC→Clipart 33.6→35.5。（Table 3–4, p.7）

## 限制
- S→C 只比 DRU 高 0.1（58.8 vs 58.7）；K→C 只比 SF-YOLO 高 0.7（50.1 vs 49.4）。（Table 1, p.6）
- 需事先對每張目標影像跑一次分割模型（一次性前處理成本）。（FALCON, p.2）

## 設計決策與消融證據
| 設計 | 為什麼 | 證據 |
|---|---|---|
| 用遮罩規範特徵，而非只修偽標籤 | 偽標籤差的根源是特徵注意力分散 | 只拿遮罩篩偽標籤進步有限；加 SPAR 損失才明顯（Fig. 2, p.7–8） |
| 遮罩離線算一次 | 訓練與推論都不呼叫基礎模型 | 前處理約 17 分鐘，為訓練時間 3.8%（p.15，以 GSAM 計） |
| 遮罩越準越好 | 遮罩語意越對齊，規範越有效 | 源模型注意力 45.8 < GSAM 46.2 < ESC-Net 46.5 < OV-SAM 46.9（Table 6, p.8） |
| IRPL 三部件 | 交叉熵梯度無上限、偵測前景背景不平衡、常見類別主導 | peak-adjust 55.9 → +前背景加權 56.3 → +熵正則 56.8（S→C，Table 7, p.8） |

## 作者提到的限制與未來方向
- 結論未列限制或未來工作。（p.8）
- 補充材料指出額外成本只在一次性前處理（約 17 分鐘、峰值 18 GB，訓練本身 ≤ 9.6 GB）。（p.15）

## 矛盾
- 內文寫「贏 SF-YOLO 4.9%」（p.6），但 Table 1 為 46.9 − 42.5 = **4.4**。依規則以表格為準。
- VOC→Clipart：表格 mAP 35.5，但 20 類自算平均為 35.35（約 35.4），差距小，依規則用表格 35.5。（Table 3, p.7）
- 與 [[dsod-2026]] 的 Source only 不同（25.2：FALCON, Table 1, p.6；29.5：DSOD, Table 1, p.8），因基線偵測器不同；**兩篇絕對分數不可直接比較**，見 [[results-comparison]]。

## 和其他論文的關係
- 與 [[dsod-2026]] 同屬「借用[[vision-foundation-model]]」：DSOD 把 DINOv2 特徵**加進**模型（推論要帶著或蒸餾），FALCON 只用 OV-SAM 的遮罩當**規範**（推論不需要）。見 [[method-comparison]]。
- IRPL 屬於 [[pseudo-label]] 雜訊處理家族的延伸。
