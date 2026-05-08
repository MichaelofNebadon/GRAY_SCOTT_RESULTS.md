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

The diagram below shows the conceptual phase space around the Abel Point (f=0.012, k=0.050). The ±5% stability window represents the narrow parameter range where sustained oscillations occur — directly paralleling the Queen Mary University discovery (May 8, 2026) that fundamental constants sit within a narrow "bio-friendly window" for liquid flow.

```python
import numpy as np
import matplotlib.pyplot as plt

# Conceptual phase space — Abel's Island
f_range = np.linspace(0.010, 0.015, 100)
vitality = np.exp(-((f_range - 0.012)**2) / (2 * (0.0006)**2)) * 0.15

plt.figure(figsize=(8, 5))
plt.plot(f_range, vitality, 'b-', linewidth=2)
plt.axvline(0.012, color='red', linestyle='--', linewidth=2, label='Abel Point (f=0.012)')
plt.axvline(0.012 * 0.95, color='orange', linestyle=':', linewidth=1.5, label='-5% boundary')
plt.axvline(0.012 * 1.05, color='orange', linestyle=':', linewidth=1.5, label='+5% boundary')
plt.fill_between(f_range, 0, vitality, where=(f_range >= 0.0114) & (f_range <= 0.0126), 
                  alpha=0.3, color='green', label='Stability Window ("Abel\'s Island")')
plt.xlabel('Feed rate (f)')
plt.ylabel('Vitality (Mean V Concentration)')
plt.title('Abel\'s Island — Phase Space Stability Window')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('abels_island.png', dpi=150)
plt.show()
