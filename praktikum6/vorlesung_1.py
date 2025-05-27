import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_triangular
x = np.array([1, 2, 3, 4])
y = np.array([6, 6.8, 10, 10.5])

A = np.array([
    [np.sum(x ** 2), np.sum(x)],
    [np.sum(x), len(x)],
])

b = np.array([
    [np.sum(x * y)],
    [np.sum(y)]
])

print(A)
print(b)

result = np.linalg.solve(A, b)
print(result)

## Option 2
print(x)
A2 = np.array([x, np.ones_like(x)]).T
print(A2)

# Normalengleichung lösen
lam = np.linalg.solve(A2.T@A2, A2.T@y)
print(lam)

Q, R = np.linalg.qr(A2)
lam_qr = solve_triangular(R, Q.T@y)

f = lambda x: lam[0]*x + lam[1]
g = lambda x: lam_qr[0]*x + lam_qr[1]

xx = np.linspace(x.min(), x.max())
plt.plot(x, y, 'o', label='data')
plt.plot(xx, f(xx), 'o', label='model')
plt.plot(xx, g(xx), ':', label='model QR')
plt.legend()
plt.xlabel("x")
plt.show()