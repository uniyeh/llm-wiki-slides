---
title: 物件偵測（Object Detection）
type: concept
tags: [basics]
sources: [dsod-2026]
updated: 2026-11-21
summary: 找出「有什麼、在哪裡」
order: 10
---
# 物件偵測（Object Detection）

## 白話版
讓電腦看一張照片，同時回答「有什麼東西」和「在哪裡」——用方框把每台車、每個人框起來並貼上名字。就像玩「威利在哪裡」，不只要找到，還要指出位置。

## 重點
- 輸出 = 一組「框（bounding box）+ 類別 + 信心分數」。
- 常見架構：兩階段（Faster R-CNN）、一階段、無錨框；近年有 Transformer 架構的 [detr](detr.md)。（DSOD, p.2）
- 傳統偵測器會對同一物體產生多個框，需用 NMS 去重；DETR 系列不需要。（DSOD, p.2）
- 評估指標見 [benchmarks](benchmarks.md)（mAP）。

## 相關
[domain-shift](domain-shift.md) · [source-free-adaptation](source-free-adaptation.md)
