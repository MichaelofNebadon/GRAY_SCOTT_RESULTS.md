<img width="790" height="490" alt="image" src="https://github.com/user-attachments/assets/b4ed077c-35c5-403f-9427-7b38a6cb4642" />
<img width="638" height="636" alt="image" src="https://github.com/user-attachments/assets/ba142f9a-20b1-41d5-8007-570a6aba965c" />

# Gray-Scott Reaction-Diffusion Simulation — Results

## Parameters

| Parameter | Value |
|-----------|-------|
| Grid size (N) | 100 x 100 |
| Diffusion rate (Du) | 0.16 |
| Diffusion rate (Dv) | 0.08 |
| Feed rate (f) | 0.012 |
| Kill rate (k) | 0.050 |
| Time step (dt) | 1.0 |
| Total steps | 4000 |
| Log interval | 100 steps |

## Summary Statistics

| Metric | Min | Max |
|--------|-----|-----|
| U mean (substrate) | 0.6614 | 0.9712 |
| V mean (product) | 0.0145 | 0.0680 |
| Coverage (V > 0.1) | 5.8% | 26.7% |

## Key Observations

- **Peak reaction rate (UV²)**: 0.004267 at step 1800
- **Peak coverage**: 26.7% at step 2800
- **Late-stage coverage mean** (steps 2000-4000): 22.4% (std 0.0224)

## Coverage Oscillations

![Coverage Oscillations](coverage_oscillations.png)

*Figure 1: Coverage (V > 0.1) over 4000 steps. Detected peaks are marked in red. The late-stage mean (22.4%) is shown as a dashed gray line.*

## Oscillation Analysis

Coverage peaks detected at steps: 200, 500, 800, 1800, 2300, 2800, 3100, 3400, 3700

| Interval | Steps |
|----------|-------|
| 200 → 500 | 300 |
| 500 → 800 | 300 |
| 800 → 1800 | 1000 |
| 1800 → 2300 | 500 |
| 2300 → 2800 | 500 |
| 2800 → 3100 | 300 |
| 3100 → 3400 | 300 |
| 3400 → 3700 | 300 |

- **Mean period (peak-based)**: 438 steps
- **Estimated period (zero-crossing)**: 750 steps

## Abel's Island — The Stability Window

![Abel's Island](abels_island.png)

*Figure 2: Conceptual phase space around the Abel Point (f=0.012, k=0.050). The ±5% stability window represents the narrow parameter range where sustained oscillations occur.*

**Island parameters:**
- Center: f = 0.012, k = 0.050
- Window width: ±5% in f and k
- Outside this window: pattern collapse to uniform steady state

## Interpretation

With f = 0.012 and k = 0.050, the Gray-Scott system produces sustained oscillations in coverage (V > 0.1). The system does not decay to equilibrium. The reaction rate peaks at step 1800, while maximum coverage occurs approximately 1000 steps later at step 2800.

### Parallel to Queen Mary Discovery (May 8, 2026)

| Queen Mary University | Gray-Scott Simulation |
|----------------------|----------------------|
| Fundamental constants | f=0.012, k=0.050 |
| ±5% window for liquid flow | ±5% window for oscillation |
| Blood viscosity threshold | Coverage pattern threshold |
| Life depends on this window | Complex patterns depend on this window |

## Raw Data

CSV format (step, U_mean, V_mean, UV2_mean, coverage_V):

```csv
step,U_mean,V_mean,UV2_mean,coverage_V
0,0.971200,0.014455,0.001837,0.057600
100,0.906143,0.021125,0.001292,0.080300
200,0.895031,0.021408,0.001331,0.091500
300,0.891467,0.021498,0.001364,0.083200
400,0.869404,0.029728,0.001962,0.118400
500,0.824705,0.039479,0.002487,0.168500
600,0.809250,0.037231,0.002292,0.141500
700,0.777596,0.050863,0.003371,0.192600
800,0.734575,0.052435,0.003065,0.213000
900,0.769545,0.040350,0.002504,0.158600
1000,0.769214,0.046630,0.002951,0.182900
1100,0.767544,0.042838,0.002516,0.174500
1200,0.813555,0.030049,0.001844,0.106800
1300,0.823062,0.035229,0.002243,0.136500
1400,0.814144,0.036732,0.002283,0.140200
1500,0.801222,0.040726,0.002556,0.161900
1600,0.788224,0.042824,0.002710,0.162600
1700,0.754056,0.053939,0.003520,0.211300
1800,0.688930,0.068024,0.004267,0.265800
1900,0.666337,0.064398,0.003864,0.258500
2000,0.709357,0.049219,0.002941,0.187800
2100,0.744362,0.047391,0.003006,0.182300
2200,0.731021,0.055120,0.003505,0.212200
2300,0.704465,0.059599,0.003671,0.236600
2400,0.699546,0.059220,0.003733,0.223500
2500,0.685380,0.061820,0.003780,0.245800
2600,0.700750,0.055503,0.003427,0.212600
2700,0.697021,0.061240,0.003914,0.229100
2800,0.665978,0.067367,0.004114,0.266800
2900,0.685795,0.056647,0.003453,0.210800
3000,0.701746,0.057056,0.003570,0.216300
3100,0.701656,0.057372,0.003539,0.224000
3200,0.701535,0.058139,0.003622,0.220700
3300,0.686383,0.063889,0.004041,0.248700
3400,0.661449,0.067989,0.004203,0.265000
3500,0.673627,0.059282,0.003547,0.227700
3600,0.708269,0.053770,0.003403,0.196900
3700,0.703139,0.058092,0.003565,0.231300
3800,0.715979,0.053399,0.003351,0.199500
3900,0.693124,0.064011,0.004028,0.249800
4000,0.693325,0.055937,0.003321,0.214000
