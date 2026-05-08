import numpy as np
import matplotlib.pyplot as plt

N = 100
Du, Dv = 0.16, 0.08
f, k = 0.012, 0.050
dt = 1.0
STEPS = 4000
LOG_INT = 100

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

def run():
    U, V = init_fields()
    log = []
    for s in range(STEPS + 1):
        if s % LOG_INT == 0:
            cov = float((V > 0.1).sum()) / (N * N)
            log.append((s, cov))
        if s < STEPS:
            UV2 = U * V * V
            U += dt * (Du * laplacian(U) - UV2 + f * (1 - U))
            V += dt * (Dv * laplacian(V) + UV2 - (f + k) * V)
            U = np.clip(U, 0, 1)
            V = np.clip(V, 0, 1)
    return np.array(log)

if __name__ == "__main__":
    data = run()
    steps = data[:, 0]
    cov = data[:, 1]
    
    plt.figure(figsize=(10, 5))
    plt.plot(steps, cov, color='seagreen')
    plt.xlabel('step')
    plt.ylabel('coverage (V > 0.1)')
    plt.title('Gray-Scott Baseline — f=0.012, k=0.050')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print(f"Final coverage: {cov[-1]:.4f}")
