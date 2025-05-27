import numpy as np

def f(x):
    x1, x2, x3 = x
    return np.array([
        x1 + x2**2 - x3**2 - 13,
        np.log(x2/4) + np.e **(0.5 * x3 -1) - 1,
        (x2 - 3)**2 - (x3**3) + 7
    ])

def jacobian(x):
    x1, x2, x3 = x
    return np.array([
        [1, 2*x2, -2*x3],
        [0, 1/x2, (0.5 * np.e)**(0.5 *x3-1)],
        [0, 2*x2 - 6, -3*x2**2]
    ])

def newton_method(x0, tol=1e-5, iterations=100):
    x_vector = np.array(x0, dtype=float)
    for i in range(iterations):
        J = jacobian(x_vector)
        delta_x = np.linalg.solve(J, -f(x_vector))
        x_new_vector = x_vector + delta_x

        f_x_k_normiert = np.linalg.norm(f(x_new_vector))

        x_vector = x_new_vector

        if f_x_k_normiert <= tol:
            return i, x_new_vector

# Initial vector
x0 = [1.5, 3, 2.5]
anzahl_iter, x_final = newton_method(x0)
print(f"anzahl iterationen: {anzahl_iter}, x = {x_final}")
