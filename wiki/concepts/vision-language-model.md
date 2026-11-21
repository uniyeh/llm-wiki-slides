---
title: 圖文模型（Vision-Language Model, 如 CLIP）
type: concept
tags: [vfm, clip, prompt]
sources: [cga-2026, ttaod-f-2025]
aliases: [CLIP, VLM]
updated: 2026-11-21
summary: 圖文模型 CLIP、提示詞
order: 160
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

## 和[[vision-foundation-model|視覺基礎模型]]、[[vision-language-detector|圖文偵測器]]有什麼不同？
| | 視覺基礎模型（DINOv2、OV-SAM） | 圖文模型（CLIP） | 圖文偵測器（Grounding DINO、YOLO-World） |
|---|---|---|---|
| 懂文字嗎 | 否（OV-SAM 為開放詞彙分割，但本 wiki 只用其不分類別遮罩） | 是 | 是 |
| 輸出 | 特徵或遮罩（DSOD, p.3；FALCON, p.3） | 整張圖和文字的相似度（CGA, p.3） | 框＋類別（TTAOD-F, p.3） |
| 本 wiki 用途 | 當顧問或畫重點 | 分類的參考答案 | 直接當偵測器 |

## 相關
[[cga-2026]] · [[class-confusion]]
