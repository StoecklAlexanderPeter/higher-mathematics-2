import numpy as np


def f(x):
    x1, x2, x3 = x
    return np.array([
        x1 + x2 ** 2 - x3 ** 3 - 13,
        np.log(x2/4) + np.exp(0.5 * x3 - 1) - 1,
        (x2 - 3) ** 2 - x3**3 + 7
    ])


def df(x):
    x1, x2, x3 = x
    return np.array([
        [1, 2 * x2, -3 * x3 ** 2],
        [0, 1 / x2, 0.5 * np.exp(0.5 * x3)],
        [0, 2 * (x2 - 3), -1]
    ])


def newton(f, df, x0, tol=1e-5, max_iter=20, kmax=4):
    num_iter = 0
    err = 1 + tol
    x = np.array(x0, dtype=float)

    while err > tol:
        fx = f(x)
        Jx = df(x)

        d = np.linalg.solve(Jx, -fx)

        k = 0
        normfx = np.linalg.norm(fx)
        while (k < kmax) and (np.linalg.norm(f(x + d / 2 ** k)) > normfx):
            k += 1

        x = x + d / 2 ** k

        err = np.linalg.norm(f(x))
        num_iter += 1

        if num_iter > max_iter:
            raise Exception("Maximale Anzahl an Iterationen erreicht, Konvergenz nicht sichergestellt.")

    return (x, num_iter)


x0 = [1.5, 3.0, 2.5]

solution, iterations = newton(f, df, x0)
print("Lösung:", solution)
print("Anzahl Iterationen:", iterations)