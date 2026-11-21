---
title: TTAOD-F — Test-Time Adaptive Object Detection with Foundation Model
type: source
tags: [tta, vision-language-detector, grounding-dino, prompt-tuning, mean-teacher, memory]
sources: [ttaod-f-2025]
raw: raw/TTAOD-F_Test-Time_Adaptive_Object_Detection_Foundation_Model_NeurIPS2025_[AW].pdf
venue: NeurIPS 2025
slide-role: 正式內容「另一條路：邊用邊學（TTA）」1 頁（使用者決策 2026-11-21）
updated: 2026-11-22
---
# TTAOD-F（NeurIPS 2025）

## 一句話摘要
第一個用基礎模型做「邊用邊學」物件偵測的方法：以圖文偵測器 Grounding DINO 為底，只調少量文字＋影像提示，再用「記憶庫」保存有把握的例子來校正判斷、補足沒有參考答案的圖片。（TTAOD-F, p.1–3）

## 要解決的問題
- [[test-time-adaptation|TTA]]：在推論時即時調整，比離線的 UDA 更貼近自駕、機器人等真實需求。（TTAOD-F, p.1）
- 既有 TTA 偵測方法（多以 Faster R-CNN 為底）的兩個問題（TTAOD-F, Fig. 1, p.1–2）：
  1. 需要來源資料的統計量（特徵平均、變異數）→ 違反無來源原則。
  2. 假設來源與目標類別相同（[[open-set-detection|封閉集合]]）。
- 直接全參數微調大模型：會削弱泛化能力、對雜訊樣本敏感；且每批都要有可靠[[pseudo-label|偽標籤]]很難。（TTAOD-F, p.2）

## 方法（白話＋技術）
**白話**：拿一位「看得懂文字指令」的通才偵測員上工，不改它的大腦，只調它的「便條紙」（提示）；同時讓它帶一本筆記本，記下每類最有把握的例子，遇到拿不準的就翻筆記比對，遇到完全沒把握的照片，就把筆記裡的例子貼上去當練習題。

**技術**（Grounding DINO Swin-T，p.3, p.7）：
1. **Multi-modal Prompt-based Mean-Teacher**（p.4–5）→ [[prompt-tuning]]
   - 文字提示 P_T 加在文字 token 上（初始 0）；影像提示：每層 Transformer 加 m=10 個可學 token。（p.4, p.7）
   - **Test-time Warm-start**：用第一張測試圖各層 image token 的平均值初始化影像提示，避免零／隨機初始化導致偵測崩潰。
   - 只更新提示，其餘凍結；老師提示以 EMA（γ=0.999）跟隨學生；偽標籤門檻 0.3。（p.5, p.7）
2. **Instance Dynamic Memory（IDM）**：每類一個佇列（最多 20 個），存高信心框的裁切圖＋DINOv2 特徵＋分數；滿了就替換最低分者。（p.5–6）
   - **Memory Enhancement**：用各類 DINOv2 特徵原型對高信心預測重新加分（免訓練）。（Eq. 9, p.6）
   - **Memory Hallucination**：沒有可用偽標籤的圖，從記憶隨機貼最多 3 個實例進去製造正樣本。（p.6）

## 實驗設定（資料集、指標）
- Pascal-C（Pascal VOC 測試集 × 15 種影像損壞，20 類，AP50）；COCO-C（COCO val2017 × 15 種損壞，80 類，mAP）；ODinW-13（13 個不同領域、不同類別的資料集）。（p.6–7）→ [[benchmarks]]
- Grounding DINO 以 Objects365、GoldG、Cap4M 預訓練，**未在來源資料上微調**；單張 RTX 3090。（p.7）

## 主要結果（已驗算：15 種損壞平均與 Avg 欄一致）
| 基準 | 舊方法最佳（Faster R-CNN） | GD 直接用 | GD + Mean Teacher | **TTAOD-F** | 來源 |
|---|---|---|---|---|---|
| Pascal-C（AP50） | 45.2（STFAR） | 44.8 | 51.5 | **56.2** | Table 1, p.7 |
| COCO-C（mAP） | 25.3（STFAR, R-101） | 20.6 | 24.1 | **26.0** | Table 2, p.7 |
| ODinW-13（mAP） | — | 52.8 | 53.1（內文「+0.3」推算） | **54.2** | Fig. 4, p.8 |

- COCO-C 15 種損壞中 8 種最佳（自算驗證一致）。（Table 2, p.7–8）
- 消融（Pascal-C）：只調文字 45.4（+0.6）；只調影像 41.4（−3.4）；影像＋Warm-start 53.4；再加文字 53.9；再加 MH 54.9；全部（再加 ME）56.2；只用 ME（免訓練）46.1。（Table 3, p.8）
- 影像提示數量：m 超過 30 開始下降，m=10 最佳。（Table 4, p.9）

## 限制
- **推論變慢**：每張 213.1 ms（直接用）→ 693.8 ms（TTAOD-F），約 3.3 倍；Mean Teacher 版 635.0 ms。（Table 9, p.14）
- 與 Faster R-CNN 舊方法的比較不完全公平（偵測器不同），作者自承；公平比較是 GD+MT 51.5 → 56.2。（p.8）
- ODinW 中 Mushrooms、Packages 沒進步：測試圖太少（5 張、4 張）。（p.8）
- 「完全不需來源資料」指不需要特定來源領域資料；Grounding DINO 本身仍在大規模網路資料上預訓練。（p.7）

## 設計決策與消融證據
| 設計 | 為什麼 | 證據 |
|---|---|---|
| 只調提示（凍結大模型） | 全參數微調削弱泛化、對雜訊敏感、資料少易過擬合 | （p.2） |
| 文字＋影像提示 | 只調文字不足以適應 | 只文字 45.4、只影像 41.4、影像＋Warm-start 53.4、三者 53.9（Table 3, p.8） |
| Test-time Warm-start | 零或隨機初始化會讓影像分支退化甚至偵測崩潰 | 41.4 → 53.4（Table 3, p.8；p.5） |
| 記憶庫容量 20 | 太小原型不具代表、貼圖過擬合；太大混入雜訊 | （Fig. 5, p.9） |

## 作者提到的限制與未來方向
- NeurIPS 檢查表「限制」一欄作者填 NA，稱無明顯限制。（p.18）
- wiki 整理的實際限制見上方「限制」段（延遲約 3.3 倍等）。

## 矛盾
- 未發現內文與表格矛盾。

## 和其他論文的關係
- 與 SFOD 論文（[[dsod-2026]]、[[falcon-sfod-2026]]）同樣不用來源資料、同樣用 [[mean-teacher]]；差別是「上線時即時調整」vs「事前離線調整」。見 [[test-time-adaptation]]。
- 與 [[sfuod-2025]] 一樣擺脫封閉集合假設，但做法是靠[[vision-language-detector|圖文偵測器]]的開放詞彙能力。
- 與 [[dsod-2026]] 一樣用 DINOv2，但用途不同：這裡只拿來算記憶庫特徵相似度。
- [[vlod-tta-2026]] 確認批評本篇：老師模型＋額外前向傳遞＋DINOv2 記憶造成開銷；同準確度下 VLOD-TTA 記憶體 3.76 vs 11.37 GB。（VLOD-TTA, p.4, Table 5, p.11）
