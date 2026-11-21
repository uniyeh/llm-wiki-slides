---
title: 注意力圖／特徵激活（Feature Activation Map）
type: concept
tags: [feature, object-focus]
sources: [falcon-sfod-2026]
updated: 2026-11-21
summary: 模型在看哪裡
order: 80
---
# 注意力圖（特徵激活圖）

## 白話版
把模型「在照片上盯著哪裡看」畫成熱度圖：越亮代表模型越在意。好的模型目光會集中在車子、行人身上；換到霧天時，目光可能飄到霧和背景雜物上。

## 重點
- FALCON 取骨幹最後一層特徵的「通道平均」當作這張圖，通常會亮在前景物體上。（FALCON, p.3）
- [domain-shift](domain-shift.md) 會讓這張圖變分散、延伸到背景，造成框不準與誤判。（FALCON, Fig. 1, p.2）
- FALCON 的 SPAR 要求這張圖貼近物體遮罩。（FALCON, Eq. 3, p.4）

## 相關
[segmentation-model](segmentation-model.md) · [falcon-sfod-2026](../sources/falcon-sfod-2026.md)
