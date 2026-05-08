# Gray-Scott Reaction-Diffusion Simulation — Results

## Parameters

| Parameter | Value |
|-----------|-------|
| Grid size (N) | 100 × 100 |
| Diffusion rate (Du) | 0.16 |
| Diffusion rate (Dv) | 0.08 |
| Feed rate (f) | 0.012 |
| Kill rate (k) | 0.050 |
| Time step (dt) | 1.0 |
| Total steps | 4000 |
| Log interval | 100 steps |

## Baseline Results (k = 0.050)

| Metric | Value |
|--------|-------|
| U mean range | 0.661 – 0.971 |
| V mean range | 0.014 – 0.068 |
| Coverage range (V > 0.1) | 5.8% – 26.7% |
| Peak reaction rate (UV²) | 0.004267 at step 1800 |
| Peak coverage | 26.7% at step 2800 |
| Late‑stage mean coverage | 22.4% |
| Mean period | 438 steps |

## k‑sweep Phase Boundary

| k | late_mean | late_std | final_cov | regime |
|---|-----------|----------|-----------|--------|
| 0.040 | 0.0000 | 0.0000 | 0.0000 | collapsed |
| 0.044 | 0.0000 | 0.0000 | 0.0000 | collapsed |
| 0.046 | 0.0000 | 0.0000 | 0.0000 | collapsed |
| 0.048 | 0.2402 | 0.0582 | 0.2813 | oscillating |
| 0.050 | 0.2182 | 0.0307 | 0.2071 | stable |
| 0.052 | 0.1638 | 0.0313 | 0.1838 | stable |
| 0.054 | 0.0011 | 0.0028 | 0.0000 | collapsed |
| 0.056 | 0.0000 | 0.0000 | 0.0000 | collapsed |
| 0.060 | 0.0000 | 0.0000 | 0.0000 | collapsed |

**Phase boundaries:**
- Lower collapse: between k = 0.046 and 0.048
- Upper collapse: between k = 0.052 and 0.054
- Stable window: k ∈ [0.048, 0.052]

## Noise Resilience Test

| η | late_mean | late_std | period_mean | peaks |
|---|-----------|----------|-------------|-------|
| 0.000 | 0.2182 | 0.0307 | 500.0 | 8 |
| 0.001 | 0.2192 | 0.0344 | 485.7 | 8 |
| 0.003 | 0.2221 | 0.0322 | 387.5 | 9 |
| 0.006 | 0.2176 | 0.0289 | 380.0 | 11 |

## Repository Files

- `gray_scott.py` – baseline simulation
- `gray_scott_noise.py` – noise resilience test
- `gray_scott_k_sweep.py` – k‑sweep phase boundary
- `gray_scott_bubbles.csv` – raw baseline data

---

*Simulation run on Carnets (iPad) | Results verified | May 8, 2026*
