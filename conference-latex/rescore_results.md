# Phase 1 — 10-scale composite (`weights = Ours` = balance-weighted)

## Per-metric ranks within the 10-subset

### balance
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MF / Agg | 0.6855 |
| 2 | MF / KM | 0.6850 |
| 3 | MICE / KM | 0.6740 |
| 4 | KNN / KM | 0.5425 |
| 5 | KNN / Agg | 0.3610 |
| 6 | MICE / Agg | 0.3562 |
| 7 | None40 / Agg | 0.3553 |
| 8 | None40 / KM | 0.3152 |
| 9 | None20 / KM | 0.2894 |
| 10 | None20 / Agg | 0.2582 |

### silhouette
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MICE / KM | 0.7921 |
| 2 | KNN / KM | 0.7854 |
| 3 | MF / Agg | 0.7564 |
| 4 | MF / KM | 0.7554 |
| 5 | None40 / Agg | 0.1572 |
| 6 | KNN / Agg | -0.0199 |
| 7 | None40 / KM | -0.0719 |
| 8 | MICE / Agg | -0.0779 |
| 9 | None20 / KM | -0.2127 |
| 10 | None20 / Agg | -0.3168 |

### calinski_harabasz
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MICE / KM | 13154.9105 |
| 2 | MF / Agg | 9792.4979 |
| 3 | MF / KM | 9654.3655 |
| 4 | KNN / KM | 8744.7758 |
| 5 | None40 / KM | 1281.8871 |
| 6 | None20 / KM | 28.0411 |
| 7 | MICE / Agg | 2.3449 |
| 8 | None40 / Agg | 2.1610 |
| 9 | None20 / Agg | 1.1092 |
| 10 | KNN / Agg | 0.2786 |

### dunn
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MF / Agg | 0.9810 |
| 2 | MF / KM | 0.0555 |
| 3 | None20 / Agg | 0.0434 |
| 4 | KNN / KM | 0.0325 |
| 5 | MICE / KM | 0.0308 |
| 6 | None40 / Agg | 0.0208 |
| 7 | None20 / KM | 0.0206 |
| 8 | KNN / Agg | 0.0166 |
| 9 | MICE / Agg | 0.0100 |
| 10 | None40 / KM | 0.0085 |

### davies_bouldin
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MICE / KM | 0.7919 |
| 2 | KNN / KM | 0.7861 |
| 3 | MF / Agg | 0.7303 |
| 4 | MF / KM | 0.7298 |
| 5 | None40 / Agg | 0.6137 |
| 6 | None20 / Agg | 0.3039 |
| 7 | MICE / Agg | 0.2818 |
| 8 | None20 / KM | 0.1909 |
| 9 | None40 / KM | 0.1686 |
| 10 | KNN / Agg | 0.0685 |

### xie_beni
| Rank | Pipeline | Value |
|---:|---|---:|
| 1 | MICE / KM | 0.9705 |
| 2 | KNN / KM | 0.9651 |
| 3 | MF / Agg | 0.9605 |
| 4 | MF / KM | 0.9600 |
| 5 | None40 / Agg | 0.6853 |
| 6 | MICE / Agg | 0.2820 |
| 7 | None20 / Agg | 0.1826 |
| 8 | None20 / KM | 0.0793 |
| 9 | None40 / KM | 0.0325 |
| 10 | KNN / Agg | 0.0163 |

## 10-scale composite ranking

| Rank | Pipeline | 10-scale composite |
|---:|---|---:|
| 1 | MF / Agg | 9.1000 |
| 2 | MICE / KM | 8.9000 |
| 3 | MF / KM | 8.1000 |
| 4 | KNN / KM | 7.7000 |
| 5 | None40 / Agg | 4.6000 |
| 6 | MICE / Agg | 3.9500 |
| 7 | KNN / Agg | 3.9500 |
| 8 | None40 / KM | 3.5500 |
| 9 | None20 / KM | 2.9000 |
| 10 | None20 / Agg | 2.2500 |

## Derived statistics

### Mean composite by imputer (K-Means + Agg / 2)
- MissForest: **8.60**  (was 25.30 in 32-scale)
- MICE: **6.43**  (was 18.13)
- KNN: **5.82**  (was 15.70)
- Baselines (four): **3.33**  (was 8.09)

### Pooled means and lift ratios
- All-imputed pooled mean (six cells): **6.95**  (was 19.71)
- Lift, all imputed vs baselines: **2.09x**  (was 2.4x)
- Lift, MissForest vs baselines: **2.59x**  (was 3.1x)

### K-Means-imputed cells
- Mean: **8.23**  (was 23.98)
- Range: **7.70 to 8.90**  (was 22.05 to 26.60)

### Agglomerative-imputed cells and best Agg baseline
- MF/Agg: **9.10**  (was 27.30)
- MICE/Agg: **3.95**  (was 9.65)
- KNN/Agg: **3.95**  (was 9.35)
- Best Agg baseline (None40/Agg): **4.60**  (was 10.35)
- MICE/Agg AND KNN/Agg both fall below best Agg baseline: **YES**  (interaction claim survives)

---

# Phase 2 — Broader weight-sensitivity study (10-scale)

Six weight regimes over (balance, silhouette, CH, Dunn, DB, XB).
Each row sums to 1. Composite is ranked within the 10-subset only.

## Regimes tested

| # | Regime | balance | silhouette | CH | Dunn | DB | XB |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Ours (balance-weighted) | 0.350 | 0.250 | 0.200 | 0.100 | 0.050 | 0.050 |
| 2 | Equal | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 |
| 3 | Silhouette-only | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4 | Balance-only | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5 | No-balance (5-way equal) | 0.000 | 0.200 | 0.200 | 0.200 | 0.200 | 0.200 |
| 6 | Separation-heavy | 0.100 | 0.350 | 0.250 | 0.100 | 0.100 | 0.100 |

## Robustness summary

| Regime | Top pipeline | MF/Agg rank | MICE/KM rank | Strong-4 in top-4? | Strong-4 in top-5? | Degenerate-6 in bottom-6? |
|---|---|---:|---:|:---:|:---:|:---:|
| Ours (balance-weighted) | MF / Agg (9.10) | 1 | 2 | YES | YES | YES |
| Equal | MICE / KM (9.00) | 2 | 1 | YES | YES | YES |
| Silhouette-only | MICE / KM (10.00) | 3 | 1 | YES | YES | YES |
| Balance-only | MF / Agg (10.00) | 1 | 3 | YES | YES | YES |
| No-balance (5-way equal) | MICE / KM (9.20) | 2 | 1 | YES | YES | YES |
| Separation-heavy | MICE / KM (9.40) | 2 | 1 | YES | YES | YES |

## Full rankings per regime (audit)

### Ours (balance-weighted)
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MF / Agg | 9.1000 |
| 2 | MICE / KM | 8.9000 |
| 3 | MF / KM | 8.1000 |
| 4 | KNN / KM | 7.7000 |
| 5 | None40 / Agg | 4.6000 |
| 6 | MICE / Agg | 3.9500 |
| 7 | KNN / Agg | 3.9500 |
| 8 | None40 / KM | 3.5500 |
| 9 | None20 / KM | 2.9000 |
| 10 | None20 / Agg | 2.2500 |

### Equal
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MICE / KM | 9.0000 |
| 2 | MF / Agg | 8.8333 |
| 3 | KNN / KM | 8.0000 |
| 4 | MF / KM | 7.8333 |
| 5 | None40 / Agg | 5.0000 |
| 6 | MICE / Agg | 3.8333 |
| 7 | None20 / Agg | 3.5000 |
| 8 | None20 / KM | 3.1667 |
| 9 | None40 / KM | 3.0000 |
| 10 | KNN / Agg | 2.8333 |

### Silhouette-only
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MICE / KM | 10.0000 |
| 2 | KNN / KM | 9.0000 |
| 3 | MF / Agg | 8.0000 |
| 4 | MF / KM | 7.0000 |
| 5 | None40 / Agg | 6.0000 |
| 6 | KNN / Agg | 5.0000 |
| 7 | None40 / KM | 4.0000 |
| 8 | MICE / Agg | 3.0000 |
| 9 | None20 / KM | 2.0000 |
| 10 | None20 / Agg | 1.0000 |

### Balance-only
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MF / Agg | 10.0000 |
| 2 | MF / KM | 9.0000 |
| 3 | MICE / KM | 8.0000 |
| 4 | KNN / KM | 7.0000 |
| 5 | KNN / Agg | 6.0000 |
| 6 | MICE / Agg | 5.0000 |
| 7 | None40 / Agg | 4.0000 |
| 8 | None40 / KM | 3.0000 |
| 9 | None20 / KM | 2.0000 |
| 10 | None20 / Agg | 1.0000 |

### No-balance (5-way equal)
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MICE / KM | 9.2000 |
| 2 | MF / Agg | 8.6000 |
| 3 | KNN / KM | 8.2000 |
| 4 | MF / KM | 7.6000 |
| 5 | None40 / Agg | 5.2000 |
| 6 | None20 / Agg | 4.0000 |
| 7 | MICE / Agg | 3.6000 |
| 8 | None20 / KM | 3.4000 |
| 9 | None40 / KM | 3.0000 |
| 10 | KNN / Agg | 2.2000 |

### Separation-heavy
| Rank | Pipeline | Composite (10-scale) |
|---:|---|---:|
| 1 | MICE / KM | 9.4000 |
| 2 | MF / Agg | 8.6500 |
| 3 | KNN / KM | 8.1000 |
| 4 | MF / KM | 7.6500 |
| 5 | None40 / Agg | 4.9500 |
| 6 | None40 / KM | 3.7000 |
| 7 | MICE / Agg | 3.6500 |
| 8 | None20 / KM | 3.1500 |
| 9 | KNN / Agg | 3.1000 |
| 10 | None20 / Agg | 2.6500 |

## Load-bearing claim

- The four strong imputed pipelines (MF/Agg, MICE/KM, MF/KM, KNN/KM) occupy the **top 4** in all 6 regimes: **YES**
- The four strong imputed pipelines occupy the **top 5** in all 6 regimes: **YES**
- The six degenerate pipelines occupy the **bottom 6** in all 6 regimes: **YES**

### Top-1 identity across regimes
- **Ours (balance-weighted)**: MF / Agg
- **Equal**: MICE / KM
- **Silhouette-only**: MICE / KM
- **Balance-only**: MF / Agg
- **No-balance (5-way equal)**: MICE / KM
- **Separation-heavy**: MICE / KM

Distinct top-1 pipelines across all 6 regimes: ['MF / Agg', 'MICE / KM']
