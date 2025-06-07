import numpy as np
import sympy as sp

a,b = sp.symbols("a b")
x = np.array([1,2,3,4])
y = np.array([7.1, 7.9, 8.3, 8.8])

g = []
for i in range(len(x)):
    f_val_at_xi = a * sp.ln(x[i] + b)
    g_i = y[i] - f_val_at_xi
    g.append(g_i)

g = sp.Matrix(g)
lam = sp.Matrix([a, b])
Dg = g.jacobian(lam)
print(g, Dg)

g = sp.lambdify([[[a], [b]]], g, "numpy")
Dg = sp.lambdify([[[a], [b]]], Dg, "numpy")

def gauss_newton_gedaempft(g, Dg, lam0, tol):
    n = 0
    lam = np.copy(lam0)
    err = np.linalg.norm(g(lam), 2)
    while err > tol:
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam))
        min_p = 0
        min_fehler = np.linalg.norm(g(lam), 2)
        for p in range(0,10):
            aktueller_fehler = np.linalg.norm(g(lam + (delta/2**p)), 2)
            if aktueller_fehler < min_fehler:
                min_p = p
                min_fehler = aktueller_fehler
        err = np.linalg.norm((delta/2**min_p))
        lam = lam + (delta / 2**min_p)
        print(f"{n}: {lam}")
        # err = np.linalg.norm(g(lam), 2)
        n = n + 1
    return (lam, n)

tol = 1e-5
lam0 = np.array([[1, 1]]).T
[xn, n] = gauss_newton_gedaempft(g, Dg, lam0, tol)
print(f"x_{n} = {xn}")
