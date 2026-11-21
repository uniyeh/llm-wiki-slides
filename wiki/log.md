# Log

## [2026-11-21] init | 專案建立
- 建立 raw/ wiki/{sources,concepts} asset/ slides/ 與 AGENTS.md
- asset/ 下載 Kenney Shape Characters（CC0），組合 10 個幾何角色 char_*.png

## [2026-11-21] ingest | dsod-2026
- 新增 sources/dsod-2026.md
- 新增 concepts/: object-detection, detr, domain-shift, source-free-adaptation, mean-teacher, pseudo-label, source-bias, vision-foundation-model, knowledge-distillation, benchmarks, sfod-method-families
- 標註矛盾：摘要 39.3 vs Table 2 39.2（cross-scene）

## [2026-11-21] init | 更新 AGENTS.md
- 新增頁面類型 comparison、glossary；出處加圖表號；ingest 一次一篇
- 新增 wiki/glossary.md

## [2026-11-21] lint | dsod-2026 數字驗算
- 自算 Table 1/2 各類別平均：DSOD 列與 mAP 欄不符（48.1 vs 46.4；39.2 vs 38.5），其他方法列一致
- 使用者決策：無法確認時以表格 mAP 欄為準；移除「幾乎追上 Oracle」說法

## [2026-11-21] ingest | falcon-sfod-2026
- 新增 sources/falcon-sfod-2026.md；concepts/: attention-map, segmentation-model, class-imbalance, extreme-domain-shift
- 新增 comparisons/: method-comparison, results-comparison
- 更新：vision-foundation-model, sfod-method-families, pseudo-label, mean-teacher, benchmarks, glossary
- 驗算：Table 1/2 各類別平均與 mAP 一致；矛盾：內文贏 SF-YOLO 4.9 vs 表格 4.4；Clipart 35.5 vs 自算 35.35

## [2026-11-21] ingest | sfuod-2025
- 新增 sources/sfuod-2025.md；concepts/: open-set-detection, recall-and-h-score, collaborative-tuning-paul
- 更新：benchmarks, source-free-adaptation, mean-teacher, pseudo-label, sfod-method-families, method-comparison, results-comparison, glossary
- 驗算：Known mAP、H-Score 與表格一致
- 矛盾：Cityscapes 訓練張數 2,975（SFUOD）vs 2,925（DSOD、FALCON）→ 使用者判定 SFUOD 寫錯

## [2026-11-21] ingest | cga-2026
- 新增 sources/cga-2026.md；concepts/: class-confusion, vision-language-model, image-classification
- 更新：vision-foundation-model, source-free-adaptation, pseudo-label, sfod-method-families, method-comparison, results-comparison, glossary
- 驗算：四表 Avg 與自算一致；矛盾：VisDA 最佳類別 8（內文）vs 6（表格）、車輛類 +3.9% 無法重現
- 使用者決策：CGA 為分類論文，簡報只用 1 頁延伸補充

## [2026-11-21] ingest | ttaod-f-2025
- 新增 sources/ttaod-f-2025.md；concepts/: test-time-adaptation, vision-language-detector, prompt-tuning
- 更新：benchmarks, source-free-adaptation, vision-language-model, vision-foundation-model, mean-teacher, pseudo-label, sfod-method-families, method-comparison, results-comparison, glossary
- 驗算：Pascal-C、COCO-C 平均一致；COCO-C 8/15 最佳一致；無矛盾
- 使用者決策：TTA 兩篇放正式內容「另一條路：邊用邊學」，各 1 頁

## [2026-11-21] ingest | vlod-tta-2026
- 新增 sources/vlod-tta-2026.md；concepts/: candidate-box-iou, entropy-minimization, adapter
- 更新：ttaod-f-2025, sfuod-2025（關係段落）, test-time-adaptation, vision-language-detector, benchmarks, prompt-tuning, vision-foundation-model, sfod-method-families, method-comparison, results-comparison, glossary
- 驗算：PASCAL-C 平均、COCO-C 分組加權平均一致；矛盾：TTAOD-F 延遲 693.8 vs 701.9；YW 風格 AP50 +5.8（內文）vs +5.7（表格）

## [2026-11-21] lint | 全 wiki（6 篇 ingest 完成後）
- 斷鏈 0、孤兒頁 0、缺 frontmatter 0、缺白話版 0、glossary 未收 0、index 未收 0
- 修正：results-comparison「同上」改為明確出處；benchmarks Foggy 0.02、recall 10.59、ttaod-f m=10、falcon Source only 補出處；glossary 加入連入與 sfod-method-families
- 接受（非事實缺出處）：日期、資料集名稱含數字、白話段落、表格以表頭／表下方統一標出處的列
- 矛盾已標記：dsod（2 處，使用者決策）、falcon（2）、sfuod（2，使用者決策 1）、cga（2）、vlod-tta（2）；ttaod-f 無
- 頁數：sources 6、concepts 27、comparisons 2、glossary 1

## [2026-11-21] outline | slides/outline.md
- 18 頁；三條路（請通才幫忙／認出沒見過的／邊用邊學）＋CGA 延伸 1 頁

## [2026-11-21] build | slides/index.html
- 單一 HTML、無外部 CDN；角色圖取自 ../asset/

## [2026-11-21] review | slides/review.md
- 第 1 輪：版面置中、3 頁字數超標 → 修正；第 2 輪：#頁碼跳頁 bug、第 12 頁備註精確度 → 修正；第 3 輪通過

## [2026-11-22] build | 吉祥物改為重點提醒
- 使用者決策：吉祥物只用於重點提醒（對話泡泡），約每 3～4 頁一個；保留 2、7，新增 11、14、17；其餘移除；AGENTS.md 第 6 節已更新

## [2026-11-22] lint | 使用者回饋後補 wiki
- 修正 ttaod-f-2025 消融順序（影像＋Warm-start 53.4 → 加文字 53.9 → 加 MH 54.9 → 全部 56.2；ME 單獨 46.1）
- source-bias 新增「和領域落差有什麼不同」對照表
- 新增 comparisons/cga-ideas-for-detection.md（發想頁，標明非論文結論）

## [2026-11-22] outline+build+review | 簡報 v2（23 頁）
- 方法各加「架構與設計討論」頁；第 6、7、21、22 頁改寫；吉祥物 6 隻（2、7、11、14、17、21）且不複述內文；小測驗 4 題

## [2026-11-22] ingest（補段落）| 6 篇 sources
- 依新規則補「設計決策與消融證據」「作者提到的限制與未來方向」兩段
- 新發現：VLOD-TTA 失敗分析（rider↔person 混淆、解析度 640→1024）

## [2026-11-22] synthesize | comparisons/ideas.md
- ① 作者未來方向 6 條、② 交叉發想 6 條（X1 混淆提示 × 騎士被推成行人 最有根據）、③ 共同盲點 4 條、④ 建議加讀論文 8 組

## [2026-11-22] init | AGENTS.md 加入 SYNTHESIZE 節點、使用者回饋→規則（非阻塞）、REVIEW 模擬讀者、sources 新段落規則；新增 tools/lint.py

## [2026-11-22] lint | 相近概念對照段
- 新增「和 X 有什麼不同」：prompt-tuning↔adapter、vision-language-model↔vision-foundation-model↔vision-language-detector、mean-teacher↔knowledge-distillation、class-confusion↔class-imbalance（source-bias↔domain-shift 已有）

## [2026-11-22] outline+build+review | 簡報 v3（24 頁）
- 第 21 頁改用 ideas.md X1、新增第 22 頁（X2、X3、X5）；模擬讀者檢查修 5 處；3 輪通過
