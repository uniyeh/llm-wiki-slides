---
title: 候選框與重疊程度（Proposals & IoU）
type: concept
tags: [basics, detection]
sources: [vlod-tta-2026, dsod-2026]
updated: 2026-11-21
---
# 候選框與重疊程度（IoU）

## 白話版
偵測器不是一次就畫出完美的框，而是先畫出成百上千個「可能有東西」的候選框，再挑出好的。**IoU** 是兩個框重疊多少（0＝完全不重疊、1＝完全重合）。很多框擠在同一處互相重疊，代表很多意見都同意「這裡有東西」。

## 重點
- 候選框數量：YOLO-World 約 8,400 個、Grounding DINO 約 900 個；後處理（門檻、NMS）會刪掉大多數。（VLOD-TTA, p.6）
- 互相重疊、同類別的一群框較可能是真物體；零散的框通常不可靠。（VLOD-TTA, p.6）
- mAP@0.5 就是用 IoU ≥ 0.5 判斷預測框算不算對。（DSOD, p.7）→ [[benchmarks]]
- VLOD-TTA 的 IWE 依「所屬重疊群大小」加權。（VLOD-TTA, Eq. 3, p.6）

## 相關
[[object-detection]] · [[entropy-minimization]] · [[vlod-tta-2026]]
