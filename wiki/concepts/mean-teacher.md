---
title: Mean Teacher（師生自我訓練框架）
type: method
tags: [self-training, core]
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, ttaod-f-2025]
updated: 2026-11-21
summary: 師生自我訓練框架（EMA 老師）
order: 190
---
# Mean Teacher

## 白話版
一個「學生」和一個「老師」模型一起學：老師看清楚的照片出「參考答案」，學生看被弄亂的照片去對答案；老師則慢慢吸收學生的進步。像師徒制，老師穩重、學生衝刺。

## 運作方式
- 學生與老師結構相同、初始權重相同（都來自來源模型）。（DSOD, p.3）
- 老師對「弱擴增」影像產生[偽標籤](pseudo-label.md)，學生用「強擴增」影像學習這些偽標籤。（DSOD, p.3）
- 老師權重 = 學生權重的指數移動平均（EMA）：θ_tch ← α·θ_tch + (1−α)·θ_stu。（DSOD, p.3, Eq.2）
- 用信心門檻 δ 過濾低信心的預測。（DSOD, p.3）
- 實例參數：FALCON 用 EMA 衰減 0.9996、信心門檻 0.8。（FALCON, p.6）
- 目前多數 SOTA SFOD 方法都採這個框架。（FALCON, p.1）

## 在 TTA 的變形
- TTAOD-F 只讓「提示」走師生框架：學生提示梯度更新、老師提示 EMA（γ=0.999）跟隨，大模型凍結。（TTAOD-F, Eq. 5–6, p.5）
- 代價：推論延遲大增，Grounding DINO + Mean Teacher 635 ms/張 vs 直接用 213 ms。（TTAOD-F, Table 9, p.14）

## 在開放集合情境的反直覺結果
- SFUOD 中基本 Mean Teacher 勝過 PET、DRU：進階方法讓老師更新太慢，學不到未知物體。（SFUOD, Table 1, p.6–7）

## 弱點
- 老師一開始只懂來源領域，偽標籤有偏差，錯誤會在自我訓練中被放大 → [source-bias](source-bias.md)。（DSOD, p.1, p.5）

## 和[知識蒸餾](knowledge-distillation.md)有什麼不同？
| | Mean Teacher | 知識蒸餾 |
|---|---|---|
| 老師從哪來 | 學生自己的移動平均，跟著學生一起變（DSOD, p.3） | 另一個已經訓練好的（通常更大的）模型（DSOD, p.6） |
| 目的 | 沒有答案時自己產生參考答案 | 把大模型的本事搬到小模型 |
| 本 wiki 例子 | 多數 SFOD、TTAOD-F | DSOD-Distill（雙老師：EMA 老師＋DSOD 靜態老師） |

## 相關
[source-free-adaptation](source-free-adaptation.md) · [dsod-2026](../sources/dsod-2026.md)
