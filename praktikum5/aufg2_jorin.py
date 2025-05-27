import numpy as np
import matplotlib.pyplot as plt


def Name_S5_Aufg2(x, y, xx):

    n = len(x) - 1
    h = np.diff(x)

    a = y.copy()

    A = np.zeros((n + 1, n + 1))
    print(A)
    b = np.zeros(n + 1)
    A[0, 0] = 1
    A[n, n] = 1

    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    c = np.linalg.solve(A, b)

    b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3
    d = (c[1:] - c[:-1]) / (3 * h)

    print(b)
    print(d)
    yy = np.zeros_like(xx)

    for k in range(len(xx)):
        idx = np.searchsorted(x, xx[k]) - 1
        if idx < 0:
            idx = 0
        elif idx >= n:
            idx = n - 1
        dx = xx[k] - x[idx]
        yy[k] = a[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'ro', label='Stützstellen')  # Gegebene Stützpunkte
    plt.plot(xx, yy, 'b-', label='Kubischer Spline')  # Interpolierte Werte
    plt.xlabel('x')
    plt.ylabel('S(x)')
    plt.title('Natürlicher kubischer Spline')
    plt.legend()
    plt.grid()
    plt.show()

    return yy

x_test = np.array([4, 6, 8, 10])
y_test = np.array([6, 3, 9, 0])
xx_test = np.linspace(4, 10, 100)

yy_test = Name_S5_Aufg2(x_test, y_test, xx_test)
