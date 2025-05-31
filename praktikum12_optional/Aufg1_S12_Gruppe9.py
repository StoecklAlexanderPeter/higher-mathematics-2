import numpy as np

def Gruppe9_S12_Aufg1(f, a, b, n, y0):
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

if __name__ == '__main__':
    def f(x, y): return x ** 2 + 0.1 * y
    x, y = Gruppe9_S12_Aufg1(f, -1.5, 1.5, 5, 0)
    print(x)
    print(y)