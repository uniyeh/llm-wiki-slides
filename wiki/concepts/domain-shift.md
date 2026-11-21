---
title: 領域落差（Domain Shift）
type: concept
tags: [basics]
sources: [dsod-2026]
updated: 2026-11-21
---
# 領域落差（Domain Shift）

## 白話版
模型在「訓練時看到的世界」和「實際使用的世界」長得不一樣時，表現就會掉。好比一個只在晴天白天練車的新手，第一次在濃霧夜晚上路，會認不出路標。

## 重點
- 定義：訓練資料（**來源領域 source domain**）與測試資料（**目標領域 target domain**）分布不同，導致效能大幅下降。（DSOD, p.1）
- 常見類型（見 [[benchmarks]]）：天氣（晴→霧）、場景（城市 A→城市 B）、合成→真實（遊戲畫面→實拍）。
- 例：晴天訓練的偵測器在霧天只有 29.5 mAP，若用霧天標註重訓可達 48.7。（DSOD, Table 1, p.8）

## 解法家族
- 有來源資料：UDA（非監督式領域自適應）→ 見 [[source-free-adaptation]]
- 沒有來源資料：SFOD / SFDA → 見 [[source-free-adaptation]]

## 相關
[[source-bias]] · [[object-detection]]
