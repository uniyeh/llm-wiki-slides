---
title: 分割模型（Segmentation Model, 如 OV-SAM）
type: concept
tags: [vfm, segmentation]
sources: [falcon-sfod-2026]
updated: 2026-11-21
---
# 分割模型（OV-SAM 等）

## 白話版
能把照片裡每個東西的輪廓「塗色描出來」的模型。物件偵測是畫方框，分割是沿著邊緣描形狀，更精細。

## 重點
- FALCON 用凍結的開放詞彙分割模型 OV-SAM 產生遮罩，丟掉類別資訊、只留「是物體＝1／背景＝0」。（FALCON, p.3）
- 遮罩品質越好，FALCON 效果越好：OV-SAM 46.9 > ESC-Net 46.5 > GSAM 46.2（C→F）。（FALCON, Table 6, p.8）
- 屬於 [[vision-foundation-model]] 的一種用法。

## 相關
[[attention-map]] · [[falcon-sfod-2026]]
