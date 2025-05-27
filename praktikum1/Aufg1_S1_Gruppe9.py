import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def w(v0, a):
    return (v0**2 * np.sin(2*a))/9.81

[v0, a] = np.meshgrid(np.linspace(0,100), np.linspace(0,90))
z = w(v0, a)

def Aufg1_S1_Gruppe9(x, y, z):
    # Plot Wireframe
    wireframe_fig = plt.figure(1)
    wirefreame_ax = wireframe_fig.add_subplot(111, projection='3d')
    wirefreame_ax.plot_wireframe(x,y,z, rstride=5, cstride=5)
    wirefreame_ax.set_xlabel('x')
    wirefreame_ax.set_ylabel('y')
    wirefreame_ax.set_zlabel('z')

    # Plot Surface
    fig = plt.figure(2)
    surface_ax = fig.add_subplot(111, projection='3d')
    surface_ax.plot_surface(x,y,z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    surface_ax.set_xlabel('x')
    surface_ax.set_ylabel('y')
    surface_ax.set_zlabel('z')

    # plotte in 2 Dimensionen mit Höhenlinien
    plt.figure(3)
    contour = plt.contour(x, y, z, levels=20, cmap=cm.coolwarm)
    plt.clabel(contour, inline=True, fontsize=8)
    plt.title('2D-Höhenlinien')
    plt.xlabel('x')
    plt.ylabel('y')

# Aufgabe A
# Aufg1_S1_Gruppe9(v0, a, z)

# b
## p(V,T)=RT/V
## V(p,T)=RT/p
## T(p,V)=pV/R

v_min, v_max = 0, 0.2
T_min, T_max = 0, 0.2

R = 8.31 # Gaskonstante

def p(V, T):
    return (R * T) / V

[p_V, p_T] = np.meshgrid(np.linspace(1e10,0.2), np.linspace(0,1e4))
p_p = p(p_V, p_T)
Aufg1_S1_Gruppe9(p_V, p_T, p_p)

def V(p, T):
    return (R * T) / p

[V_p, V_T] = np.meshgrid(np.linspace(1e4,1e5), np.linspace(0,1e4))
V_V = V(V_p, V_T)
Aufg1_S1_Gruppe9(V_p, V_T, V_V)

def T(p, V):
    return (p * V) / R

[T_p, T_V] = np.meshgrid(np.linspace(1e4,1e6), np.linspace(0,10))
T_T = V(T_p, T_V)
Aufg1_S1_Gruppe9(T_p, T_V, T_T)

plt.show()
