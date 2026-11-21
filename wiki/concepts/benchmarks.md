---
title: 常用資料集與評估指標
type: dataset
tags: [benchmark, metric]
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
summary: Cityscapes / Foggy / BDD100k / Sim10k / KITTI、mAP
order: 260
---
# 常用資料集與評估指標

## 白話版
研究者用幾組固定的「考卷」比較方法好壞：例如拿晴天城市照片訓練，考霧天城市照片；分數用 mAP（框得準、認得對的平均比例，0–100）。

## 資料集（DSOD, p.7）
| 資料集 | 內容 |
|---|---|
| Cityscapes | 城市街景，8 類：person, rider, car, truck, bus, train, motorcycle, bicycle（FALCON, p.5） |
| Foggy Cityscapes | Cityscapes 加上合成霧，用最濃 0.02（DSOD, p.7） |
| BDD100k | 10 萬張多天氣、多時段行車影像；SFUOD 用白天子集 36,728 訓練／5,258 驗證（SFUOD, p.6） |
| Sim10k | 1 萬張電腦合成街景（取自遊戲 GTA），只標「車」（FALCON, p.6） |
| KITTI | 7,481 張真實街景訓練圖，用於跨相機任務（FALCON, p.5–6） |
| Pascal VOC → Clipart | 真實照片 → 插畫（FALCON, p.6） |
| FLIR | 可見光／紅外線熱影像（FALCON, p.6） |
| Watercolor / ClipArt / Comic | 水彩、插畫、漫畫風格（VLOD-TTA, p.8） |
| ExDark | 低光環境（VLOD-TTA, p.8） |
| Pascal-C | Pascal VOC 測試集加 15 種影像損壞（雜訊、模糊、天氣、數位），每種 4,956 張、20 類（TTAOD-F, p.6） |
| COCO-C | COCO val2017（5k 張）加 15 種損壞，80 類（TTAOD-F, p.6–7） |
| ODinW-13 | 13 個不同領域資料集（無人機、水族館、兔子、手、蘑菇、包裹、VOC、手槍、坑洞、浣熊、貝類、熱影像、車輛），類別各不同（TTAOD-F, p.7） |

## 常見任務（DSOD, p.7）
- 晴 → 霧：Cityscapes → Foggy Cityscapes
- 跨場景：Cityscapes → BDD100k
- 合成 → 真實：Sim10k → Cityscapes
- 跨相機：KITTI → Cityscapes（FALCON, p.6）
- 極端落差：見 [[extreme-domain-shift]]
- 影像損壞（TTA 常用）：Pascal-C、COCO-C；跨資料集：ODinW-13（TTAOD-F, p.6–7）

## 矛盾
- Cityscapes 訓練張數：DSOD（p.7）、FALCON（p.5）寫 2,925；SFUOD 寫 2,975（p.6）。**使用者判定 SFUOD 寫錯**（2026-11-21）。簡報不引用。

## 指標
- **mAP@0.5**：預測框與正解重疊（IoU）≥ 0.5 才算對，各類別平均精確度再取平均。（DSOD, p.7）
- **Source only**＝不做調整的下限；**Oracle**＝用目標標註訓練的上限。（DSOD, p.7）
- 開放集合任務另有 Known mAP、U-Recall、H-Score → [[recall-and-h-score]]
- ⚠️ 不同論文的 Source only 不同（C→F：DSOD 29.5、FALCON 25.2），因基線偵測器不同，跨論文請比「進步幅度」。（DSOD, Table 1, p.8；FALCON, Table 1, p.6）

## 相關
[[domain-shift]] · [[object-detection]]
