import numpy as np
import matplotlib.pyplot as plt

a = 0.
b = 1.
h = 0.1
n = np.int_((b-a)/h)
rows = 4
z0 = np.array([0.,2.,0.,0.])

def euler_vektorieller(f, a, b, h, n, rows, z0):
    x = np.zeros(n+1)
    z = np.zeros([rows,n+1])

    x[0] = a
    z[:,0] = z0

    for i in range(0, n):
        x[i + 1] = x[i] + h
        z[:, i + 1] = z[:, i] + h * f(x[i], z[:, i])

        print(x[i + 1])
        print(z[:, i + 1])

    return x, z

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

def f(x,z): return np.array([z[1], z[2], z[3], np.sin(x)+5-1.1*z[3]+0.1*z[2]+0.3*z[0]])

x, euler_z = euler_vektorieller(f, a, b, h, n, rows, z0)
x_r, runge_z = runge_kutta_vektorieller(f, a, b, h, n, rows, z0)

plt.figure(figsize=(12, 7))
plt.plot(x, euler_z[0, :], x, euler_z[1, :], x, euler_z[2, :], x, euler_z[3, :])
plt.legend(["Euler Lösung y(x)", "y'(x)", "y''(x)", "y'''(x)"])

plt.figure(figsize=(12, 7))
plt.plot(x_r, runge_z[0, :], x_r, runge_z[1, :], x_r, runge_z[2, :], x_r, runge_z[3, :])
plt.legend(["Runge Kutta Lösung y(x)", "y'(x)", "y''(x)", "y'''(x)"])

plt.show()