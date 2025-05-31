import numpy as np
import matplotlib.pyplot as plt

a = 0.
b = 10 # 60
h = 0.01 # 0.1
n = np.int_((b-a)/h)
rows = 2
z0 = np.array([(np.pi/2), 0])

def runge_kutta_vektorieller(f, a, b, h, n, rows, z0):
    x = np.zeros(n+1)
    z = np.zeros([rows,n+1])

    x[0] = a
    z[:,0] = z0

    for i in range(0, n):
        x[i + 1] = x[i] + h
        k1 = f(x[i], z[:, i])
        k2 = f(x[i] + (h / 2), z[:, i] + (h / 2) * k1)
        k3 = f(x[i] + (h / 2), z[:, i] + (h / 2) * k2)
        k4 = f(x[i] + h, z[:, i] + h * k3)
        z[:, i + 1] = z[:, i] + h * (1/6) * (k1 + 2*k2 + 2*k3 + k4)

        print(x[i + 1])
        print(z[:, i + 1])

    return x, z

def f(x,z):
    c = 0.16; m = 1; l = 1.2; g = 9.81
    return np.array([z[1], -((c * z[1])/m)] - (g * np.sin(z[0]))/l)

x_r, runge_z = runge_kutta_vektorieller(f, a, b, h, n, rows, z0)

plt.figure(figsize=(12, 7))
plt.plot(x_r, runge_z[0, :], x_r, runge_z[1, :])
plt.legend(["Runge Kutta Lösung phi(t)", "phi'(t)"])

plt.show()