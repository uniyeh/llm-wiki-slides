---
title: 無來源領域自適應（Source-Free Domain Adaptation / SFOD）
type: concept
tags: [core, sfod, uda]
sources: [dsod-2026, sfuod-2025, cga-2026, ttaod-f-2025]
aliases: [SFOD, SFDA, SF-DAOD]
updated: 2026-11-21
---
# 無來源領域自適應（SFDA / SFOD）

## 白話版
換到新環境時，模型要自己適應，但**原本的訓練資料拿不到了**——只剩「舊模型」和「一堆沒有答案的新照片」。就像轉學生只帶著前一間學校的筆記，課本和老師都沒了，只能靠筆記自學新學校的考題。

## 為什麼拿不到來源資料？
- 資料儲存成本、隱私、運算資源等實務限制。（DSOD, p.1）
- 隱私、安全、智慧財產；例：醫療影像、生物特徵、金融紀錄不能外流。（CGA, p.1）

## 與相近設定比較
| 設定 | 來源資料 | 目標標註 | 何時調整 |
|---|---|---|---|
| UDA / UDAOD | ✅ 有 | ❌ | 事前離線 |
| **SFOD（本主題）** | ❌ 無，只有來源模型 | ❌ | 事前離線 |
| TTA / TTAOD | ❌ 無 | ❌ | 上線時即時（TTAOD-F, p.1） |
（DSOD, p.1–3）→ TTA 詳見 [[test-time-adaptation]]

## 正式定義
來源資料 D_s = {X_s, Y_s}、目標資料 D_t = {X_t}（無標註）。目標：把在 D_s 上預訓練的偵測器 G 調整到 D_t。兩大挑戰：目標無標註、來源資料不可取得。（DSOD, p.3）

## 主流做法
多數方法採自我訓練（self-training），尤其是 [[mean-teacher]] + [[pseudo-label]]。（DSOD, p.2）
→ 方法分類見 [[sfod-method-families]]。

## 分類版 SFDA
- 同樣設定也用在[[image-classification|圖片分類]]，例：[[cga-2026]]。多數方法依賴「同類樣本會聚在一起」的假設，細粒度時失效。（CGA, p.2）

## 隱含假設：封閉集合
- 一般 SFOD 假設新環境只會出現來源學過的類別；[[sfuod-2025]] 放寬成「也要找出未知物體」。（SFUOD, p.1）→ [[open-set-detection]]

## 主要難題
[[source-bias]] · 偽標籤雜訊（見 [[pseudo-label]]）

## 相關
[[domain-shift]] · [[benchmarks]] · [[dsod-2026]]
