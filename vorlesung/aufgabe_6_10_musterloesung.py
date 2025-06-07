import numpy as np
import sympy as sp

a,b = sp.symbols("a b")
x = np.array([0,1,2,3,4])
y = np.array([3,1,0.5,0.2,0.05])


g = []
for i in range(len(x)):
    f_val_at_xi = a * sp.exp(b * x[i])
    g_i = y[i] - f_val_at_xi
    g.append(g_i)

g = sp.Matrix(g)
lam = sp.Matrix([a, b])
Dg = g.jacobian(lam)

g = sp.lambdify([[[a], [b]]], g, "numpy")
Dg = sp.lambdify([[[a], [b]]], Dg, "numpy")

def gauss_newton_ungedaempft(g, Dg, lam0, tol):
    n = 0
    lam = np.copy(lam0)
    # err = np.linalg.norm(g(lam), 2)
    # while err > tol:
    for i in range(0, 10):
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam))
        lam = lam + delta
        print(f"{n}: {lam}")
        # err = np.linalg.norm(g(lam), 2)
        n = n + 1
    return (lam, n)


def gauss_newton_gedaempft(g, Dg, lam0, tol):
    n = 0
    lam = np.copy(lam0)
    # err = np.linalg.norm(g(lam), 2)
    # while err > tol:
    for i in range(0, 10):
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam))
        min_p = 0
        min_fehler = np.linalg.norm(g(lam), 2)
        for p in range(0,10):
            aktueller_fehler = np.linalg.norm(g(lam + (delta/2**p)), 2)
            if aktueller_fehler < min_fehler:
                min_p = p
                min_fehler = aktueller_fehler

        lam = lam + (delta / 2**min_p)
        print(f"{n}: {lam}")
        # err = np.linalg.norm(g(lam), 2)
        n = n + 1
    return (lam, n)

tol = 1e-5
lam0 = np.array([[1, -1.5]]).T
print("(1,-1.5) ungedämfpt")
[xn, n] = gauss_newton_ungedaempft(g, Dg, lam0, tol)
print(f"x_{n} = {xn}")

print("-----")

# lam0 = np.array([[2, 2]]).T
#[xn, n] = gauss_newton_ungedaempft(g, Dg, lam0, tol)
# print(f"x_{n} = {xn}")
# findet keine Lösung
# print("-----")
print("(1,-1.5) gedämfpt")


lam0 = np.array([[1, -1.5]]).T
[xn, n] = gauss_newton_gedaempft(g, Dg, lam0, tol)
print(f"x_{n} = {xn}")

print("-----")

print("(2,2) gedämfpt")

lam0 = np.array([[2, 2]]).T
[xn, n] = gauss_newton_gedaempft(g, Dg, lam0, tol)
print(f"x_{n} = {xn}")
print("-----")