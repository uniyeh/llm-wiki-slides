---
title: 視覺基礎模型（Vision Foundation Model, VFM）
type: concept
tags: [vfm, dinov2]
sources: [dsod-2026, falcon-sfod-2026, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
---
# 視覺基礎模型（VFM）

## 白話版
用海量、各式各樣圖片訓練出來的「通才」視覺模型。它不專精某一份工作，但看過的世界夠多，所以不容易被特定環境誤導。像見多識廣的顧問。

## 重點
- 例：DINOv2（通用特徵擷取）；也有做分割的模型。（DSOD, p.3）
- 用在 SFOD 的兩個好處：**語意互補**（VFM 給通用特徵、來源模型給類別細節）與**正則化效果**（凍結的 VFM 阻止模型過度貼合來源特徵）。（DSOD, p.1）
- 整合方式：當輔助骨幹，或當主骨幹加轉接器。（DSOD, p.3）
- 代價：多一個大模型，運算成本上升 → 可用[[knowledge-distillation]]移除。（DSOD, p.6）

## 兩種借用方式
| | 借什麼 | 推論時需要 VFM？ |
|---|---|---|
| [[dsod-2026]] | DINOv2 的特徵，直接加進模型 | 需要（Distill 版不用）（DSOD, p.4, p.6） |
| [[falcon-sfod-2026]] | [[segmentation-model|OV-SAM]] 的物體遮罩，只當規範 | 不需要，遮罩事先算好（FALCON, p.2–3） |
| [[ttaod-f-2025]]（TTA） | Grounding DINO 本身當偵測器＋DINOv2 算記憶庫相似度 | 需要（它就是偵測器）（TTAOD-F, p.3, p.6） |
| [[vlod-tta-2026]]（TTA） | YOLO-World / Grounding DINO 本身當偵測器 | 需要（它就是偵測器）（VLOD-TTA, p.8） |
| [[cga-2026]]（分類） | [[vision-language-model|CLIP]] 的圖文知識：出參考答案＋特徵對齊 | CLIP 參與訓練；推論用舊模型（CGA, p.3–5） |

## 相關
[[source-bias]] · [[dsod-2026]]
