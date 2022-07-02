import numpy as np

N = 8192
if __name__ == "__main__":
    A = np.random.randn(N, N)
    B = np.random.randn(N, N)
    C = A @ B
