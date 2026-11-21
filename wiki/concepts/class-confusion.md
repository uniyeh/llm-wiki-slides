---
title: 類別混淆（Class Confusion）
type: concept
tags: [problem, fine-grained]
sources: [cga-2026]
updated: 2026-11-21
---
# 類別混淆（Class Confusion）

## 白話版
有些東西本來就長得像，模型容易認錯，而且認錯常常是「單向」的：卡車常被當成公車，公車卻很少被當成卡車——就像你可能把雙胞胎弟弟叫成哥哥，但總把哥哥叫對。

## 重點
- **不對稱**：例如 truck 常被誤判為 bus，反之少見，原因之一是訓練資料量不同。（CGA, p.2）
- **動態**：混淆關係會在調整過程中改變。（CGA, p.2）
- 後果：產生錯誤[[pseudo-label|偽標籤]]，也扭曲特徵空間；在細粒度分類特別嚴重。（CGA, p.2）
- CGA 用混淆矩陣找出有向混淆對，再針對性處理。（CGA, p.4）

## 和[[class-imbalance|類別不平衡]]有什麼不同？
- 不平衡是「某類樣本太少」（FALCON, Table 8, p.8）；混淆是「兩類長得像而互相認錯」，且有方向（CGA, p.2）。兩者可能同時發生：卡車、公車既少見又容易互相混淆。

## 相關
[[cga-2026]] · [[class-imbalance]] · [[cga-ideas-for-detection]]
