import numpy as np


def summierte_rechtecksregel(f, a, b, n): # mittelpunktsverfahren
    h = (b-a)/n
    res = 0
    for i in range(0, n):
        xi = a + i * h
        res = res + f(xi + h/2)
    return h * res

def summierte_trapezregel(f, a, b, n):
    h = (b-a)/n
    res = (f(a) + f(b))/2
    for i in range(1, n):
        xi = a + i * h
        res = res + f(xi)
    return h * res

def summierte_simpsonregel(f, a, b, n):
    h = (b-a)/n
    res = (f(a) + f(b))/2
    for i in range(1, n+1):
        xi = a + i * h
        xim= xi - h
        res = res + f(xi) + 2 * f((xim+xi)/2)
    print(xi)
    res = res - f(xi)
    return (h/3)*res

def gauss_formel_for_n_3(f, a, b):
    return ((b-a)/2) * ((5/9) * f(-np.sqrt(0.6) * ((b-a)/2) + ((b+a)/2)) + (8/9) * f((b + a)/2)) + ((b-a)/2) * ((5/9) * f(np.sqrt(0.6) * ((b-a)/2) + ((b+a)/2)))

def f(x): return np.exp(-x**2)

a = 0
b = 0.5
n = 3
rf = summierte_rechtecksregel(f,a,b,n)
tf = summierte_trapezregel(f,a,b,n)
sf = summierte_rechtecksregel(f,a,b,n)
g3f = gauss_formel_for_n_3(f,a,b)

print(f"rf = {rf}")
print(f"tf = {tf}")
print(f"sf = {sf}")
print(f"check", sf - (1/3)*(tf+2*rf))
print(f"g3f = {g3f}")