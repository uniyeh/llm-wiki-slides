---
title: 圖文偵測器（Vision-Language Object Detector, 如 Grounding DINO）
type: concept
tags: [vlm, detector, open-vocabulary]
sources: [ttaod-f-2025, vlod-tta-2026]
aliases: [VLOD, Grounding DINO, GLIP, open-vocabulary detector]
updated: 2026-11-21
summary: 看得懂文字的偵測器（Grounding DINO、YOLO-World）
order: 170
---
# 圖文偵測器（Grounding DINO 等）

## 白話版
看得懂文字指令的物件偵測器：你打「飛機. 腳踏車. 鳥.」，它就在圖裡把這些東西框出來；想換類別就改文字，不必重新訓練。這叫「開放詞彙」。

## 重點
- 在大規模網路圖文配對上預訓練，零樣本表現強。（TTAOD-F, p.3）
- 代表：GLIP、Grounding DINO（把圖文預訓練融入 Transformer 偵測器 DINO）。（TTAOD-F, p.3）
- Grounding DINO 的文字輸入：類別名稱用句點串起來，例如 "aeroplane. bicycle. bird."，最多 256 個 token。（TTAOD-F, p.4）
- 不調整直接用，在 Pascal-C 已有 44.8 AP50，與舊 SOTA 方法 STFAR（45.2）相當。（TTAOD-F, Table 1, p.7–8）
- 仍會因分布轉移而退步，所以需要 [[test-time-adaptation]]。（TTAOD-F, p.4）
- YOLO-World：CNN 架構、為即時開放詞彙偵測設計。（VLOD-TTA, p.4）
- 運作：候選框特徵與類別文字特徵算 cosine 相似度當分數。（VLOD-TTA, Eq. 1, p.5）
- 提示詞措辭很敏感；多句平均不一定有效，依圖挑選較好。（VLOD-TTA, p.6, Fig. 5a, p.13）
- 屬於 [[vision-language-model]] 在偵測上的延伸。

## 相關
[[ttaod-f-2025]] · [[prompt-tuning]] · [[open-set-detection]]
