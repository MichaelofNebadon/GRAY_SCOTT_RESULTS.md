# Gray-Scott Reaction-Diffusion Simulation
<img width="579" height="589" alt="image" src="https://github.com/user-attachments/assets/a7e66dd1-db15-460e-8da9-105a0d9647b2" />

<img width="990" height="490" alt="image" src="https://github.com/user-attachments/assets/c7269123-d4c1-4108-a34d-c8f3299fd497" />

# Gray-Scott 2D Phase Map

Parameter sweep across feed rate (f) and kill rate (k).
Fixed: N=64, Du=0.16, Dv=0.08, dt=1.0, steps=3000.

## Regime Map (7x7 grid)

```
        k=0.040 k=0.044 k=0.048 k=0.050 k=0.052 k=0.056 k=0.060
f=0.006  COLL    COLL    COLL    COLL    COLL    COLL    COLL
f=0.008  COLL    COLL    COLL    COLL    COLL    COLL    COLL
f=0.010  COLL    COLL    OSCI    STBL    COLL    COLL    COLL
f=0.012  COLL    COLL    OSCI    STBL    STBL    COLL    COLL
f=0.014  OSCI    COLL    COLL    OSCI    OSCI    COLL    COLL
f=0.016  UNIF    OSCI    COLL    OSCI    STBL    STBL    COLL
f=0.018  UNIF    OSCI    OSCI    OSCI    OSCI    UNIF    COLL
```

Legend:

- COLL: collapsed (zero coverage)
- UNIF: uniform (full coverage, no spatial pattern)
- STBL: stable (pattern persists, low variance)
- OSCI: oscillating (pattern cycles)

## Distribution

|Regime|Count|Fraction|
|------|-----|--------|
|COLL  |30   |61.2%   |
|OSCI  |11   |22.4%   |
|STBL  |5    |10.2%   |
|UNIF  |3    |6.1%    |

## Key Findings

**Minimum feed rate for pattern formation: f >= 0.010**
Below f=0.010, all k values collapse regardless of kill rate.

**The pattern-forming region is a diagonal band**, not a rectangle.
It tilts from (f=0.010, k=0.048) toward (f=0.018, k=0.052).
Higher feed rate tolerates higher kill rate — f and k are coupled.

**Uniform saturation (UNIF) appears at low k / high f.**
At f=0.016-0.018, k=0.040, the feed rate overwhelms the kill rate
and V saturates the grid (~100% coverage). This is a morphologically
distinct regime from the bubble pattern at the baseline.

**Anomalous cell at f=0.014, k=0.040 (OSCI, 86% coverage).**
Low kill rate allows V to spread without adequate decay, producing
a near-filled or labyrinthine pattern rather than discrete bubbles.

**Gap at f=0.014, k=0.048 (COLL).**
The pattern boundary is irregular. This cell collapses while
neighboring cells at higher and lower k sustain patterns.
See boundary resolution section below.

**k=0.060 collapses at all tested f values.**

### Inverted-bubble morphology at (f=0.014, k=0.040)

Visual inspection of the final V field confirms this cell is a
distinct morphological regime, separate from both the baseline
bubble pattern and uniform saturation.

**Observed pattern:** V fills most of the grid with scattered
dark holes (low-V regions) in a high-V background. This is the
inverse of the bubble regime, where discrete V-rich spots sit
in a V-depleted substrate.

**Mechanism:**

- k=0.040 is too low to provide adequate decay of V
- f=0.014 is high enough to sustain reaction but below the
  saturation threshold (UNIF appears at k=0.040 only for f>=0.016)
- Result: V spreads across the grid forming interconnected
  maze-like structures rather than isolated nucleating bubbles

**Coverage behavior:** Rises rapidly to 80-95%, oscillates with
high amplitude, does not settle to a stable mean. The coverage
curve shows no convergence by step 4000.

**Visual evidence:** See gray_scott_f014_k040.png

**Stability test (10000 steps):**

|Metric            |Value          |
|------------------|---------------|
|Late mean coverage|0.8265         |
|Late std coverage |0.1120         |
|Final coverage    |0.9297         |
|Coverage range    |0.0625 - 0.9993|

Coverage oscillates across nearly the full range (6% to 100%)
with no convergence at 10000 steps. This is not a stable
attractor. The regime is chaotic or quasi-periodic — neither
collapsing nor stabilizing over the tested run length.

## Structural Analogy: Thermodynamic Phase Diagrams

The Gray-Scott regime map shares structural features with
thermodynamic phase diagrams (pressure vs temperature):

|Thermodynamic system                           |Gray-Scott system                                    |
|-----------------------------------------------|-----------------------------------------------------|
|Axes: pressure, temperature                    |Axes: k (kill rate), f (feed rate)                   |
|Phases: solid, liquid, gas                     |Regimes: collapsed, stable, oscillating, uniform     |
|Phase boundaries: sharp transitions            |Regime boundaries: sharp onset at collapse thresholds|
|Triple point: all three phases meet            |Irregular boundary region: multiple regimes adjacent |
|Critical point: liquid-gas distinction vanishes|High-coverage anomaly at f=0.014, k=0.040            |

The analogy is structural: both systems exhibit sharp, non-linear
transitions between distinct global states when control parameters
cross critical thresholds. The underlying mathematics (bifurcation
theory) applies to both.

This does not imply the systems are physically equivalent — they
are governed by different equations. The comparison is a
useful framing for understanding why the boundaries are sharp.

## Boundary Resolution: f=0.014

Higher-resolution sweep across k at fixed f=0.014
(step size 0.001, range k=0.044 to k=0.052).

|k     |final_cov|notes        |
|------|---------|-------------|
|0.044 |0.000    |collapsed    |
|0.045 |0.000    |collapsed    |
|0.046 |0.000    |collapsed    |
|0.047 |0.000    |collapsed    |
|0.0475|0.000    |collapsed    |
|0.0480|~0.220   |sharp onset  |
|0.0485|~0.335   |peak coverage|
|0.049 |~0.225   |declining    |
|0.050 |~0.218   |declining    |
|0.051 |~0.197   |declining    |
|0.052 |~0.142   |declining    |

**Lower boundary: between k=0.0475 and k=0.0480**
The transition is sharp — zero coverage to ~22% in a single
0.0005 step.

**Peak at k=0.0485 (~34% coverage)** — the system briefly
enters a high-coverage state immediately inside the boundary
before declining as k increases further.

**No sharp upper collapse observed in this range** — coverage
declines gradually from k=0.048 to k=0.052 at f=0.014.

## Files

- `gray_scott_2d_sweep.py` – sweep script
- `phase_map_7x7.csv` – raw data, all 49 runs
- `gray_scott_phase_map.png` – regime heatmap
- `boundary_resolution_f014.png` – boundary resolution plot
A numerical simulation of the Gray-Scott model implemented in Python/NumPy.

## Parameters

|Parameter|Value|Description                    |
|---------|-----|-------------------------------|
|N        |100  |Grid size (100x100)            |
|Du       |0.16 |Diffusion rate of U (substrate)|
|Dv       |0.08 |Diffusion rate of V (product)  |
|f        |0.012|Feed rate (base)               |
|k        |0.050|Kill rate                      |
|dt       |1.0  |Timestep                       |
|Steps    |4000 |Total iterations               |

## Equations

```
dU/dt = Du * nabla^2 U  -  U*V^2  +  f*(1 - U)
dV/dt = Dv * nabla^2 V  +  U*V^2  -  (f + k)*V
```

Laplacian computed via periodic boundary conditions using np.roll.

## Baseline Results (clean run, eta=0)

|Metric                       |Value                           |
|-----------------------------|--------------------------------|
|U mean range                 |0.661 - 0.971                   |
|V mean range                 |0.014 - 0.068                   |
|Coverage range (V > 0.1)     |5.8% - 26.7%                    |
|Peak reaction rate (UV2)     |0.004267 at step 1800           |
|Peak coverage                |26.7% at step 2800              |
|Late-stage mean coverage     |22.4% (steps 2000-4000)         |
|Late-stage coverage std      |0.0224                          |
|Late-stage oscillation period|~300-500 steps (steps 2800-4000)|

## Observed Dynamics (baseline)

Three distinct phases:

1. **Nucleation (steps 0-800):** V grows from the seeded region,
   U is locally consumed. Early peaks at steps 200, 500, 800
   with coverage rising from 5.8% to 21.3%.
1. **Expansion and peak (steps 800-1800):** Bubbles spread across
   the grid. Reaction rate UV2 and coverage both peak at step 1800
   (UV2 = 0.004267, coverage = 26.6%). The 1000-step gap between
   steps 800 and 1800 reflects the nucleation-to-expansion
   transition, not a regular oscillation.
1. **Transition and late attractor (steps 1800-4000):** Period
   settles into a stable oscillation. Coverage oscillates around
   22.4% and neither collapses to zero nor fills the grid.

## Noise Resilience Test

Feed rate f was perturbed at each step by a uniform random term eta:

```
f_step = f_base + uniform(-eta, +eta)
```

Four noise levels were tested. All runs used identical initial
conditions (same random seed).

|eta  |late_mean|late_std|period_mean|period_std|peaks|
|-----|---------|--------|-----------|----------|-----|
|0.000|0.2182   |0.0307  |500.0      |226.8     |8    |
|0.001|0.2192   |0.0344  |485.7      |135.5     |8    |
|0.003|0.2221   |0.0322  |387.5      |92.7      |9    |
|0.006|0.2176   |0.0289  |380.0      |74.8      |11   |

**Findings:**

- Late-stage coverage mean is stable across all noise levels
  (0.217-0.222), confirming the attractor is robust to feed-rate
  perturbation at these scales.
- Oscillation period compresses modestly as noise increases
  (500 -> 380 steps), with period variance decreasing. Higher
  noise causes more small fluctuations that the peak finder
  detects, increasing peak count.
- No collapse or unbounded growth was observed at any tested
  noise level.

## k-sweep Phase Boundary

Fixed f = 0.012. Swept k from 0.040 to 0.060 (9 points).

|k    |late_mean|late_std|final_cov|regime     |
|-----|---------|--------|---------|-----------|
|0.040|0.0000   |0.0000  |0.0000   |collapsed  |
|0.044|0.0000   |0.0000  |0.0000   |collapsed  |
|0.046|0.0000   |0.0000  |0.0000   |collapsed  |
|0.048|0.2402   |0.0582  |0.2813   |oscillating|
|0.050|0.2182   |0.0307  |0.2071   |stable     |
|0.052|0.1638   |0.0313  |0.1838   |stable     |
|0.054|0.0011   |0.0028  |0.0000   |collapsed  |
|0.056|0.0000   |0.0000  |0.0000   |collapsed  |
|0.060|0.0000   |0.0000  |0.0000   |collapsed  |

**Phase boundaries (f = 0.012, N = 100, steps = 4000):**

- Lower collapse threshold: between k = 0.046 and k = 0.048
- Upper collapse threshold: between k = 0.052 and k = 0.054
- Pattern-forming window: k in [0.048, 0.052]
- Window width: 0.004 (4% relative to baseline k = 0.050)
- Collapse is sharp: no gradual decay observed at boundaries

## 2D Phase Map (f vs k sweep)

Both f and k were varied across a 7x7 grid (49 runs total).
Fixed parameters: N=64, Du=0.16, Dv=0.08, dt=1.0, steps=3000.

```
        k=0.040 k=0.044 k=0.048 k=0.050 k=0.052 k=0.056 k=0.060
f=0.006  COLL    COLL    COLL    COLL    COLL    COLL    COLL
f=0.008  COLL    COLL    COLL    COLL    COLL    COLL    COLL
f=0.010  COLL    COLL    OSCI    STBL    COLL    COLL    COLL
f=0.012  COLL    COLL    OSCI    STBL    STBL    COLL    COLL
f=0.014  OSCI    COLL    COLL    OSCI    OSCI    COLL    COLL
f=0.016  UNIF    OSCI    COLL    OSCI    STBL    STBL    COLL
f=0.018  UNIF    OSCI    OSCI    OSCI    OSCI    UNIF    COLL
```

Legend: COLL=collapsed, UNIF=uniform (full coverage), STBL=stable, OSCI=oscillating

**Distribution across 49 runs:**

- Collapsed (COLL): 30 runs (61.2%)
- Oscillating (OSCI): 11 runs (22.4%)
- Stable (STBL): 5 runs (10.2%)
- Uniform (UNIF): 3 runs (6.1%)

**Key findings:**

- Pattern formation requires f >= 0.010. Below that threshold,
  all k values collapse regardless.
- The pattern-forming region is a diagonal band tilting from
  (f=0.010, k=0.048) toward (f=0.018, k=0.052). Higher f
  tolerates higher k — feed rate and kill rate are coupled.
- At low k / high f (e.g. f=0.016-0.018, k=0.040), V saturates
  the grid (UNIF, ~100% coverage). This is a different morphological
  regime from the bubble pattern at the baseline.
- The anomalous OSCI cell at f=0.014, k=0.040 (86% coverage)
  represents a near-filled or labyrinthine pattern, not discrete
  bubbles. Low kill rate allows V to spread without decaying.
- The f=0.014, k=0.048 collapse is a genuine gap in the pattern
  band — the boundary is irregular, not a simple rectangle.
- k=0.060 collapses at all tested f values.

## Files

- `gray_scott.py` – simulation and analysis script
- `gray_scott_noise.py` – noise resilience test script
- `gray_scott_bubbles.csv` – logged metrics, clean run
- `gray_scott_bubbles.png` – field plots, clean run
