import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

f = lambda x, y : x**2 + 0.1*y

# hx: Schrittweise x; hy: Schrittweise y;
def Gruppe9_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    nx = np.abs(xmax-xmin)/hx
    ny = np.abs(ymax-ymin)/hy
    x = np.linspace(xmin, xmax, 15)
    y = np.linspace(ymin, ymax, 10)

    x,y = np.meshgrid(x,y)
    vx = np.ones_like(x)
    vy = f(x,y)

    # ev. normieren
    v = np.sqrt(vx**2+vy**2)
    vx = vx / v
    vy = vy / v

    sol = integrate.solve_ivp(f, [xmin, xmax], [0], method='RK45',  max_step=0.1)

    plt.quiver(x,y,vx,vy,color='b',width=0.003,angles='xy')
    plt.plot(sol.t, sol.y[0,:], '-r')
    plt.show()

if __name__ == '__main__':
    Gruppe9_S11_Aufg1(f, -2, 2, -1, 6, 4/15, 3/10)