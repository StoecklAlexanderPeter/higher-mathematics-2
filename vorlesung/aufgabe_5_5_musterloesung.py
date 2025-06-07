import numpy as np

def f(x):
    return np.array([
        [float(5.*x[0]**2-x[1]**2)],
        [float(x[1]-0.25*(np.sin(x[0]) + np.cos(x[1])))]
    ])

def Df(x):
    return np.array([
        [float(10.*x[0]), float(-2.*x[1])],
        [float(-0.25*np.cos(x[0])), float(1. +0.25*np.sin(x[1]))]
    ])

def newton(x, eps):
    for i in np.arange(1, 1000):
        delta = np.linalg.solve(Df(x), -f(x))
        x = x + delta
        # berechne Fehler von delta:
        norm_f = np.linalg.norm(-f(x))
        print("Iteration", i)
        print("x = ", x)
        print("2 Norm f = ", norm_f)

        if norm_f <= eps:
            break

eps = 10**-5
x0_1 = np.array([[0.25], [0.25]])
newton(x0_1, eps)