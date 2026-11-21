---
title: 極端領域落差（照片↔插畫、可見光↔紅外線）
type: concept
tags: [benchmark]
sources: [falcon-sfod-2026]
updated: 2026-11-21
summary: 照片↔插畫、可見光↔紅外線
order: 120
---
# 極端領域落差

## 白話版
不只是晴天變霧天，而是「整個看世界的方式都變了」：從真實照片換成卡通插畫，或從一般相機換成只看得到熱度的紅外線相機。

## 重點
- Pascal VOC→Clipart（真實→插畫）：基線 33.6 → FALCON 35.5 mAP。（FALCON, Table 3, p.7）
- FLIR 可見光→紅外線、紅外線→COCO：都提升約 2 mAP。（FALCON, Table 4, p.7）

## 相關
[domain-shift](domain-shift.md) · [benchmarks](benchmarks.md)
