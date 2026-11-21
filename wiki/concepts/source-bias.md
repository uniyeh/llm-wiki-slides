---
title: 來源偏差（Source Bias）
type: concept
tags: [problem]
sources: [dsod-2026]
updated: 2026-11-21
summary: 調整後仍偏向來源領域的核心問題
order: 40
---
# 來源偏差（Source Bias）

## 白話版
模型雖然在學新環境，但腦袋還是用舊環境的習慣在判斷，像搬到台北的人還一直用老家的路名找路。

## 重點
- 定義：調整後的模型仍偏向來源領域，導致泛化差，並在自我訓練中累積錯誤。（DSOD, p.1）
- 為什麼 SFOD 特別嚴重：UDA 能同時看兩個領域來學共通特徵；SFOD 只能看目標資料。（DSOD, p.1–2）
- 對策之一：引入不偏向任何領域的 [vision-foundation-model](vision-foundation-model.md)（DSOD）。

## 和[領域落差](domain-shift.md)有什麼不同？
| | 領域落差 | 來源偏差 |
|---|---|---|
| 是誰的問題 | **資料**：訓練環境 ≠ 使用環境（DSOD, p.1） | **模型**：調整後仍偏向來源領域（DSOD, p.1） |
| 何時出現 | 一換環境就有 | 在「調整」的過程中留下的後遺症 |
| 比喻 | 考題變了 | 換了考題，卻改不掉舊解法 |
| 為何 SFOD 特別嚴重 | — | 只看得到新資料、無法同時對照新舊資料學共通特徵；錯誤還會在自我訓練中累積（DSOD, p.1–2） |

## 相關
[pseudo-label](pseudo-label.md) · [mean-teacher](mean-teacher.md) · [dsod-2026](../sources/dsod-2026.md)
