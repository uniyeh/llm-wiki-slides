---
title: SFUOD — Source-Free Unknown Object Detection
type: source
tags: [sfod, open-set, unknown-detection, mean-teacher, deformable-detr]
sources: [sfuod-2025]
raw: raw/SFUOD_Source-Free_Unknown_Object_Detection_ICCV2025_[AW].pdf
venue: ICCV 2025
updated: 2026-11-22
---
# SFUOD / CollaPAUL（ICCV 2025）

## 一句話摘要
提出新情境 SFUOD：沒有來源資料的情況下，模型不只要適應新環境認得「學過的東西」，還要把「沒學過的東西」框出來標成「不認識」；方法 CollaPAUL 用協作調整減少新舊知識混淆，用主軸投影替未知物體貼偽標籤。（SFUOD, p.1–2）

## 要解決的問題
- 一般 SFOD 是「封閉集合」假設：新環境只會出現來源領域定義過的類別，因此偵測不到未定義的物體。（SFUOD, p.1）→ 見 [[open-set-detection]]
- 實務需要：自駕車要能發現行人、動物等未預期物體以避免事故。（SFUOD, p.1）
- 現有 SFOD 方法套到這個情境的兩大困難（SFUOD, p.2）：
  1. **知識混淆**：來源知識讓已知與未知互相誤判，連已知物體也學更差。
  2. **未知偽標籤無效**：老師沒學過未知物體，給不出可靠的[[pseudo-label|偽標籤]]。

## 方法（白話＋技術）
**白話**：原本的模型只認得車。CollaPAUL 加派一個「只看新環境的助手」和原模型一起討論，避免舊經驗把事情搞混；再利用「不管是車還是行人，都『長得像個東西』，背景則不像」這個共通點，把沒見過的東西挑出來、標成「不認識」。

**技術**（建立在 DRU + [[detr|Deformable-DETR]] + [[mean-teacher]] 上，p.6）→ 細節見 [[collaborative-tuning-paul]]
1. **Collaborative tuning**：輔助目標編碼器（取激活最高的 top-k 特徵 → SVD 截斷重建 → cross-attention + MLP）提取「目標相依」知識；在解碼器前 L=3 層插入協作層，以 cross-domain attention 融合來源與目標特徵。（SFUOD, p.4–5, Table 4, p.7）
2. **PAUL（Principal Axis-based Unknown Labeling）**：已知 proposal 用信心門檻 0.3 標註；計算已知 proposal 特徵的主軸，把其餘 proposal 投影上去算「像物體程度」（objectness，cosine 相似度），高於已知平均者 ∪ 未知信心高於門檻者 → 標成 unknown。（SFUOD, Eq. 7–11, p.5–6）

## 實驗設定（資料集、指標）
- 天氣：Cityscapes → Foggy Cityscapes（霧 0.02）；跨場景：Cityscapes → BDD100K 白天子集（36,728 訓練／5,258 驗證）。（SFUOD, p.6）
- **已知類別**：Car、Truck、Bus；**未知類別**：Person、Rider、Motorcycle、Train、Bicycle。（SFUOD, p.6）
- 指標見 [[recall-and-h-score]]：Known mAP、U-Recall、H-Score。（SFUOD, p.6）
- AdamW、EMA α=0.99、4× RTX 3090。（SFUOD, p.6）

## 主要結果（已驗算：Known mAP＝三類平均、H-Score＝調和平均，皆一致）
| 任務 | 指標 | Source only | Mean Teacher | DRU | 最佳既有方法 | CollaPAUL | 來源 |
|---|---|---|---|---|---|---|---|
| 晴→霧 | Known mAP | 26.56 | 16.91 | 22.97 | 26.18（SF-UT） | **32.32** | Table 1, p.6 |
| 晴→霧 | U-Recall | 0.00 | 6.02 | 3.60 | 6.02（MT） | **10.59** | Table 1, p.6 |
| 晴→霧 | H-Score | 0.00 | 8.88 | 6.22 | 8.88（MT） | **15.95** | Table 1, p.6 |
| 城市→BDD | Known mAP | 24.41 | 26.42 | 17.24 | 26.68（SF-UT） | **28.21** | Table 2, p.6 |
| 城市→BDD | U-Recall | 0.00 | 6.08 | 6.86 | 6.86（DRU） | **8.57** | Table 2, p.6 |
| 城市→BDD | H-Score | 0.00 | 9.89 | 9.82 | 9.89（MT） | **13.15** | Table 2, p.6 |

- 消融（晴→霧，基線 DRU）：+Collab Known mAP 22.97→30.63；+PAUL U-Recall 3.60→6.46；兩者 32.32 / 10.59 / 15.95。（Table 3, p.7）
- 反直覺發現：基本 Mean Teacher 在此情境勝過 PET、DRU 等進階 SFOD 方法；作者認為進階方法讓老師更新太慢，學不到未知物體。（SFUOD, p.7）
- PAUL vs 只用信心：U-Recall 3.56 → 10.59。（Table 7, p.7）

## 限制
- 絕對分數仍低：未知物體約只找回 1/10（U-Recall 10.59）。（Table 1, p.6）
- 城市→BDD 的單一類別不是全部最佳：Car 不如 Mean Teacher（57.95 vs 59.68）、Bus 不如 SF-UT（9.40 vs 15.21）；三個總指標才是最佳。（Table 2, p.6）
- 所有未知類別合併成單一「unknown」，不分辨是什麼。（SFUOD, p.3）

## 設計決策與消融證據
| 設計 | 為什麼 | 證據 |
|---|---|---|
| 協作調整（輔助目標編碼器＋cross-domain attention） | 來源知識造成已知／未知混淆，需要不依賴來源的目標知識 | Known mAP 22.97 → 30.63（Table 3, p.7）；cross-domain 15.95 > prefix-tuning 12.57（H，Table 6, p.7） |
| 協作層插 3 層 | 從早期層插入以穩定傳遞 | L=3 最佳，L=4、5 下降（Table 4, p.7） |
| PAUL 主軸投影 | 老師沒學過未知，信心低；但未知與已知共享「物體性」 | U-Recall：只用信心 3.56、注意力 4.00、PAUL 10.59（Table 7, p.7） |

## 作者提到的限制與未來方向
- 「SFUOD 仍有改進空間」；期望為開放集合的領域自適應偵測提供新方向。（p.8）
- 相關方法無法直接套用：OpenDet 需監督學習、OW-DETR 需單一領域持續學習、SOMA 需來源資料。（p.11）

## 矛盾
- **Cityscapes 訓練張數**：SFUOD 寫 2,975 訓練／500 驗證、共 3,475（p.6）；[[dsod-2026]]（p.7）與 [[falcon-sfod-2026]]（p.5）寫 2,925。
  - **決策（使用者，2026-11-21）**：判定 SFUOD 寫錯。簡報不引用此數字。
- 內文說跨場景「在所有指標都超越基線」（p.7），但只對三個總指標成立，單一類別並非全勝（見「限制」）。

## 和其他論文的關係
- 與 [[dsod-2026]]、[[falcon-sfod-2026]] 不同：它們假設封閉集合，SFUOD 放寬成開放集合。見 [[method-comparison]]。
- 以 DRU 為基線（DSOD 也沿用 DRU 設定，DSOD, p.7）。
- 與 [[ttaod-f-2025]] 一樣想擺脫「來源與目標類別相同」的假設；TTAOD-F 靠[[vision-language-detector|圖文偵測器]]的開放詞彙達成。（TTAOD-F, p.2）
