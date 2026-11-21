---
title: 圖文模型（Vision-Language Model, 如 CLIP）
type: concept
tags: [vfm, clip, prompt]
sources: [cga-2026, ttaod-f-2025]
aliases: [CLIP, VLM]
updated: 2026-11-21
---
# 圖文模型（CLIP 等）

## 白話版
同時讀得懂「圖」和「文字」的模型。給它一張照片和幾句描述（「一張貓的照片」「一張狗的照片」），它能判斷照片最符合哪一句——所以不用重新訓練也能分類新東西（零樣本 zero-shot）。

## 重點
- CLIP：影像編碼器＋文字編碼器，以兩者特徵的 cosine 相似度做零樣本分類。（CGA, p.3）
- **提示詞（prompt）**：文字輸入的模板，例如「A picture of a [類別]」；可只微調提示詞、凍結其餘參數（CoOp 方式）。（CGA, p.3）
- CGA 加入混淆提示詞「[i] looks like a [j]」讓 CLIP 分辨更細。（CGA, p.5）
- 屬於 [[vision-foundation-model]] 的一種。
- 用在偵測上就是[[vision-language-detector|圖文偵測器]]（GLIP、Grounding DINO）。（TTAOD-F, p.3）
- 調整方式見 [[prompt-tuning]]。

## 相關
[[cga-2026]] · [[class-confusion]]
