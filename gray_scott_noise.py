import numpy as np
import matplotlib.pyplot as plt

N = 100
Du, Dv = 0.16, 0.08
f_base, k = 0.012, 0.050
dt = 1.0
STEPS = 4000
LOG_INT = 100
NOISE_LEVELS = [0.0, 0.001, 0.003, 0.006]

def laplacian(Z):
    return (np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4 * Z)

def init_fields(seed=42):
    rng = np.random.default_rng(seed)
    U = np.ones((N, N))
    V = np.zeros((N, N))
    r = N // 8
    cx, cy = N // 2, N // 2
    U[cx-r:cx+r, cy-r:cy+r] = 0.50 + rng.uniform(-0.05, 0.05, (2*r, 2*r))
    V[cx-r:cx+r, cy-r:cy+r] = 0.25 + rng.uniform(-0.05, 0.05, (2*r, 2*r))
    return U, V

def run(noise_scale, seed=42):
    rng = np.random.default_rng(seed)
    U, V = init_fields(seed)
    log = []
    for s in range(STEPS + 1):
        if s % LOG_INT == 0:
            cov = float((V > 0.1).sum()) / (N * N)
            log.append((s, cov))
        if s < STEPS:
            f = f_base + rng.uniform(-noise_scale, noise_scale)
            UV2 = U * V * V
            U += dt * (Du * laplacian(U) - UV2 + f * (1 - U))
            V += dt * (Dv * laplacian(V) + UV2 - (f + k) * V)
            U = np.clip(U, 0, 1)
            V = np.clip(V, 0, 1)
    return np.array(log)

def find_peaks(arr, distance=3):
    peaks = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            if not peaks or (i - peaks[-1]) >= distance:
                peaks.append(i)
    return np.array(peaks)

if __name__ == "__main__":
    steps_arr = np.arange(0, STEPS + 1, LOG_INT)
    
    for eta in NOISE_LEVELS:
        data = run(eta)
        cov = data[:, 1]
        late = cov[len(cov)//2:]
        peaks = find_peaks(cov, distance=3)
        period = np.diff(steps_arr[peaks]).mean() if len(peaks) > 1 else float('nan')
        print(f"η={eta}: late_mean={late.mean():.4f}, period={period:.1f}, peaks={len(peaks)}")
