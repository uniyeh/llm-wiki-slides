---
title: Index
type: index
updated: 2026-11-21
---
# SF-DAOD Wiki 目錄

## Sources（論文）
- [[dsod-2026]] — 用 DINOv2 特徵注入＋前景規範，減輕 SFOD 的來源偏差；附輕量蒸餾版
- [[sfuod-2025]] — 新情境：無來源資料＋偵測未知物體；CollaPAUL 協作調整＋主軸投影標未知
- [[vlod-tta-2026]] — （TTA）免老師的 IoU 加權熵＋提示挑選，同準確度、記憶體約 1/3
- [[ttaod-f-2025]] — （TTA）第一個用圖文偵測器做邊用邊學：提示調整＋記憶庫
- [[cga-2026]] — （分類，延伸）CLIP＋混淆提示詞處理不對稱類別混淆
- [[falcon-sfod-2026]] — 用 OV-SAM 遮罩把注意力拉回物體＋抗雜訊、顧及少數類別的損失

## Concepts（概念）
- [[object-detection]] — 找出「有什麼、在哪裡」
- [[domain-shift]] — 訓練環境≠使用環境，效能下滑
- [[source-free-adaptation]] — 沒有來源資料下的自適應（SFOD/SFDA）定義與比較
- [[source-bias]] — 調整後仍偏向來源領域的核心問題
- [[pseudo-label]] — 模型自己出的參考答案
- [[vision-foundation-model]] — 見多識廣的通才模型（DINOv2 等）
- [[sfod-method-families]] — SFOD 方法家族總覽
- [[attention-map]] — 模型在看哪裡
- [[segmentation-model]] — 描輪廓的模型（OV-SAM）
- [[class-imbalance]] — 類別多寡不均、長尾
- [[extreme-domain-shift]] — 照片↔插畫、可見光↔紅外線
- [[open-set-detection]] — 已知／未知物體，封閉 vs 開放集合
- [[class-confusion]] — 類別容易認錯且有方向性
- [[vision-language-model]] — 圖文模型 CLIP、提示詞
- [[image-classification]] — 分類 vs 偵測
- [[test-time-adaptation]] — 邊用邊學（TTA）與 SFOD 的差別
- [[vision-language-detector]] — 看得懂文字的偵測器（Grounding DINO、YOLO-World）
- [[candidate-box-iou]] — 候選框與重疊程度

## Methods（方法）
- [[mean-teacher]] — 師生自我訓練框架（EMA 老師）
- [[detr]] — Transformer 偵測器（Deformable-DETR）
- [[knowledge-distillation]] — 大模型教小模型
- [[collaborative-tuning-paul]] — SFUOD 的協作調整與未知標註
- [[prompt-tuning]] — 只調便條紙的參數高效微調
- [[entropy-minimization]] — 讓模型更果斷的調整目標
- [[adapter]] — 插入小轉接頭的參數高效微調

## 術語
- [[glossary]] — 全部術語的中英對照與白話

## Comparisons（比較）
- [[method-comparison]] — 各論文方法並列
- [[results-comparison]] — 各論文結果與進步幅度
- [[ideas]] — （SYNTHESIZE）延伸發想總表：作者未來方向、交叉發想、共同盲點、建議加讀論文
- [[cga-ideas-for-detection]] — （發想）把 CGA 的混淆提示帶回偵測

## Datasets & Metrics
- [[benchmarks]] — Cityscapes / Foggy / BDD100k / Sim10k / KITTI、mAP
- [[recall-and-h-score]] — 開放集合指標
