abel_pattern_attractor.py formally known as Gray-Scott Reaction-Diffusion Simulation — Results
This documentation establishes the baseline metrics and identifies 
the sharp thresholds required for pattern formation.

## Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| N | 100 | Grid size (100×100) |
| Du | 0.16 | Diffusion rate of U (substrate) |
| Dv | 0.08 | Diffusion rate of V (product) |
| f | 0.012 | Feed rate (base) |
| k | 0.050 | Kill rate |
| dt | 1.0 | Timestep |
| Steps | 4000 | Total iterations |
| Log interval | 100 | Steps between log entries |

## Equations
dU/dt = Du * ∇²U - U·V² + f·(1 - U)
dV/dt = Dv * ∇²V + U·V² - (f + k)·V

Laplacian computed via periodic boundary conditions using `np.roll`.

## Baseline Results (k = 0.050, η = 0)

| Metric | Value |
|--------|-------|
| U mean range | 0.661 – 0.971 |
| V mean range | 0.014 – 0.068 |
| Coverage range (V > 0.1) | 5.8% – 26.7% |
| Peak reaction rate (UV²) | 0.004267 at step 1800 |
| Peak coverage | 26.7% at step 2800 |
| Late‑stage mean coverage | 22.4% (steps 2000–4000) |
| Late‑stage coverage std | 0.0224 |
| Late‑stage oscillation period | ~300‑500 steps |

## Observed Dynamics (baseline)

Three distinct phases:

1. **Nucleation (steps 0–800):** V grows from seeded region, U is locally consumed. Coverage rises from 5.8% to 21.3%.
2. **Expansion and peak (steps 800–1800):** Bubbles spread across grid. UV² and coverage both peak at step 1800 (26.6%).
3. **Transition and late attractor (steps 1800–4000):** Period settles into stable oscillation around 22.4%. Neither collapses nor fills grid.

## k‑sweep Phase Boundary (f = 0.012)

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

**Phase boundaries (f = 0.012, N = 100, steps = 4000):**

- Lower collapse: between k = 0.046 and 0.048
- Upper collapse: between k = 0.052 and 0.054
- Pattern‑forming window: k ∈ [0.048, 0.052]
- Window width: 0.004 (4% relative to k = 0.050)
- Collapse is sharp: no gradual decay at boundaries

## Noise Resilience Test

Feed rate f perturbed at each step: `f_step = f_base + uniform(-η, +η)`

| η | late_mean | late_std | period_mean | period_std | peaks |
|---|-----------|----------|-------------|------------|-------|
| 0.000 | 0.2182 | 0.0307 | 500.0 | 226.8 | 8 |
| 0.001 | 0.2192 | 0.0344 | 485.7 | 135.5 | 8 |
| 0.003 | 0.2221 | 0.0322 | 387.5 | 92.7 | 9 |
| 0.006 | 0.2176 | 0.0289 | 380.0 | 74.8 | 11 |

**Findings:**

- Late‑stage coverage mean stable across all η (0.217–0.222)
- Oscillation period compresses (500 → 380 steps), period variance decreases
- No collapse or unbounded growth observed at any tested η

## Repository Files

- `gray_scott.py` – baseline simulation
- `gray_scott_noise.py` – noise resilience test
- `gray_scott_k_sweep.py` – k‑sweep phase boundary
- `gray_scott_2d_sweep.py` – 2D (f,k) sweep (49 runs)
- `gray_scott_bubbles.csv` – raw baseline data
- `gray_scott_noise_results.csv` – noise test data
- `phase_map_7x7.csv` – 2D sweep raw data
- `gray_scott_bubbles.png` – coverage plot
- `gray_scott_baseline_fields.png` – final U/V fields
- `gray_scott_f014_k040.png` – inverted‑bubble final field
- `stability_f014_k040.png` – 10k‑step stability coverage
- `gray_scott_phase_map.md` – full 2D phase map documentation

---

*Simulation run on Carnets (iPad) | Results verified | May 8, 2026*
