---
title: 術語表
type: glossary
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
summary: 全部術語的中英對照與白話
order: 10
---
# 術語表

| 術語（English） | 一句白話 | 詳見 |
|---|---|---|
| 物件偵測（Object Detection） | 找出照片裡有什麼、在哪裡，並用框框起來 | [[object-detection]] |
| 來源領域（Source Domain） | 模型原本受訓的環境（例：晴天城市） | [[domain-shift]] |
| 目標領域（Target Domain） | 模型要被拿去用的新環境（例：霧天城市） | [[domain-shift]] |
| 領域落差（Domain Shift） | 訓練環境和使用環境不一樣，表現就下滑 | [[domain-shift]] |
| 非監督式領域自適應（UDA） | 有舊資料、新資料沒答案，讓模型適應新環境 | [[source-free-adaptation]] |
| 無來源物件偵測（SFOD） | 連舊資料都沒有，只靠舊模型＋新照片適應 | [[source-free-adaptation]] |
| 來源偏差（Source Bias） | 模型還是用舊環境的習慣判斷新環境 | [[source-bias]] |
| 偽標籤（Pseudo-label） | 模型自己猜的答案，拿來當練習用的正解 | [[pseudo-label]] |
| Mean Teacher | 老師出參考答案、學生練習，老師慢慢吸收學生進步 | [[mean-teacher]] |
| EMA（指數移動平均） | 用「大部分舊的＋一點點新的」慢慢更新 | [[mean-teacher]] |
| 視覺基礎模型（VFM） | 看過海量圖片的通才視覺模型，例如 DINOv2 | [[vision-foundation-model]] |
| 知識蒸餾（Knowledge Distillation） | 大模型把本事教給小模型 | [[knowledge-distillation]] |
| DETR / Deformable-DETR | 用 Transformer 一次列出所有物體的偵測器 | [[detr]] |
| mAP | 偵測準確度的平均分數，0–100 越高越好 | [[benchmarks]] |
| Oracle | 拿新環境的標準答案訓練出來的「理論上限」 | [[benchmarks]] |
| 注意力圖（Feature Activation Map） | 模型在照片上「盯著哪裡看」的熱度圖 | [[attention-map]] |
| 分割模型（Segmentation, OV-SAM） | 沿著物體邊緣描出形狀的模型 | [[segmentation-model]] |
| 遮罩（Mask） | 黑白圖：白＝物體、黑＝背景 | [[segmentation-model]] |
| 類別不平衡／長尾（Long-tail） | 有些類別很多、有些很少，模型偏心常見的 | [[class-imbalance]] |
| 極端領域落差 | 照片變插畫、一般相機變紅外線這種大轉變 | [[extreme-domain-shift]] |
| 損失函數（Loss） | 模型的「扣分規則」，訓練就是讓扣分變少 | [[pseudo-label]] |
| 封閉集合／開放集合（Closed-set / Open-set） | 考題答案一定在選項內／可能出現選項外的東西 | [[open-set-detection]] |
| 未知物體（Unknown Object） | 模型沒學過、叫不出名字但該被框出來的東西 | [[open-set-detection]] |
| 召回率（Recall） | 該找到的東西裡找到了幾成 | [[recall-and-h-score]] |
| H-Score | 已知準確度與未知找回率的綜合分，兩者都要好才高 | [[recall-and-h-score]] |
| 協作調整（Collaborative Tuning） | 舊模型＋只看新環境的助手一起判斷 | [[collaborative-tuning-paul]] |
| 物體性（Objectness） | 「像不像一個東西」的分數，不管它是什麼類別 | [[collaborative-tuning-paul]] |
| 圖片分類（Image Classification） | 看整張圖回答「這是什麼」，一張圖一個答案 | [[image-classification]] |
| 類別混淆（Class Confusion） | 長得像的東西容易認錯，而且常是單向的 | [[class-confusion]] |
| 圖文模型（CLIP） | 同時看得懂圖和文字的通才模型 | [[vision-language-model]] |
| 提示詞（Prompt） | 給模型的文字模板，例如「一張___的照片」 | [[vision-language-model]] |
| 零樣本（Zero-shot） | 沒特別訓練過也能直接判斷新類別 | [[vision-language-model]] |
| 測試時調整（TTA） | 上線時一邊用一邊調整，不先離線訓練 | [[test-time-adaptation]] |
| 圖文偵測器（Grounding DINO） | 看得懂文字指令的偵測器，類別可以隨時換 | [[vision-language-detector]] |
| 開放詞彙（Open-vocabulary） | 想找什麼就用文字說，不限固定類別 | [[vision-language-detector]] |
| 提示調整（Prompt Tuning） | 不改大模型，只調前面一小段「便條紙」 | [[prompt-tuning]] |
| 影像損壞（Corruption） | 雜訊、模糊、霧、壓縮失真等讓照片變差的狀況 | [[benchmarks]] |
| 推論延遲（Latency） | 模型處理一張圖要花多久 | [[test-time-adaptation]] |
| 候選框（Proposal） | 偵測器先畫出的大量「可能有東西」的框 | [[candidate-box-iou]] |
| IoU（交併比） | 兩個框重疊多少，0 到 1 | [[candidate-box-iou]] |
| 熵（Entropy） | 模型有多猶豫，越低越有把握 | [[entropy-minimization]] |
| 熵最小化 | 要求模型更果斷，不需正確答案就能調整 | [[entropy-minimization]] |
| 確認偏誤（Confirmation Bias） | 把自己猜錯的也越來越當真 | [[entropy-minimization]] |
| 轉接器（Adapter） | 插在大模型裡的小轉接頭，只調它 | [[adapter]] |
| YOLO-World | CNN 架構、速度快的圖文偵測器 | [[vision-language-detector]] |
| SFOD 方法家族 | 各派解法的分類總覽 | [[sfod-method-families]] |
| 免梯度調整（Gradient-free） | 不做反向傳播就能調整，速度更快 | [[ideas]] |
