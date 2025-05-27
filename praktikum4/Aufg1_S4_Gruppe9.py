
# Lagarde Polynomse
def l0(x): return ((x-2500)*(x-5000)*(x-10000))/(-2500*-5000*-10000)
def l1(x): return ((x-0)*(x-5000)*(x-10000))/(2500*-2500*-7500)
def l2(x): return ((x-0)*(x-2500)*(x-10000))/(5000*2500*-5000)
def l3(x): return ((x-0)*(x-2500)*(x-5000))/(10000*7500*5000)

#Polynom
def p(x): return 1013 * l0(x) + 747 * l1(x) + 540 * l2(x) + 226 * l3(x)

result = p(3750)
print(result)