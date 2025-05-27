import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def f(x,y):
    return x**2 + y**2


[x,y] = np.meshgrid(np.linspace(-5,5), np.linspace(-5,5));
z = f(x,y)

print(np.shape(x))
print(np.shape(y))
print(np.shape(z))
"""
plt.contour(x, y, z)

plt.title('Höhenlinien')
plt.xlabel('x')
plt.ylabel('y')

fig = plt.figure(0)
cont = plt.contour(x, y, z, cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)

plt.title('Höhenlinien')
plt.xlabel('x')
plt.ylabel('y')

fig = plt.figure(1)
cont = plt.contour(x, y, z, [1,4,9,16,25,36,49,64,81,100,121,144,169],cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)

plt.title('Höhenlinien')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
"""
"""
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)

plt.title('Fläche')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title('Fläche')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x,y,z, rstride=5, cstride=5)

plt.title('Gitter')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
"""
fig = plt.figure(6)
ax = fig.add_subplot(111, projection='3d')
surf = ax.contour(x,y,z, cmap=cm.coolwarm)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title('Fläche')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()