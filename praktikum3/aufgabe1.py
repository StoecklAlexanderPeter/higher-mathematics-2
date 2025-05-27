import numpy as np

def f(x):
    x1, x2 = x
    return np.array([
        20 - 18 * x1 - 2 * x2 ** 2,
        -4 * x2 * (x1 - x2 ** 2)
    ])

def jacobian(x):
    x1, x2 = x
    return np.array([
        [-18, -4 * x2],
        [-4 * x2, -4 * x1 + 12 * x2 ** 2]
    ])

def newton_method(x0, iterations=2):
    x = np.array(x0, dtype=float)
    print(f"Iteration 0: x = {x}, ||f(x)||_2 = {np.linalg.norm(f(x)):.6f}")

    for k in range(1, iterations + 1):
        J = jacobian(x)
        delta_x = np.linalg.solve(J, -f(x))
        x_new = x + delta_x

        f_x_k_normiert = np.linalg.norm(f(x_new))
        x_k_minus_x_k_minus_1_normiert = np.linalg.norm(x_new - x)

        print(f"Iteration {k}: x = {x_new}, ||f(x)||_2 = {f_x_k_normiert:.6f}, ||x^(k) - x^(k-1)||_2 = {x_k_minus_x_k_minus_1_normiert:.6f}")
        x = x_new

# Initial vector
x0 = [1.1, 0.9]
newton_method(x0)