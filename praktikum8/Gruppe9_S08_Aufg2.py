import numpy as np

a = 5
b = 20
v = np.array([a, 8, 11, 14, 17, b])
v_without_b = v[:-1]
v_without_ab = v[1:-1]

print(v)
print(v_without_b)
print(v_without_ab)
n = 5
h = (b-a)/n

def f(x): return 10 * x ** (-3/2)

def dd_f(x): return 10 * (15/4) * x ** (-7/2)
def dddd_f(x): return 10 * (945/16) * x ** (-11/2)

x_vals = np.linspace(a, b, 1000)
max_f_dd = np.max(np.abs(dd_f(x_vals)))
max_f_dddd = np.max(np.abs(dddd_f(x_vals)))

#2a )
x_verschoben = v_without_b + (h/2)
result_2a = 3 * sum(f(x_verschoben))
print(f"2b) {result_2a}")
E_Rf = ((h**2)/24) * (b-a) * max_f_dd
print(f"Fehler Rechteck: {E_Rf}" )

#2b)
result_2b = 3 * (((f(a) + f(b))/2) + sum(f(v_without_ab)))
print(f"2b) {result_2b}")
E_Tf = ((h**2)/12) * (b-a) * max_f_dd
print(f"Fehler Trapez: {E_Tf}" )

#2c)
result_2c = 0.5*f(a) + sum(f(v_without_ab)) + 2*((f(5)+f(8))/2 + (f(8)+f(11))/2 + (f(11)+f(14))/2 + (f(14)+f(17))/2 + (f(17)+f(20))/2) + 0.5*f(b)
print(f"2c) {result_2c}")
E_Sf = ((h**4)/2880) * (b-a) * max_f_dddd
print(f"Fehler Sf: {E_Tf}" )

# exakter Wert des Integrals und Fehler davon in PDF