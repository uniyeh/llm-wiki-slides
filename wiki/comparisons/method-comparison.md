---
title: 方法比較
type: comparison
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
---
# 方法比較

## 白話版（延伸）
[[cga-2026]] 是圖片分類，不放進下表；它借用 CLIP，針對「容易搞混的類別」出更細的參考答案，與 DSOD、FALCON 同屬「借用通才模型」思路。

## 另一條路：邊用邊學（TTA）
| | [[ttaod-f-2025]] | [[vlod-tta-2026]] |
|---|---|---|
| 設定 | [[test-time-adaptation|TTA]]，上線時即時調整；開放詞彙（TTAOD-F, p.1–3） | 同左（VLOD-TTA, p.2） |
| 基礎 | [[vision-language-detector|Grounding DINO]]（Swin-T）（TTAOD-F, p.7） | YOLO-World-S 與 Grounding DINO-T（VLOD-TTA, p.8） |
| 調什麼 | 只調文字＋影像[[prompt-tuning|提示]]，大模型凍結（TTAOD-F, p.4–5） | [[adapter]]＋文字殘差；每張圖一步後重置（VLOD-TTA, p.7） |
| 調整訊號 | Mean Teacher＋記憶庫加分與貼圖（TTAOD-F, p.5–6） | [[entropy-minimization|IoU 加權熵]]＋提示挑選（VLOD-TTA, p.6–7） |
| 代價（vs 直接用） | 延遲約 3.3 倍（TTAOD-F, Table 9, p.14） | 延遲約 2.5 倍（VLOD-TTA, Table 5, p.11） |

## 白話版
大家面對同一個困境（沒課本、只有筆記、新考題），解法不同：DSOD 請通才顧問「一起答題」；FALCON 請通才事先畫重點，再自己練習。

| | [[dsod-2026]] | [[falcon-sfod-2026]] | [[sfuod-2025]] |
|---|---|---|---|
| 設定 | SFOD（[[source-free-adaptation]]） | SFOD | SFOD＋[[open-set-detection|未知物體]] |
| 認為的核心問題 | [[source-bias]]（DSOD, p.1） | 注意力散到背景、偽標籤雜訊與不平衡（FALCON, p.1–2） | 已知／未知知識混淆、未知偽標籤無效（SFUOD, p.2） |
| 基礎框架 | [[mean-teacher]] + Deformable-DETR（DSOD, p.3, p.7） | [[mean-teacher]]，以 Simple-SFOD 為基線（FALCON, p.6） | [[mean-teacher]] + Deformable-DETR，以 DRU 為基線（SFUOD, p.6） |
| 借用的基礎模型 | DINOv2（特徵）（DSOD, p.3） | OV-SAM（遮罩）（FALCON, p.3） | 無；加一個輔助目標編碼器（SFUOD, p.4） |
| 怎麼用 | 特徵相加融合＋前景特徵對齊（DSOD, p.4–5） | 注意力圖對齊遮罩＋抗雜訊損失（FALCON, p.3–4） | 協作調整＋主軸投影標未知（SFUOD, p.4–6） |
| 推論時需要基礎模型？ | 需要；Distill 版不需要（DSOD, p.6） | 不需要（FALCON, p.2） | 不適用 |
| 其他特色 | 自動挑融合權重（DAAW）（DSOD, p.5） | 理論誤差上界（FALCON, p.4–5）；少見類別進步大（FALCON, Table 8, p.8） | 提出新情境與兩個 benchmark（SFUOD, p.2） |
