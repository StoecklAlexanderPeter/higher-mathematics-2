import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

sp.init_printing()

x=np.array([2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5, 8. ,8.5, 9. , 9.5])
y=np.array([159.57209984, 159.8851819 , 159.89378952, 160.30305273,
       160.84630757, 160.94703969, 161.56961845, 162.31468058,
       162.32140561, 162.88880047, 163.53234609, 163.85817086,
       163.55339958, 163.86393263, 163.90535931, 163.44385491])

lam0 = np.array([100, 120, 3, -1],dtype=np.float64)
tol = 1e-5
max_iter = 30
pmax = 5
damping = 1

p = sp.symbols('p0 p1 p2 p3')
print(p)

def f(x,p):
    return (p[0] + p[1] * 10 ** (p[2] + p[3] * x)) / (1 + 10 ** (p[2] + p[3] * x))
print(f)

g = sp.Matrix([y[k]-f(x[k],p) for k in range(len(x))])
print(g)

Dg = g.jacobian(p)
print(Dg)

g = sp.lambdify([p], g, 'numpy')
Dg = sp.lambdify([p], Dg, 'numpy')
print(g(lam0))

def gauss_newton(g, Dg, lam0, tol, max_iter):
    k = 0
    lam = np.copy(lam0)
    err_func = np.linalg.norm(g(lam)) ** 2

    while err_func > tol and k < max_iter:
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()
        lam = lam + delta
        err_func = np.linalg.norm(g(lam)) ** 2
        increment = np.linalg.norm(delta)
        k = k + 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return (lam, k)


def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k = 0
    lam = np.copy(lam0)
    err_func = np.linalg.norm(g(lam)) ** 2
    while err_func > tol and k < max_iter:
        [Q, R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()
        p = 0
        minimal_p = 0
        minimal_err_func = err_func
        while damping and p <= pmax:
            lam_test = lam + delta / (2 ** p)
            err_func_test = np.linalg.norm(g(lam_test)) ** 2
            if err_func_test < minimal_err_func:
                minimal_p = p
                minimal_err_func = err_func_test
            p += 1

        lam = lam + (0.5 ** minimal_p) * delta
        err_func = np.linalg.norm(g(lam)) ** 2
        increment = np.linalg.norm(delta)
        k = k + 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return (lam, k)

# [lam_without,n_without] = gauss_newton(g, Dg, lam0, tol, max_iter)
[lam_with,n_with] = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)
t = sp.symbols('t')
# F_Without = f(t,lam_without)
F_With = f(t,lam_with)
# print(F_Without)
print(F_With)
#F_Without = sp.lambdify([t],F_Without,'numpy')
F_With = sp.lambdify([t],F_With,'numpy')
t = np.linspace(x.min(),x.max())

plt.plot(x,y,'o')
# plt.plot(t,F_Without(t), label="f_without")
plt.plot(t,F_With(t), label="f_with")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# b)
# Nein, das ungedämpfte Verfahren konvergiert hier nicht.
# Dies wurde im auskommentierten Code getestet.
# Das ungedämpfte Verfahren vertraut auf den Newton-Schritt.
# Wenn dieser aber zu gross ist kann es zu Instabilität kommen.
# Der Algorithmus „springt vorbei“, divergiert oder oszilliert.

def err_func(lam_x):
    return np.linalg.norm(g(lam_x))**2

xopt = scipy.optimize.fmin(err_func, lam0)
print(xopt)

# c) Lösungen liegen sehr nah beieinander und sind über die Toleranz erklärbar.