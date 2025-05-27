from cProfile import label

import numpy as np
from matplotlib import pyplot as plt

d=np.array([
    [1971, 2250.],
    [1972, 2500.],
    [1974, 5000.],
    [1978, 29000.],
    [1982, 120000.],
    [1985, 275000.],
    [1989, 1180000.],
    [1993, 3100000.],
    [1997, 7500000.],
    [1999, 24000000.],
    [2000, 42000000.],
    [2002, 220000000.],
    [2003, 410000000.],
])

x = d[:, 0] - 1970
A = np.vstack([x, np.ones_like(x)]).T
y = np.log10(d[:, -1])
print(d[:, -1])
print(A)
print(y)

lam = np.linalg.solve(A.T@A, A.T@y)
print(f"solve={lam}")

y_pred = A @ lam
xx = np.linspace(min(x), (max(x)+12), 100) # bis 2015
exploration_logN_2015 = lam[1] + lam[0] * (2015 - 1970)

def moores_law(x): return 2250 * (2 ** (x/2))

plt.figure()
plt.semilogy(1970 + x, 10**y, 'ko', label='Messdaten', base=10)
plt.semilogy(1970 + x, 10**y_pred, 'r-', label='Fit')
plt.semilogy(1970 + x, moores_law(x), "--", label='Moores law')
plt.semilogy(2015, 10**exploration_logN_2015, "X", label='prediction 2015')
plt.xlabel('Jahr')
plt.ylabel('Anzahl Transistoren')
plt.legend()
plt.show()

# Moores law ist ein wenig optimistischer

