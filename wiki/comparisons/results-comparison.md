---
title: 結果比較
type: comparison
sources: [dsod-2026, falcon-sfod-2026, sfuod-2025, cga-2026, ttaod-f-2025, vlod-tta-2026]
updated: 2026-11-21
---
# 結果比較

## 白話版
不同論文的「起跑點」不一樣（基礎模型不同），所以不能只看最後分數誰高，要看各自「進步了多少」。

## 晴→霧（Cityscapes → Foggy Cityscapes, mAP@0.5）
| 論文 | Source only（起點） | 方法 | 進步 | 來源 |
|---|---|---|---|---|
| [[dsod-2026]] | 29.5 | 48.1 ⚠️ | +18.6 | DSOD, Table 1, p.8 |
| [[falcon-sfod-2026]] | 25.2 | 46.9 | +21.7 | FALCON, Table 1, p.6 |

⚠️ DSOD 的 48.1 與其各類別平均（46.4，自算自 DSOD, Table 1, p.8）不符，見 [[dsod-2026]]「矛盾」。

## 其他任務
| 任務 | DSOD（起點→結果） | FALCON（起點→結果） |
|---|---|---|
| Cityscapes → BDD100k | 29.1 → 39.2（Table 2, p.9） | 19.1 → 36.9（Table 2, p.7） |
| Sim10k → Cityscapes（car） | 48.9 → 61.4（Table 3, p.9） | 32.0 → 58.8（Table 1, p.6） |
| KITTI → Cityscapes（car） | — | 33.9 → 50.1（Table 1, p.6） |

## 開放集合（SFUOD，指標不同，不與上表比較）
| 任務 | 既有最佳 Known mAP / U-Recall / H | CollaPAUL | 來源 |
|---|---|---|---|
| 晴→霧 | 26.18 / 6.02 / 8.88 | 32.32 / 10.59 / 15.95 | SFUOD, Table 1, p.6 |
| 城市→BDD | 26.68 / 6.86 / 9.89 | 28.21 / 8.57 / 13.15 | SFUOD, Table 2, p.6 |

註：「既有最佳」各指標可能來自不同方法；只計 SFOD 方法，不含 Source only。

## 另一條路：邊用邊學（TTA，基準不同，不與 SFOD 比較）
| 基準 | 直接用 | Mean Teacher | 方法 | 來源 |
|---|---|---|---|---|
| Pascal-C（AP50） | 44.8 | 51.5 | [[ttaod-f-2025]] 56.2 | TTAOD-F, Table 1, p.7 |
| COCO-C（mAP） | 20.6 | 24.1 | [[ttaod-f-2025]] 26.0 | TTAOD-F, Table 2, p.7 |
| ODinW-13（mAP） | 52.8 | 53.1 | [[ttaod-f-2025]] 54.2 | TTAOD-F, Fig. 4, p.8 |
| 推論延遲（ms/張，COCO-C） | 213.1 | 635.0 | [[ttaod-f-2025]] 693.8 | TTAOD-F, Table 9, p.14 |

### TTAOD-F vs VLOD-TTA（同條件，VLOD-TTA 量測，COCO-C，Grounding DINO）
| | 直接用 | TTAOD-F | VLOD-TTA | 來源 |
|---|---|---|---|---|
| mAP | 20.6 | 26.0 | 26.2 | VLOD-TTA, Table 5, p.11 |
| GPU 記憶體（GB） | 1.36 | 11.37 | 3.76 | VLOD-TTA, Table 5, p.11 |
| 延遲（ms/張） | 210.6 | 701.9 | 531.6 | VLOD-TTA, Table 5, p.11 |
| ODinW-13 mAP | 52.8 | 54.2 | 56.0 | VLOD-TTA, Fig. 4, p.12 |

⚠️ TTAOD-F 延遲兩篇量測不同（693.8 ms：TTAOD-F, Table 9, p.14；701.9 ms：VLOD-TTA, Table 5, p.11），引用時標明出處。

## 延伸：分類版 SFDA（準確率 %，不與偵測比較）
| 資料集 | 前最佳 ProDe-V | [[cga-2026]] | 來源 |
|---|---|---|---|
| VisDA | 91.6 | 92.2 | CGA, Table I, p.7 |
| DomainNet-126 | 85.0 | 86.6 | CGA, Table III, p.8 |
| Office-Home | 86.2 | 86.3 | CGA, Table II, p.7 |
| Office-31 | 92.6 | 92.7 | CGA, Table IV, p.8 |

## 共同比較對象 DRU（兩篇都列）
- C→F：DSOD 表中 DRU 43.6（DSOD, Table 1, p.8）；FALCON 表中 DRU 43.7（FALCON, Table 1, p.6）。各類別數字相同，差在四捨五入。
