---
title: 知識蒸餾（Knowledge Distillation）
type: method
tags: [deployment]
sources: [dsod-2026]
updated: 2026-11-21
summary: 大模型教小模型
order: 210
---
# 知識蒸餾（Knowledge Distillation）

## 白話版
讓一個大而強的「老師模型」把會的東西教給小而快的「學生模型」，學生不必背著老師的大腦也能做得差不多好。

## 重點
- DSOD-Distill：已調好的 DSOD 當「靜態老師」，加上一般的 EMA 老師，雙老師在 loss 層級合併監督訊號，學生不含 DINOv2，推論沒有額外負擔。（DSOD, p.6）
- 效果：晴→霧 46.9 mAP，只比完整 DSOD 低約 1 點，仍贏過 DDT。（DSOD, p.7, Table 1）

## 和[[mean-teacher]]有什麼不同？
- Mean Teacher 的老師是學生自己的移動平均；蒸餾的老師是另一個訓練好的大模型。DSOD-Distill 同時用兩種老師。（DSOD, p.3, p.6）

## 相關
[[vision-foundation-model]] · [[dsod-2026]]
