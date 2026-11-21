---
title: SFOD 方法家族總覽
type: concept
tags: [overview, synthesis]
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
summary: SFOD 方法家族總覽
order: 60
---
# SFOD 方法家族總覽

## 白話版
大家都想解決「沒課本、只有筆記，怎麼自學新考題」，各派做法不同：有的改善「自己出的參考答案」品質，有的請外援（通才模型），有的改變師生互動規則。

## 家族
1. **偽標籤篩選／修正**：SED（熵門檻）、LPLD 等。（DSOD, p.2–3）；FALCON 的 IRPL 改用抗雜訊損失而非只篩選。（FALCON, p.4）
2. **師生框架改良**：PETS（動態＋靜態多老師）、DRU（動態重訓）、DDT（非對稱權重更新）。（DSOD, p.2–3）；SF-UT 用初始老師的固定偽標籤＋AdaBN。（SFUOD, p.3）
3. **特徵／關係學習**：A2SFOD（分成像來源／不像來源兩群）、IRG（實例關係圖＋對比學習）。（DSOD, p.2）；Simple-SFOD 證明精心設計的自我訓練可勝過複雜架構；SF-YOLO 用於 YOLO 偵測器。（FALCON, p.2）
4. **VFM 輔助**：[dsod-2026](../sources/dsod-2026.md)（注入 DINOv2 特徵＋規範）、[falcon-sfod-2026](../sources/falcon-sfod-2026.md)（OV-SAM 遮罩規範[注意力](attention-map.md)＋抗雜訊損失）。比較見 [method-comparison](../comparisons/method-comparison.md)。

5. **擴展問題設定：開放集合**：[sfuod-2025](../sources/sfuod-2025.md)（已知類別適應＋未知物體偵測）。

6. **另一條路：邊用邊學（TTA）**：[ttaod-f-2025](../sources/ttaod-f-2025.md)（圖文偵測器＋提示調整＋記憶庫）、[vlod-tta-2026](../sources/vlod-tta-2026.md)（IoU 加權熵＋提示挑選，免老師、更省）；舊 TTA 偵測方法 STFAR、CTTOD 等需來源統計量。（TTAOD-F, p.3）→ [test-time-adaptation](test-time-adaptation.md)
7. **延伸：分類版 SFDA**：[cga-2026](../sources/cga-2026.md)（CLIP＋混淆提示詞）；相關前作 DIFO、ProDe 也用 CLIP。（CGA, p.3）


## 相關
術語總表：[glossary](../glossary.md)

[source-free-adaptation](source-free-adaptation.md) · [mean-teacher](mean-teacher.md)
