import sympy as sp
from sympy.plotting import plot3d
import matplotlib.pyplot as plt

x, y = sp.symbols('x y')

f1 = x**2 / 186**2 - y**2 / (300**2 - 186**2) - 1
f2 = (y - 500)**2 / 279**2 - (x - 300)**2 / (500**2 - 279**2) - 1

p1 = plot3d(f1, (x, -2000, 2000), (y, -2000, 2000), show=False)
p2 = plot3d(f2, (x, -2000, 2000), (y, -2000, 2000), show=False)

p1.extend(p2)
p1.show()
plt.show()

# Koordinaten:
# x - 2000, y -1900, z 42
# x 480, y 1000, z - 73
# x 1700, y 2000, z 12
# x -2000, y 1975, z - 4