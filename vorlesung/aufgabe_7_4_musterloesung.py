import numpy as np
import sympy as sp

# NOT TESTED

x = sp.symbols('x')

def summierte_rechtecksregel_fehlerabschaetzung(f, a, b, n):
    h = (b-a)/n
    f_dd = sp.diff(f, x, 2)
    f_dd_vals = np.array([])
    for i in range(0, n+1):
        xi = a + i * h
        f_dd_val = f_dd.subs(x, xi)
        f_dd_vals = np.append(f_dd_vals, f_dd_val)
    return ((h**2)/24) * (b-a) * np.max(f_dd_vals)

def summierte_rechtecksregel(f, a, b, n, tol): # mittelpunktsverfahren
    h = (b-a)/n
    res = 0
    for i in range(1, n):
        xi = a + i * h
        res = res + f.subs(x, xi + h/2)
    return h * res

def summierte_trapezregel_fehlerabschaetzung(f, a, b, n):
    h = (b-a)/n
    f_dd = sp.diff(f, x, 2)
    f_dd_vals = np.array([])
    for i in range(1, n+1):
        xi = a + i * h
        f_dd_val = f_dd.subs(x, xi)
        f_dd_vals = np.append(f_dd_vals, f_dd_val)
    return ((h**2)/12) * (b-a) * np.max(f_dd_vals)

def summierte_trapezregel(f, a, b, n, tol):
    h = (b-a)/n
    res = (f.subs(x, a) + f.subs(x, b))/2
    for i in range(0, n):
        xi = a + i * h
        res = res + f.subs(x, xi)
        print(summierte_trapezregel_fehlerabschaetzung(f,a,b,n))
    return h * res

def summierte_simpsonregel_fehlerabschaetzung(f, a, b, n):
    h = (b-a)/n
    f_dddd = sp.diff(f, x, 4)
    f_dddd_vals = np.array([])
    for i in range(0, n+1):
        xi = a + i * h
        f_dddd_val = f_dddd.subs(x, xi)
        f_dddd_vals = np.append(f_dddd_vals, f_dddd_val)
    return ((h**4)/2880) * (b-a) * np.max(f_dddd_vals)

def summierte_simpsonregel(f, a, b, n, tol):
    h = (b-a)/n
    res = (f.subs(x, a) + f.subs(x, b))/2
    for i in range(0, n+1):
        xi = a + i * h
        xim= xi - h
        res = res + f.subs(x, xi) + 2 * f.subs(x, (xim+xi)/2)
    res = res - f.subs(x, xi)
    return (h/3)*res

f = sp.exp(-x**2)

a = 0
b = 0.5
n = 10
tol = 10e-5
rf = summierte_rechtecksregel(f,a,b,n,tol)
tf = summierte_trapezregel(f,a,b,n,tol)
sf = summierte_rechtecksregel(f,a,b,n,tol)

print(f"rf = {rf}")
print(f"tf = {tf}")
print(f"sf = {sf}")
print(f"check", sf - (1/3)*(tf+2*rf))

"""
rf = 0.6912198912198912
tf = 0.9470238095238095
sf = 0.6912198912198912
check -0.08526797276797271
"""