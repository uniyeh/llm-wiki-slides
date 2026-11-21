---
title: 偽標籤（Pseudo-label）
type: concept
tags: [self-training]
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025]
updated: 2026-11-21
summary: 模型自己出的參考答案
order: 50
---
# 偽標籤（Pseudo-label）

## 白話版
沒有標準答案時，讓模型自己先猜一份答案，再拿「比較有把握的猜測」當作答案來練習。風險是：猜錯的也會被當成正解，越練越歪。

## 重點
- 在 [mean-teacher](mean-teacher.md) 中由老師模型產生，只保留信心高於門檻的框。（DSOD, p.3）
- 早期 SFOD 方法 SED 用熵（entropy）搜尋門檻來篩選較可靠的偽標籤。（DSOD, p.2）
- 偽標籤錯誤會在自我訓練中累積（error accumulation）。（DSOD, p.1）
- DSOD 也拿偽標籤框做成熱圖，標出「哪裡是物體」。（DSOD, p.5）
- 交叉熵損失梯度無上限，一個錯的偽標籤就可能主導訓練；FALCON 的 IRPL 讓師生一致的簡單框少學、不一致的框保留修正訊號。（FALCON, p.4）
- 未知物體的偽標籤更難：老師沒學過就給不出來；SFUOD 用 PAUL（主軸投影判斷「像不像物體」）解決。（SFUOD, p.5）→ [collaborative-tuning-paul](collaborative-tuning-paul.md)
- 容易混淆的類別（卡車↔公車）會產生錯誤偽標籤；CGA 用 CLIP＋混淆提示詞產生更細的軟標籤。（CGA, p.2, p.5）→ [class-confusion](class-confusion.md)
- 有些圖過門檻後完全沒有偽標籤，就浪費了；TTAOD-F 從記憶庫貼入高信心實例「製造」正樣本（Memory Hallucination）。（TTAOD-F, p.6）
- 偽標籤差的根源之一是特徵本身注意力分散，見 [attention-map](attention-map.md)。（FALCON, p.1）

## 相關
[source-bias](source-bias.md) · [source-free-adaptation](source-free-adaptation.md)
