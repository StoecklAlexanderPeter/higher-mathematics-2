
import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

f = lambda x, y : x**2 + 0.1*y

x = np.linspace(-2,2,15)
y = np.linspace(-1,2,10)
print(x.shape)
x,y = np.meshgrid(x,y)
print(x.shape)
vx = np.ones_like(x)
vy = f(x,y)
# ev. normieren
v = np.sqrt(vx**2+vy**2)
vx = vx / v
vy = vy / v

n = 50
ti = -1.5
tf = 1.5
y0 = [0]
sol = integrate.solve_ivp(f, [ti, tf], y0, method='RK45',  max_step=0.1)

ti = 0
tf = 1.5
y0 = [0.5]
sol2 = integrate.solve_ivp(f, [ti, tf], y0, method='RK45', max_step=0.1)

plt.quiver(x,y,vx,vy,color='b',width=0.003,angles='xy')
plt.plot(sol.t, sol.y[0,:], '-r')
plt.plot(sol2.t, sol2.y[0,:], '-c')
plt.show()
