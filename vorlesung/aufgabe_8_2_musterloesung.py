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

# klassisches Euler Verfahren
for i in range(0, n):
    t[i+1] = t[i] + h
    y[i+1] = y[i] + h * f(t[i], y[i])

def analytisches_y(t):
    return -10*t**2 - 200 * t - 2000 + 1722.5 * np.exp(0.05 *(2*t + 3))
t_new = np.linspace(a,b, 100)

plt.plot(t,y,t_new, analytisches_y(t_new))
plt.legend(["Klassisches Euler", "Exakte Lösung"])
plt.xlabel("t")
plt.ylabel("y")
plt.grid("major")
plt.show()