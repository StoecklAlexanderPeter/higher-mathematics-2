import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
y = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422, 308.745])
b = np.array([])
d = np.array([])
offset = -1900
x = x + offset

h = np.diff(x)
a = y.copy()

A = np.zeros((len(x)-2, len(x)-2))
z = np.zeros((len(x)-2))
for i in range(0, len(x)-2):
    A[i, i] = 2 * (h[i] + h[i+1])
    if i+1 < (len(x)-2):
        A[i, i+1] = h[i]
        A[i+1, i] = h[i]
    z[i] = 3 * ((y[i+2]-y[i+1])/h[i+1]) - 3 * ((y[i+1]-y[i])/h[i])

missing_c = np.linalg.solve(A, z)
c = np.concatenate(([0], missing_c, [0]))

for i in range(0, len(y)-1):
    b = np.append(b, ((y[i+1] - y[i])/h[i]) - ((h[i] * (c[i+1] + (2*c[i]))) /3))

for i in range(0, len(c)-1):
    d = np.append(d, (1/(3*h[i])) * (c[i+1] - c[i]))

print(c)
print(b)
print(d)

xx = np.linspace(1900 + offset, 2010 + offset, 100)
yy = np.zeros_like(xx)

n = len(x) - 1
for k in range(len(xx)):
    idx = np.searchsorted(x, xx[k]) - 1
    if idx < 0:
        idx = 0
    elif idx >= n:
        idx = n - 1
    dx = xx[k] - x[idx]
    yy[k] = a[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3

# b
scipy_cs = CubicSpline(x, y)
y_scipy = scipy_cs(xx)

#c
coefficients = np.polyfit(x, y, 11)
print("Polynomial coefficients:", coefficients)
y_polyval = np.polyval(coefficients, xx)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Stützstellen')  # Gegebene Stützpunkte
plt.plot(xx, yy, 'b-', label='Cubic Spline')  # Interpolierte Werte
plt.plot(xx, y_scipy, '-', label='Scipy Cubic Spline')
plt.plot(xx, y_polyval, '-', label='11th-Degree Polynomial Fit')
plt.plot(xx, y_polyval, '-', label='11th-Degree Polynomial Fit')

plt.xlabel('x')
plt.ylabel('S(x)')
plt.title('Natürlicher kubischer Spline')
plt.legend()
plt.grid()
plt.show()
