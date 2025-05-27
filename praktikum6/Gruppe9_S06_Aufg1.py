import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_triangular
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4])

A = np.vstack([x**2, x, np.ones_like(x)]).T
print(f"A={A}")

lam = np.linalg.solve(A.T@A, A.T@y)
print(f"solve={lam}")

Q, R = np.linalg.qr(A)
lam_qr = solve_triangular(R, Q.T@y)
print(f"QR={lam_qr}")

#b) Vergleichen Sie die Konditionszahl der auftretenden Matrizen AT A bzw. R. Was fällt Ihnen auf?
print(f"Konditionszahl A.T@A = {np.linalg.cond(A.T@A)}; Konditionszahl R = {np.linalg.cond(R)}; ")
# Das die Konditionszahl von R viel kleiner ist als die Konditionszahl von A.T@A

# c)
coefficients = np.polyfit(x, y, 2)
print("Polynomial coefficients:", coefficients)

f = lambda x: lam[0]*x**2 + lam[1]*x + lam[2]
g = lambda x: lam_qr[0]*x**2 + lam_qr[1]*x + lam_qr[2]
polyfit_f = lambda x: coefficients[0]*x**2 + coefficients[1]*x + coefficients[2]

xx = np.linspace(x.min(), x.max())
plt.plot(x, y, 'o', label='data')
plt.plot(xx, f(xx), 'o', label='model')
plt.plot(xx, g(xx), ':', label='model QR')
plt.plot(xx, polyfit_f(xx), 'x', label='Polyfit')
plt.legend()
plt.xlabel("x")
plt.show()

fehler_f = np.sum((y - f(x))**2)
print(f"fehler_f={fehler_f}")
fehler_qr = np.sum((y - g(x))**2)
print(f"fehler_qr={fehler_qr}")
fehler_polyfit = np.sum((y - polyfit_f(x))**2)
print(f"fehler_polyfit={fehler_polyfit}")

# polyfit hat minim weniger fehler


