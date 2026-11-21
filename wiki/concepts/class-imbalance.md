---
title: 類別不平衡／長尾（Class Imbalance / Long-tail）
type: concept
tags: [problem]
sources: [falcon-sfod-2026]
updated: 2026-11-21
summary: 類別多寡不均、長尾
order: 100
---
# 類別不平衡／長尾

## 白話版
練習題裡「汽車」出現上千次、「火車」只出現幾十次，模型自然擅長汽車、不會火車。偵測裡還有另一種不平衡：大部分候選框其實是背景。

## 重點
- 偵測的偽標籤嚴重不平衡：背景大量、正樣本稀少。（FALCON, p.2）
- Foggy Cityscapes 目標資料的物體數量差很多：car 4,667、person 3,419、bicycle 1,175，但 bus 98、truck 93、train 只有 23 個。（FALCON, Table 8, p.8）
- FALCON 的 IRPL 對少見類別幫助最大：train +4.1、truck +4.0、bus +2.9；類別頻率越低進步越多（r = −0.90）。（FALCON, Table 8, p.8）

## 和[類別混淆](class-confusion.md)有什麼不同？
- 不平衡看「數量」，混淆看「長相」；見 [class-confusion](class-confusion.md)。

## 相關
[pseudo-label](pseudo-label.md) · [falcon-sfod-2026](../sources/falcon-sfod-2026.md)
