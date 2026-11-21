---
title: DETR / Deformable-DETR
type: method
tags: [detector, transformer]
sources: [dsod-2026]
updated: 2026-11-21
---
# DETR / Deformable-DETR

## 白話版
一種用 Transformer 做物件偵測的方法：模型直接「一次列出清單」說畫面中有哪些物體、各在哪，不需要事後再刪掉重複的框。

## 重點
- DETR 把偵測改寫成「集合預測」問題，去掉 NMS 與錨框；缺點是訓練收斂慢。（DSOD, p.2）
- Deformable-DETR 用稀疏注意力改善收斂速度，是 DSOD 等 SFOD 方法的基線偵測器。（DSOD, p.2, p.7）

## 相關
[[object-detection]] · [[dsod-2026]]
