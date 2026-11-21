---
title: 協作調整（Collaborative Tuning）與 PAUL
type: method
tags: [open-set, unknown-labeling]
sources: [sfuod-2025]
updated: 2026-11-21
summary: SFUOD 的協作調整與未知標註
order: 220
---
# 協作調整與 PAUL（CollaPAUL）

## 白話版
- **協作調整**：原本的模型帶著舊環境的經驗，另外加一個「只看新環境」的助手，兩者一起討論再下判斷，避免舊經驗把已知和未知搞混。
- **PAUL**：車、卡車、公車雖然不同，但都「像個物體」。先找出已知物體的共同特徵方向，再看其他候選框在這個方向上像不像——像的就是「不認識的物體」，不像的就是背景。

## 技術重點
- 目標編碼器：激活最高的 top-k 特徵 → SVD 只保留前 r 個主成分重建 → cross-attention + MLP。（SFUOD, p.4）
- 協作層：cross-domain attention 讓同一組 object query 同時看來源與目標特徵；插在前 L 層解碼器，L=3 最佳。（SFUOD, p.4–5, Table 4, p.7）
- PAUL：objectness 分數 = 投影到已知主軸後的 cosine 相似度平均；門檻 δ = 已知分數平均；unknown 遮罩 = objectness 遮罩 ∪ 信心遮罩。（SFUOD, Eq. 7–11, p.5–6）
- 效果：cross-domain attention 優於 prefix-tuning（H 15.95 vs 12.57）；PAUL 優於只用信心或注意力挑未知（U-Recall 10.59 vs 3.56 / 4.00）。（SFUOD, Table 6–7, p.7）

## 相關
[open-set-detection](open-set-detection.md) · [pseudo-label](pseudo-label.md) · [sfuod-2025](../sources/sfuod-2025.md)
