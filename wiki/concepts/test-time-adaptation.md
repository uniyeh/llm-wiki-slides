---
title: 測試時調整（Test-Time Adaptation, TTA）
type: concept
tags: [core, tta]
sources: [ttaod-f-2025, vlod-tta-2026]
aliases: [TTA, TTAOD, 邊用邊學]
updated: 2026-11-21
summary: 邊用邊學（TTA）與 SFOD 的差別
order: 150
---
# 測試時調整（TTA）——邊用邊學

## 白話版
SFOD 像「轉學前先拿新學校的考古題自習一段時間」；TTA 則是「直接上考場，一邊寫一邊調整答題策略」。兩者都沒有原本的課本，差別在什麼時候調整。

## 與 SFOD 的差別
| | SFOD（[[source-free-adaptation]]） | TTA |
|---|---|---|
| 來源資料 | 不用 | 不用（理想上）（TTAOD-F, p.2） |
| 何時調整 | 上線前，拿一批目標資料離線訓練多輪 | 上線時，邊推論邊即時調整（TTAOD-F, p.1） |
| 看到資料的方式 | 可以反覆看整批 | 資料流，一批一批來（TTAOD-F, p.3） |
| 在意的成本 | 訓練時間 | **推論速度、記憶體**（TTAOD-F, Table 9, p.14） |

## 重點
- TTA 偵測（TTAOD）早期方法其實會用來源資料的統計量，並假設類別相同；TTAOD-F 用[[vision-language-detector|圖文偵測器]]擺脫兩者。（TTAOD-F, p.1–3）
- 常用基準：影像損壞（Pascal-C、COCO-C）、跨資料集（ODinW-13）。→ [[benchmarks]]

## 兩篇 TTA 論文的路線
| | [[ttaod-f-2025]] | [[vlod-tta-2026]] |
|---|---|---|
| 調整目標 | [[mean-teacher]] 偽標籤 | [[entropy-minimization|IoU 加權熵]] |
| 調什麼 | 文字＋影像[[prompt-tuning|提示]] | [[adapter]]＋文字殘差 |
| 是否跨圖累積 | 是（老師持續更新、記憶庫） | 否，每張圖調一步後重置 |
| 適用偵測器 | Transformer（Grounding DINO） | Transformer 與 CNN（YOLO-World） |
| COCO-C mAP / 記憶體 / 延遲 | 26.0 / 11.37 GB / 701.9 ms | 26.2 / 3.76 GB / 531.6 ms |
（TTAOD-F, p.4–6；VLOD-TTA, p.6–8, Table 5, p.11）

## 相關
[[ttaod-f-2025]] · [[prompt-tuning]] · [[mean-teacher]]
