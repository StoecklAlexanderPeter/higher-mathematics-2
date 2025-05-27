import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate

def euler(f, a, b, n, y0):
    h = (b-a)/n
    x = np.zeros(n+1)
    y = np.zeros(n+1)

    x[0] = a
    y[0] = y0

    for i in range(0, n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x[i], y[i])

    return y


def mittelpunkt(f, a, b, n, y0):
    h = (b-a)/n
    x = np.zeros(n+1)
    y = np.zeros(n+1)

    x[0] = a
    y[0] = y0

    for i in range(0, n):
        x_h = x[i] + (h/2)
        y_h = y[i] + (h/2) * f(x[i], y[i])
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x_h, y_h)

    return y


# modifiziertes Euler Verfahren
def mod_euler(f, a, b, n, y0):
    h = (b-a)/n
    x = np.zeros(n+1)
    y = np.zeros(n+1)

    x[0] = a
    y[0] = y0

    for i in range(0, n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x[i], y[i])
        k1 = f(x[i], y[i])
        k2 = f(x[i+1], y[i+1])
        y[i+1] = y[i] + h * (k1+k2)/2

    return y

def Gruppe9_S11_Aufg3(f, a, b, n, y0):
    x = np.linspace(a, b, n+1)
    y_euler = euler(f, a, b, n, y0)
    y_mittelpunkt = mittelpunkt(f, a, b, n, y0)
    y_modeuler = mod_euler(f, a, b, n, y0)

    return [x, y_euler, y_mittelpunkt, y_modeuler]

def f(x, y): return x**2/y

x, y_euler, y_mittelpunkt, y_modeuler = Gruppe9_S11_Aufg3(f, 0, 1.4, 2, 2)
print(x)
print(y_euler)
print(y_mittelpunkt)
print(y_modeuler)

# stimmt überein mit Lösung aus Aufgabe 2

def Gruppe9_S11_Aufg1(f, x, y_euler, y_mittelpunkt, y_modeuler, y0):
    # Richtungsfeld erzeugen
    x_vals = np.linspace(0, 1.5, 20)
    y_vals = np.linspace(1, 4, 20)
    X, Y = np.meshgrid(x_vals, y_vals)
    U = 1
    V = f(X, Y)
    N = np.sqrt(U**2 + V**2)
    U, V = U/N, V/N  # Normieren der Pfeile für gleichmäßige Länge

    plt.figure(figsize=(10, 6))
    plt.quiver(X, Y, U, V, angles='xy', scale=25, color='gray', alpha=0.6)

    # Exakte Lösung mit solve_ivp
    sol = integrate.solve_ivp(f, [0, 1.5], [y0], method='RK45', max_step=0.01)

    # Numerische Lösungen
    plt.plot(x, y_euler, 'bo--', label='Euler-Verfahren')
    plt.plot(x, y_mittelpunkt, 'go--', label='Mittelpunktverfahren')
    plt.plot(x, y_modeuler, 'mo--', label='modifiziertes Euler-Verfahren')

    # Exakte Lösung
    plt.plot(sol.t, sol.y[0], 'r', label='Exakte Lösung (solve_ivp)')

    # Achsenbeschriftung und Legende
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Richtungsfeld und Lösungen der DGL y\' = x²/y')
    plt.grid(True)
    plt.legend()
    plt.xlim([0, 1.5])
    plt.ylim([1, 4])
    plt.show()

Gruppe9_S11_Aufg1(f, x, y_euler, y_mittelpunkt, y_modeuler, 2)