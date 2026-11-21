---
title: 已知／未知物體（封閉集合 vs 開放集合）
type: concept
tags: [open-set, problem]
sources: [sfuod-2025]
aliases: [closed-set, open-set, unknown object]
updated: 2026-11-21
---
# 已知／未知物體：封閉集合 vs 開放集合

## 白話版
「封閉集合」像選擇題：答案一定在選項裡。「開放集合」像真實世界：可能出現選項外的東西，這時模型應該誠實說「我不認識，但這裡有個東西」，而不是硬猜成汽車。

## 重點
- 一般 SFOD 假設來源與目標類別相同（封閉集合），偵測不到未定義物體。（SFUOD, p.1）
- 相關設定：未知物體偵測、開放世界物件偵測（OWOD，加上持續學習）、AOOD（有來源資料的開放集合領域自適應）。（SFUOD, p.3）
- SFUOD = 無來源資料 + 開放集合：已知類別照常分類，所有未定義類別合併為一個「unknown」類。（SFUOD, p.3）
- 評估要同時看「已知的準確度」與「未知找回率」→ [[recall-and-h-score]]

## 相關
[[sfuod-2025]] · [[source-free-adaptation]]
