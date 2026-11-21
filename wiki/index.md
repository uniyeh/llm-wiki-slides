---
title: Index
type: index
updated: 2026-11-22
generated-by: tools/build_index.py（請勿手改，改各頁 frontmatter 的 summary／order 後重跑）
---
# SF-DAOD Wiki 目錄

> 點檔名即可開啟。建議閱讀順序：[object-detection](concepts/object-detection.md) → [domain-shift](concepts/domain-shift.md) → [source-free-adaptation](concepts/source-free-adaptation.md) → [sfod-method-families](concepts/sfod-method-families.md) → 各篇論文。

```
wiki/
├── index.md
├── glossary.md
├── log.md
├── sources/      （6 篇論文）
├── concepts/     （27 頁：概念 18、方法 7、資料集與指標 2）
└── comparisons/  （4 頁：比較與發想）
```

- 📄 根目錄
  - [glossary](glossary.md) — 全部術語的中英對照與白話
  - [log](log.md) — 操作紀錄（ingest／lint／synthesize／build…）
- 📁 [sources/](sources/) — 論文（6）
  - [dsod-2026](sources/dsod-2026.md) — 用 DINOv2 特徵注入＋前景規範，減輕 SFOD 的來源偏差；附輕量蒸餾版
  - [falcon-sfod-2026](sources/falcon-sfod-2026.md) — 用 OV-SAM 遮罩把注意力拉回物體＋抗雜訊、顧及少數類別的損失
  - [sfuod-2025](sources/sfuod-2025.md) — 新情境：無來源資料＋偵測未知物體；CollaPAUL 協作調整＋主軸投影標未知
  - [ttaod-f-2025](sources/ttaod-f-2025.md) — （TTA）第一個用圖文偵測器做邊用邊學：提示調整＋記憶庫
  - [vlod-tta-2026](sources/vlod-tta-2026.md) — （TTA）免老師的 IoU 加權熵＋提示挑選，同準確度、記憶體約 1/3
  - [cga-2026](sources/cga-2026.md) — （分類，延伸）CLIP＋混淆提示詞處理不對稱類別混淆
- 📁 [concepts/](concepts/) — 概念、方法、資料集（27）
  - 🧩 概念與問題（18）
    - [object-detection](concepts/object-detection.md) — 找出「有什麼、在哪裡」
    - [domain-shift](concepts/domain-shift.md) — 訓練環境≠使用環境，效能下滑
    - [source-free-adaptation](concepts/source-free-adaptation.md) — 沒有來源資料下的自適應（SFOD/SFDA）定義與比較
    - [source-bias](concepts/source-bias.md) — 調整後仍偏向來源領域的核心問題
    - [pseudo-label](concepts/pseudo-label.md) — 模型自己出的參考答案
    - [sfod-method-families](concepts/sfod-method-families.md) — SFOD 方法家族總覽
    - [vision-foundation-model](concepts/vision-foundation-model.md) — 見多識廣的通才模型（DINOv2 等）
    - [attention-map](concepts/attention-map.md) — 模型在看哪裡
    - [segmentation-model](concepts/segmentation-model.md) — 描輪廓的模型（OV-SAM）
    - [class-imbalance](concepts/class-imbalance.md) — 類別多寡不均、長尾
    - [class-confusion](concepts/class-confusion.md) — 類別容易認錯且有方向性
    - [extreme-domain-shift](concepts/extreme-domain-shift.md) — 照片↔插畫、可見光↔紅外線
    - [open-set-detection](concepts/open-set-detection.md) — 已知／未知物體，封閉 vs 開放集合
    - [image-classification](concepts/image-classification.md) — 分類 vs 偵測
    - [test-time-adaptation](concepts/test-time-adaptation.md) — 邊用邊學（TTA）與 SFOD 的差別
    - [vision-language-model](concepts/vision-language-model.md) — 圖文模型 CLIP、提示詞
    - [vision-language-detector](concepts/vision-language-detector.md) — 看得懂文字的偵測器（Grounding DINO、YOLO-World）
    - [candidate-box-iou](concepts/candidate-box-iou.md) — 候選框與重疊程度
  - 🛠️ 方法（7）
    - [mean-teacher](concepts/mean-teacher.md) — 師生自我訓練框架（EMA 老師）
    - [detr](concepts/detr.md) — Transformer 偵測器（Deformable-DETR）
    - [knowledge-distillation](concepts/knowledge-distillation.md) — 大模型教小模型
    - [collaborative-tuning-paul](concepts/collaborative-tuning-paul.md) — SFUOD 的協作調整與未知標註
    - [prompt-tuning](concepts/prompt-tuning.md) — 只調便條紙的參數高效微調
    - [adapter](concepts/adapter.md) — 插入小轉接頭的參數高效微調
    - [entropy-minimization](concepts/entropy-minimization.md) — 讓模型更果斷的調整目標
  - 📊 資料集與指標（2）
    - [benchmarks](concepts/benchmarks.md) — Cityscapes / Foggy / BDD100k / Sim10k / KITTI、mAP
    - [recall-and-h-score](concepts/recall-and-h-score.md) — 開放集合指標
- 📁 [comparisons/](comparisons/) — 比較與發想（4）
  - [method-comparison](comparisons/method-comparison.md) — 各論文方法並列
  - [results-comparison](comparisons/results-comparison.md) — 各論文結果與進步幅度
  - [ideas](comparisons/ideas.md) — （SYNTHESIZE）延伸發想總表：作者未來方向、交叉發想、共同盲點、建議加讀論文
  - [cga-ideas-for-detection](comparisons/cga-ideas-for-detection.md) — （發想）把 CGA 的混淆提示帶回偵測
