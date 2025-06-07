import numpy as np
import matplotlib.pyplot as plt

def f(t, y_t):
    return t**2 + 0.1 * y_t

a = -1.5
b = 1.5
y0 = 0
n = 5
h = (b - a) / n

t = np.zeros(n+1)
y = np.zeros(n+1)

t[0] = a
y[0] = y0

# Runge Kutta Verfahren
for i in range(0, n):
    t[i+1] = t[i] + h

    k1 = f(t[i], y[i])
    k2 = f(t[i] + 0.5*h, y[i] + 0.5*h*k1)
    k3 = f(t[i] + 0.5*h, y[i] + 0.5*h*k2)
    k4 = f(t[i] + h, y[i] + h*k3)

    y[i+1] = y[i] + h * (1/6) * (k1 + 2*k2 + 2*k3 + k4)

print(t)
print(y)
def analytisches_y(t):
    return -10*t**2 - 200 * t - 2000 + 1722.5 * np.exp(0.05 *(2*t + 3))
t_new = np.linspace(a,b, 100)

plt.plot(t,y,t_new, analytisches_y(t_new))
plt.legend(["Modifiziertes Euler", "Exakte Lösung"])
plt.xlabel("t")
plt.ylabel("y")
plt.grid("major")
plt.show()