---
title: VLOD-TTA — Test-Time Adaptation of Vision-Language Object Detectors
type: source
tags: [tta, vision-language-detector, yolo-world, grounding-dino, entropy, efficiency]
sources: [vlod-tta-2026]
raw: raw/VLOD-TTA_Test-Time_Adaptation_Vision-Language_Object_Detectors_ECCV2026.pdf
venue: ECCV 2026（依檔名）
slide-role: 正式內容「另一條路：邊用邊學（TTA）」1 頁（使用者決策 2026-11-21）
updated: 2026-11-22
summary: （TTA）免老師的 IoU 加權熵＋提示挑選，同準確度、記憶體約 1/3
order: 50
---
# VLOD-TTA（ECCV 2026）

## 一句話摘要
比 TTAOD-F 更省的「邊用邊學」：不用老師模型，改用「重視成群重疊框」的熵最小化（IWE），再依每張圖挑選最相關的文字描述（IPS），準確度相當但記憶體只要約 1/3。（VLOD-TTA, p.1–3, Table 5, p.11）

## 要解決的問題
- [[vision-language-detector|圖文偵測器]]零樣本很強，但遇到分布轉移仍會退步；SFDA 要事先收集目標資料、離線調整，不適合部署 → 需要 [[test-time-adaptation|TTA]]。（VLOD-TTA, p.1–2）
- 唯一前作 [[ttaod-f-2025]]：老師模型＋額外前向傳遞＋DINOv2 記憶 → 測試時開銷大；且只適用 Transformer 偵測器，無法用在 CNN 型的 YOLO-World。（VLOD-TTA, p.2, p.4）
- 分類常用的[[entropy-minimization|熵最小化]]用在偵測有兩個問題：會放大確認偏誤（把位置錯的框也變得很有自信）、忽略候選框之間的結構。（VLOD-TTA, p.2–3）
- 分類常用的「多句提示詞平均」用在偵測幾乎沒幫助，甚至變差。（VLOD-TTA, p.3）

## 方法（白話＋技術）
**白話**：偵測器會對同一個東西畫出一大堆重疊的框——一大群框都說「這裡有人」多半是真的；孤零零幾個框說「這裡有狗」多半是看錯。VLOD-TTA 調整時只相信「成群」的意見。另外，每類準備 16 句描述，針對眼前這張圖挑最貼切的幾句來用。

**技術**（VLOD-TTA, p.5–7）：
1. **IWE（IoU-weighted Entropy）**：對每類把預測為該類的[[candidate-box-iou|候選框]]建圖，IoU ≥ θ 就連邊；框的權重 w_i = |所在連通塊大小|^γ（γ=1.1）；以加權平均熵當調整目標，權重不回傳梯度。（Eq. 3, p.6；γ, p.8）
   - YOLO-World 約 8,400 個候選框、Grounding DINO 約 900 個。（p.6）
2. **IPS（Image-conditioned Prompt Selection）**：每類 T=16 句 GPT 生成提示；計算每句與本圖候選框特徵的平均相似度，只保留前 ρ=25%；再加一個可學殘差向量 Δ；最終分數 = λ·提示分數 + (1−λ)·原分數。（Eq. 4, p.6–7；p.8）
3. **只更新少量參數**：YOLO-World 在骨幹與 neck 插 Conv-[[adapter]]；Grounding DINO 只在文字編碼器插 MLP-Adapter。（p.7–8）
4. **每張圖只調一步，預測後重置回初始**（不跨圖累積）；batch size 1。（p.7–8）

## 實驗設定（資料集、指標）
- 風格：Watercolor、ClipArt、Comic；行車：Cityscapes、BDD100K；低光：ExDark；影像損壞：PASCAL-C、COCO-C（15 種損壞 × 5 嚴重度）；另有 ODinW-13。（p.7–8, p.12）→ [[benchmarks]]
- 偵測器：YOLO-World-Small（YW）、Grounding DINO-Tiny（GD）；比較 Zero-shot、TPT、VPT、DPE、Adapter（Tent 目標）。（p.8）

## 主要結果（已驗算：PASCAL-C 平均、COCO-C 分組加權平均皆一致）
**與 TTAOD-F 正面比較**（COCO-C，GD，RTX 3090）（Table 5, p.11）
| | Zero-shot | TTAOD-F | **VLOD-TTA** | VLOD-TTA*（加 Warm-start） |
|---|---|---|---|---|
| 平均 mAP | 20.6 | 26.0 | **26.2** | 27.3 |
| 總參數（百萬） | 172.9 | 629.9 | 173.9 | 173.9 |
| GPU 記憶體（GB） | 1.36 | 11.37 | 3.76 | 3.92 |
| 延遲（ms/張） | 210.6 | 701.9 | 531.6 | 567.3 |

**其他**
| 基準 | 偵測器 | Zero-shot | VLOD-TTA | 來源 |
|---|---|---|---|---|
| ODinW-13（mAP） | GD | 52.8 | **56.0**（TTAOD-F 54.2） | Fig. 4, p.12 |
| PASCAL-C（AP50） | YW | 34.0 | **39.6**（15 種皆最佳） | Table 2, p.10 |
| Watercolor / ClipArt / Comic（mAP） | YW | 26.9 / 24.4 / 17.8 | 29.6 / 28.1 / 21.4 | Table 1, p.9 |
| Watercolor / ClipArt / Comic（mAP） | GD | 37.4 / 38.4 / 31.2 | 38.9 / 41.2 / 34.2 | Table 1, p.9 |
| Cityscapes / BDD100K（mAP） | YW | 18.8 / 13.3 | 19.4 / 14.6 | Table 1, p.9 |
| Cityscapes / BDD100K（mAP） | GD | 24.1 / 16.6 | 25.8 / 18.1 | Table 1, p.9 |
| ExDark 低光（mAP） | YW / GD | 35.2 / 35.4 | 36.4 / 37.3 | Table 1, p.9 |

- ODinW-13 中 12/13 個資料集贏過 TTAOD-F。（Fig. 4, p.12）
- PASCAL-C 最大進步：JPEG +14.1、Pixelate +8.9、Impulse +8.0。（p.10）
- 消融（YW, 風格）：Adapter → IWE → +IPS 每步都進步，如 Watercolor mAP 28.3 → 29.3 → 29.6。（Table 3, p.11）
- 提示平均 vs 挑選：平均讓 Watercolor −0.35、Comic −0.30 AP50；挑選三者平均 +1.0。（Fig. 5a, p.12–13）
- 大模型也有效：YW-Large +3.0～+4.9、GD-Big +2.3～+3.3 AP50。（Table 6, p.12）

## 限制
- 仍比直接用慢：531.6 vs 210.6 ms/張（約 2.5 倍）。（Table 5, p.11）
- 行車場景進步小（YW 平均 +1.0 mAP、GD +1.6）：小物體多、候選框重疊少，IWE 較難發揮。（p.9）
- YW 上 Adapter 基線在 BDD100K 反而低於 Zero-shot（AP50 21.7 vs 22.0）。（Table 1, p.9）
- 與 TTAOD-F 比較時 batch size 不同（4 vs 1）；作者註明 TTAOD-F 改用 1 時效能下降。（p.11 註腳）

## 設計決策與消融證據
| 設計 | 為什麼 | 證據 |
|---|---|---|
| 不用老師、改熵最小化 | 老師需第二個偵測器與額外前向傳遞 | 記憶體 3.76 vs 11.37 GB（Table 5, p.11） |
| IWE 依重疊群加權 | 一般熵把孤立框也拉高信心（確認偏誤） | Adapter 28.3 → IWE 29.3（Watercolor mAP，Table 3, p.11） |
| IPS 挑選而非平均 | 平均會稀釋相關提示 | 平均 −0.35／−0.30；挑選平均 +1.0 AP50（Fig. 5a, p.13） |
| Adapter 而非 BN | BN 需逐資料集調學習率，未知環境不實際 | （Table 4, p.10–11） |
| 單張一步、用完重置 | 單張圖的參數不預期能泛化到其他圖 | （p.7） |

## 作者提到的限制與未來方向
- IWE 在「小物體多、候選框重疊少」的場景（如 Cityscapes）效果較弱。（p.15）
- 仍比 zero-shot 慢（測試時要反向傳播）；**未來方向：免梯度（gradient-free）的 VLOD 測試時調整**。（p.15）
- 失敗分析（補充材料）：
  - **rider 與 person 標籤重疊**：零樣本模型偏向 person，IWE 會把模稜兩可的騎士進一步推向 person；Cityscapes 上 person AP 17.8 → 16.5、rider 6.3 → 1.9。把 rider 併入 person 後，VLOD-TTA 反而進步（person 23.2 → 24.4）。（Table 12–13, p.22–23）
  - **小物體與解析度**：YOLO-World 預設縮到 640×640，遠處小物體不易形成穩定重疊框；改 1024×1024 後 ZS 28.5 → VLOD-TTA 31.2 mAP（640 時僅 18.8 → 19.4）。（Table 14, p.23）
- 在水下等罕見類別領域，CLIP 式提示反而變差，IPS 仍有進步。（p.24）

## 矛盾
- **TTAOD-F 延遲**：TTAOD-F 自己量 693.8 ms（TTAOD-F, Table 9, p.14）；本篇量 701.9 ms（Table 5, p.11）。直接用：213.1 vs 210.6 ms。屬不同量測，簡報標明出處。
- 內文：YW 風格三資料集 AP50 平均 **+5.8**（p.9）；表格自算為 **+5.7**（Table 1, p.9）。依規則用表格。

## 和其他論文的關係
- 直接比較並批評 [[ttaod-f-2025]]：同準確度、更省資源；並借用其 Warm-start 得到 VLOD-TTA*。（p.11）
- 與 SFOD 論文同樣不用來源資料，但屬「邊用邊學」，見 [[test-time-adaptation]]。
- 「多個提示詞」的想法與 [[cga-2026]] 的混淆提示詞相呼應：CGA 加入「看起來像 X 的 Y」；VLOD-TTA 依圖挑選最相關的描述。
