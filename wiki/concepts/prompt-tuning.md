---
title: 提示調整（Prompt Tuning）
type: method
tags: [parameter-efficient]
sources: [ttaod-f-2025, cga-2026, vlod-tta-2026]
updated: 2026-11-21
---
# 提示調整（Prompt Tuning）

## 白話版
不改大模型的「大腦」，只調它前面的一小段「便條紙」（幾個可學的數字向量），就能讓它適應新任務。好處是便宜、快，而且不容易把原本會的東西忘掉。

## 重點
- 屬於參數高效微調：只更新提示，其餘參數凍結。（TTAOD-F, p.4–5；CGA, p.3）
- **文字提示**：加在文字 token 上。（TTAOD-F, Eq. 1, p.4）；CGA 只微調文字提示（CoOp 方式）。（CGA, p.3）
- **影像提示**：在影像編碼器每層加幾個可學 token。（TTAOD-F, Eq. 2–3, p.4）
- 只調文字不夠（+0.6），只調影像若初始化不好會變差（−3.4）；用第一張測試圖初始化（Warm-start）後兩者互補。（TTAOD-F, Table 3, p.8）
- 提示太多會過擬合（m>30 下降）。（TTAOD-F, Table 4, p.9）

## 提示挑選（不訓練提示，而是挑）
- VLOD-TTA 每類 16 句 GPT 提示，依本圖相容度保留前 25%；比全部平均好（+1.0 vs 部分下降）。（VLOD-TTA, p.6–8, Fig. 5a）
- 另一種參數高效方式：[[adapter]]。

## 和[[adapter|轉接器]]有什麼不同？
| | 提示調整 | 轉接器 |
|---|---|---|
| 調哪裡 | 輸入端加幾個可學向量（文字或影像 token）（TTAOD-F, p.4） | 模型「層與層之間」插小模組（VLOD-TTA, p.7） |
| 共同點 | 大模型凍結、只調少量參數 | 同左 |
| 本 wiki 例子 | TTAOD-F、CGA | VLOD-TTA（約 0.89M 參數，Table 5, p.11） |

## 相關
[[vision-language-detector]] · [[vision-language-model]] · [[ttaod-f-2025]]
