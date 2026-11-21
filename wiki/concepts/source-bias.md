---
title: 來源偏差（Source Bias）
type: concept
tags: [problem]
sources: [dsod-2026]
updated: 2026-11-21
---
# 來源偏差（Source Bias）

## 白話版
模型雖然在學新環境，但腦袋還是用舊環境的習慣在判斷，像搬到台北的人還一直用老家的路名找路。

## 重點
- 定義：調整後的模型仍偏向來源領域，導致泛化差，並在自我訓練中累積錯誤。（DSOD, p.1）
- 為什麼 SFOD 特別嚴重：UDA 能同時看兩個領域來學共通特徵；SFOD 只能看目標資料。（DSOD, p.1–2）
- 對策之一：引入不偏向任何領域的 [[vision-foundation-model]]（DSOD）。

## 相關
[[pseudo-label]] · [[mean-teacher]] · [[dsod-2026]]
