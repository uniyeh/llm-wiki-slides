---
title: 熵最小化（Entropy Minimization）
type: method
tags: [tta, objective]
sources: [vlod-tta-2026]
updated: 2026-11-21
summary: 讓模型更果斷的調整目標
order: 250
---
# 熵最小化

## 白話版
「熵」是模型有多猶豫：各類別分數差不多＝很猶豫（熵高），一類特別高＝很有把握（熵低）。熵最小化就是要求模型「更果斷」。不需要正確答案就能調整，所以常用在邊用邊學；風險是連猜錯的也會變得很有自信。

## 重點
- 標準目標：所有候選框的平均熵 L = (1/N) Σ H(p_i)。（VLOD-TTA, Eq. 2, p.5）
- 代表方法 Tent：更新 batch normalization 參數來最小化熵。（VLOD-TTA, p.4）
- 用在偵測的問題：放大確認偏誤（位置錯的框也被拉高信心）、把孤立框和成群框一視同仁。（VLOD-TTA, p.2–3, Fig. 1）
- 改良：VLOD-TTA 的 IWE 依[重疊群](candidate-box-iou.md)加權。（VLOD-TTA, p.6）
- 與 [mean-teacher](mean-teacher.md) 相比：不需老師模型與額外前向傳遞，開銷較低。（VLOD-TTA, p.2, p.11）

## 相關
[test-time-adaptation](test-time-adaptation.md) · [vlod-tta-2026](../sources/vlod-tta-2026.md)
