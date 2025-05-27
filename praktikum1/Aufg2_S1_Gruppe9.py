import numpy as np
from matplotlib import pyplot as plt

# w(x,t) einer schwingenden Welle;
# x Ortskoordinate, t Zeit
# O**2 * w / O * t**2 = c**2 * O**2 * w / (O*x**2)
# c = konstante Geschwindigkeit


# a1) w(x,t) = sin(x + ct)
# a2) v(x,t) = sin(x + ct) + cos(2x + 2ct)

c = 1

def w(x, t): return np.sin(x + c*t)
def v(x, t): return np.sin(x + c*t) + np.cos(2*x + 2*c*t)


[x, t] = np.meshgrid(np.linspace(0, 50), np.linspace(0,6 * np.pi))
z = w(x, t)

# Plot Wireframe
wireframe_fig = plt.figure(1)
wirefreame_ax = wireframe_fig.add_subplot(111, projection='3d')
wirefreame_ax.plot_wireframe(x,t,z, rstride=5, cstride=5)
wirefreame_ax.set_xlabel('x')
wirefreame_ax.set_ylabel('y')
wirefreame_ax.set_zlabel('z')

plt.show()



