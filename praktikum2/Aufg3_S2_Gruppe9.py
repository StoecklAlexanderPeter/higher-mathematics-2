import sympy as sp

sp.init_printing()
x1, x2, x3 = sp.symbols("x1 x2 x3")

f1 = x1 + x2**2 - x3**2 - 13
f2 = sp.ln(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 - 3)**2 - x3**3 + 7


f = sp.Matrix([f1,f2,f3])
print(f)

X = sp.Matrix([x1,x2,x3])
Df = f.jacobian(X)
print(Df)

x0 = [(x1,1.5),(x2,3),(x3,2.5)]
x0Matrix = sp.Matrix([1.5, 3, 2.5])
Df0 = Df.subs(x0)
print(Df0)

fx0 = f.subs(x0)
print(fx0)

x_minus_x0 = X - x0Matrix
print(x_minus_x0)
# x-x0

result = fx0 + Df0 @ x_minus_x0
print("result: ")
print(result)
# Matrix([[x1 + 6*x2 - 5.0*x3 - 15.75], [x2/3 + 0.642012708343871*x3 - 2.32100635417194 + log(3/4)], [38.25 - 18.75*x3]])
