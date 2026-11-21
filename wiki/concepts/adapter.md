---
title: 轉接器（Adapter）
type: method
tags: [parameter-efficient]
sources: [vlod-tta-2026]
updated: 2026-11-21
---
# 轉接器（Adapter）

## 白話版
在大模型的某幾層之間插入小小的「轉接頭」，調整時只動轉接頭、不動大模型。和[[prompt-tuning|提示調整]]一樣是「花小錢辦大事」的參數高效方法。

## 重點
- VLOD-TTA：YOLO-World 在骨幹與 neck 插 Conv-Adapter；Grounding DINO 只在文字編碼器插 MLP-Adapter；初始為 0。（VLOD-TTA, p.7–8）
- 只調約 0.89M 參數（總 173.9M）。（VLOD-TTA, Table 5, p.11）
- 改調 batch norm 也有類似效果，但每個資料集要另調學習率，不適合未知環境；Adapter 一個學習率通用。（VLOD-TTA, Table 4, p.10–11）

## 相關
[[prompt-tuning]] · [[vlod-tta-2026]]
