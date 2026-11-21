---
title: 召回率（Recall）與 H-Score
type: dataset
tags: [metric]
sources: [sfuod-2025]
updated: 2026-11-21
summary: 開放集合指標
order: 270
---
# 召回率與 H-Score

## 白話版
- **召回率（U-Recall）**：該找到的未知物體裡，找到了幾成。10.59 代表大約每 10 個只找到 1 個（SFUOD, Table 1, p.6）。
- **H-Score**：把「已知認得準」和「未知找得到」綜合成一個分數，兩者都要好才會高，只顧一邊會被拉低。

## 定義
- Known mAP：已知類別的 mAP（見 [[benchmarks]]）。（SFUOD, p.6）
- U-Recall：未知類別的召回率。（SFUOD, p.6）
- H-Score：Known mAP 與 U-Recall 的調和平均 = 2·A·B / (A+B)。（SFUOD, p.6）
  - 驗算例：2×32.32×10.59 / (32.32+10.59) = 15.95。（SFUOD, Table 1, p.6）
- 只認已知、完全不找未知（U-Recall=0）→ H-Score=0，例如 Source only。（SFUOD, Table 1, p.6）

## 相關
[[open-set-detection]] · [[sfuod-2025]]
