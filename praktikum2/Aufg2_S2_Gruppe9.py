import sympy as sp

sp.init_printing()
x1, x2, x3 = sp.symbols("x1 x2 x3")

print("Aufgabe a: ")
fa1 = 5 * x2 * x1
fa2 = x1**2 * x2**2 + x1 + 2 * x2

fa = sp.Matrix([fa1,fa2])
print(fa)

Xa = sp.Matrix([x1,x2])
Dfa = fa.jacobian(Xa)
print(Dfa)

Dfa0 = Dfa.subs([(x1,1),(x2,2)])
print(Dfa0)

# b)
print("Aufgabe b: ")

fb1 = sp.ln(x1**2 + x2**2) + x3**2
fb2 = sp.exp(x2**2 + x3**2) + x1**2
fb3 = (1/(x3**2+x1**2)) + x2**2


fb = sp.Matrix([fb1,fb2,fb3])
print(fb)

Xb = sp.Matrix([x1,x2,x3])
Dfb = fb.jacobian(Xb)
print(Dfb)

Dfb0 = Dfb.subs([(x1,1),(x2,2),(x3,3)])
print(Dfb0)

