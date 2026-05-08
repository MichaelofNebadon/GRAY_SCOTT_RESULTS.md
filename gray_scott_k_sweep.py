import numpy as np

N = 100
Du, Dv = 0.16, 0.08
f = 0.012
dt = 1.0
STEPS = 4000
LOG_INT = 100
K_VALUES = [0.040, 0.044, 0.046, 0.048, 0.050, 0.052, 0.054, 0.056, 0.060]

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

def run(k_val, seed=42):
    U, V = init_fields(seed)
    log = []
    for s in range(STEPS + 1):
        if s % LOG_INT == 0:
            cov = float((V > 0.1).sum()) / (N * N)
            log.append((s, cov))
        if s < STEPS:
            UV2 = U * V * V
            U += dt * (Du * laplacian(U) - UV2 + f * (1 - U))
            V += dt * (Dv * laplacian(V) + UV2 - (f + k_val) * V)
            U = np.clip(U, 0, 1)
            V = np.clip(V, 0, 1)
    return np.array(log)

if __name__ == "__main__":
    print(f"{'k':^8} {'late_mean':^12} {'late_std':^12} {'final_cov':^12}")
    print("-" * 48)
    
    for k_val in K_VALUES:
        data = run(k_val)
        cov = data[:, 1]
        late = cov[len(cov)//2:]
        print(f"{k_val:8.3f} {late.mean():12.4f} {late.std():12.4f} {cov[-1]:12.4f}")
