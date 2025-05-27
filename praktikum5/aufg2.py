
"""
Implementieren den Algorithmus zur Berechnung der natürlichen kubischen Splinefunktion S(x) gemäss Skript
in der Funktion [yy] = Name_S5_Aufg2(x,y,xx).
x der Vektor mit den (n + 1) gegebenen Stützstellen (aufsteigend sortiert) und
y der analoge Vektor mit den bekannten Stützwerten.

Der Vektor xx defniert die Werte, für die yy = S(xx) berechnet werden soll.
Dabei müssen die Werte von xx innerhalb des Intervals [x0, xn] liegen.

Ihre Funktion soll zusätzlich S(x) für die durch xx defnierten Werte grafsch darstellen.
Überprüfen Sie Ihre Funktion anhand Aufgabe 1.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([4,6,8,10])
y = np.array([6,3,9,0])
b = np.array([])
d = np.array([])

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

xx = np.linspace(4, 10, 100)
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

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Stützstellen')  # Gegebene Stützpunkte
plt.plot(xx, yy, 'b-', label='Kubischer Spline')  # Interpolierte Werte
plt.xlabel('x')
plt.ylabel('S(x)')
plt.title('Natürlicher kubischer Spline')
plt.legend()
plt.grid()
plt.show()
