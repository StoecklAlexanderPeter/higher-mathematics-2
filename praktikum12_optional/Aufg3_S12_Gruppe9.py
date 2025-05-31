import numpy as np

from matplotlib import pyplot as plt

def runge_kutta(f, a, b, n, y0):
    h = (b-a)/n
    last_y = y0
    x = np.array([])
    y = np.array([y0])

    for i in range(n):
        t = a + i * h
        k_1 = f(t, last_y)
        k_2 = f(t + (h/2), last_y+(h/2)*k_1)
        k_3 = f(t + (h/2), last_y+(h/2)*k_2)
        k_4 = f(t + h, last_y+h*k_3)
        y_new = last_y + h * (1/6) * (k_1 + 2*k_2 + 2*k_3 + k_4)

        last_y = y_new
        x = np.append(x, t)
        y = np.append(y, y_new)

    x = np.append(x, b)
    return x, y


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

def Gruppe9_S12_Aufg3(f, a, b, n, y0):
    x, y_runge = runge_kutta(f, a, b, n, y0)
    y_euler = euler(f, a, b, n, y0)
    y_mittelpunkt = mittelpunkt(f, a, b, n, y0)
    y_modeuler = mod_euler(f, a, b, n, y0)

    return x, y_runge, y_euler, y_mittelpunkt, y_modeuler

if __name__ == '__main__':
    def f(x, y): return (x ** 2) / y
    # def f_exakt(x): return np.sqrt(((2*(x**3))/2) + 4)
    def f_exakt(x): return np.sqrt(((2/3) * (x ** 3)) + (11.998/3))

    y0 = 2
    a = 0.1
    b = 10
    n = (int) ((b-a)/0.1) - 1 # n = (b-a)/0.1  # h sollte 0.1 sein

    print(n)

    x, y_runge, y_euler, y_mittelpunkt, y_modeuler = Gruppe9_S12_Aufg3(f, a, b, n, y0)

    y_exakt = f_exakt(x)

    ### Fehlerberechnung
    fehler_runge = np.abs(y_exakt - y_runge)
    fehler_euler = np.abs(y_exakt - y_euler)
    fehler_mittelpunkt = np.abs(y_exakt - y_mittelpunkt)
    fehler_modeuler = np.abs(y_exakt - y_modeuler)

    plt.figure()
    plt.plot(x, y_runge, label="Runge Kutta Verfahren")
    plt.plot(x, y_euler, label="Euler Verfahren")
    plt.plot(x, y_mittelpunkt, label="Mittelpunkt Verfahren")
    plt.plot(x, y_modeuler, label="Modifiziertes Euler Verfahren")
    plt.plot(x, y_exakt, label="analytische Lösung")
    plt.legend()


    plt.figure(figsize=(12, 7))


    plt.plot(x, fehler_runge, label="Globaler Fehler Runge-Kutta")
    plt.plot(x, fehler_euler, label="Globaler Fehler Euler")
    plt.plot(x, fehler_mittelpunkt, label="Globaler Fehler Mittelpunkt")
    plt.plot(x, fehler_modeuler, label="Globaler Fehler Mod. Euler")

    plt.xlabel("$x_i$") # x-Achse beschriftet als x_i
    plt.ylabel("Globaler Fehler (logarithmisch)")
    plt.yscale('log') # Setzt die y-Achse auf eine logarithmische Skala
    plt.legend()
    plt.grid(True)
    plt.show()
