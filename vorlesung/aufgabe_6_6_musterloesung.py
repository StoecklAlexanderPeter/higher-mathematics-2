import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4])
y = np.array([6,12,30,80,140])

def f1(x): return np.exp(x)

def f2(x):
    x_dum = np.copy(x)
    x_dum[:] = 1 # sets all elements to 1
    return x_dum

def f(x, lam):
    return lam[0]*f1(x) + lam[1]*f2(x) # y = ax + b

A = np.zeros([5,2])
A[:, 0] = f1(x) # erste Kolumne mit 1,2,3,4 füllen
A[:, 1] = f2(x) # zweite Kolumne mit 1 füllen

lam_1 = A.T @ y
print(np.linalg.solve(A.T @ A, A.T @ y))

[Q, R] = np.linalg.qr(A) #A = QR | QR Zerlegung
lam = np.linalg.solve(R, Q.T @ y) # R * lambda = Q^T * y | nach lambda auflösen
# print(lam)
"""
x_fine = np.arange(x[0], x[-1]+0.1, 0.1) # generiere x Punkte von 1 zu 4 in 0.1 Schritten
plt.plot(x,y, "o")
plt.plot(x_fine, f(x_fine, lam))
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["data", "f(x) = a*x+b"])
plt.show()
"""