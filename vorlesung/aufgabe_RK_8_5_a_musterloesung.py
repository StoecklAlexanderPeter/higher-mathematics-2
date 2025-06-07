import numpy as np
import matplotlib.pyplot as plt

def f(t, y): return y
def y_exact(x): return np.exp(x)

def rk_4(f,a,b,n,y0):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)

    x[0] = a
    y[0] = y0
    h = (b - a) / n

    for i in range(0, n):
        x[i + 1] = x[i] + h

        k1 = f(x[i], y[i])
        k2 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k1)
        k3 = f(x[i] + 0.5 * h, y[i] + 0.5 * h * k2)
        k4 = f(x[i] + h, y[i] + h * k3)

        y[i + 1] = y[i] + h * (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x,y

a = 0
b = 1
y0 = 1
n1 = 10
n2 = 20

[x1,y1] = rk_4(f,a,b,n1,y0)
[x2,y2] = rk_4(f,a,b,n2,y0)

x_new = np.linspace(a,b, 100)

plt.plot(x1, y1, x2, y2, x_new, y_exact(x_new))
plt.legend(["RK4 h = 0.1", "RK4 h = 0.05", "Exakte Lösung"])
plt.xlabel("t")
plt.ylabel("y")
plt.grid("major")

# Fehlerberechnung des Absoluten Fehler
fehler_rk1 = np.abs(y1 - y_exact(x1))
fehler_rk2 = np.abs(y2 - y_exact(x2))

plt.figure()
plt.plot(x1, fehler_rk1, x2, fehler_rk2)
plt.legend(["RK4 h = 0.1", "RK4 h = 0.05"])
plt.xlabel("t")
plt.ylabel("y")
plt.grid("major")

plt.show()