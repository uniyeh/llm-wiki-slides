---
title: 圖片分類 vs 物件偵測
type: concept
tags: [basics]
sources: [cga-2026]
updated: 2026-11-21
---
# 圖片分類 vs 物件偵測

## 白話版
- **圖片分類**：看一整張圖，回答「這是什麼」——一張圖一個答案。
- **物件偵測**：在圖裡找出每個東西並框起來——一張圖很多答案，還要給位置。偵測比分類多了「在哪裡」和「有幾個」。

## 重點
- CGA 處理的是分類版的 SFDA，資料集為 Office-31、Office-Home、VisDA、DomainNet-126，指標為準確率。（CGA, p.6）
- 偵測見 [[object-detection]]；本 wiki 主題是偵測，分類只作延伸。

## 相關
[[object-detection]] · [[cga-2026]]
