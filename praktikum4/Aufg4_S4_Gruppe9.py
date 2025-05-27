import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def aufgabe_3a():
    x_sample = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
    y_sample = np.array([.05, .082, .15, .229, .366, .51, .563, .618, .65, .767]) * 100

    coefficients = np.polyfit(x_sample, y_sample, len(x_sample)-1)
    print("Polynomial coefficients:", coefficients)

    x = np.arange(1975, 2020.1, 0.1)
    y_polyval = np.polyval(coefficients, x)

    plt.figure()
    plt.plot(x_sample, y_sample, 'ro', label='Samples')  # Gegebene Stützpunkte
    plt.plot(x, y_polyval, '-', label='a) 9th-Degree Polynomial Fit')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-100, 250])
    plt.title('Polyfit & Polyval')
    plt.legend()
    plt.grid()
    plt.show()


def aufgabe_3b():
    x_sample = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
    x_mean = x_sample.mean()
    x_sample = x_sample - x_mean
    y_sample = np.array([.05, .082, .15, .229, .366, .51, .563, .618, .65, .767]) * 100

    coefficients = np.polyfit(x_sample, y_sample, len(x_sample)-1)
    print("Polynomial coefficients:", coefficients)

    x = np.arange(1975-x_mean, 2020.1-x_mean, 0.1)

    y_polyval = np.polyval(coefficients, x)

    plt.figure()
    plt.plot(x_sample, y_sample, 'ro', label='Samples')  # Gegebene Stützpunkte
    plt.plot(x, y_polyval, '-', label='b) 9th-Degree Polynomial Fit')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-100, 250])
    plt.title('Polyfit & Polyval')
    plt.legend()
    plt.grid()
    plt.show()

def larange_int(x, y, x_int):
    x_sym = sp.symbols("x")
    l = [1] * x.rows  # List of 1s, not a matrix

    for i in range(x.rows):
        for j in range(x.rows):
            if i != j:
                l[i] *= (x_sym - x[j, 0]) / (x[i, 0] - x[j, 0])

    # Interpolating polynomial
    p = 0
    for i in range(x.rows):
        p += y[i, 0] * l[i]

    result = p.subs(x_sym, x_int)

    return sp.simplify(p), result

def aufgabe_3d():
    x_sample = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010], dtype=float)
    x_mean = x_sample.mean()
    x_sample = x_sample - x_mean  # center the x values

    x1 = sp.Matrix(x_sample.tolist())  # column vector
    x1 = x1.reshape(len(x1), 1)         # ensure proper shape
    print("MEAN", x_mean)

    y1 = sp.Matrix([.05, .082, .15, .229, .366, .51, .563, .618, .65, .767]) * 100
    y1 = y1.reshape(len(y1), 1)

    poly, value = larange_int(x1, y1, 2020 - x_mean)

    print("Interpolating Polynomial:")
    sp.pprint(poly, use_unicode=True)

    # Evaluate on a grid
    x = np.arange(1975 - x_mean, 2020.1 - x_mean, 0.1)
    f = sp.lambdify(sp.symbols("x"), poly, modules="numpy")
    y_calculated = f(x)

    # Plotting
    plt.figure()
    plt.plot(np.array(x1).flatten(), np.array(y1).flatten(), 'ro', label='Samples')
    plt.plot(x, y_calculated, '-', label='Lagrange')

    plt.xlabel('x (centered)')
    plt.ylabel('y (%)')
    plt.ylim([-10, 110])
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # aufgabe_2()
    #aufgabe_3a()
    #aufgabe_3b()
    # 3c Schätzwert: 70%, macht aber nicht so Sinn da es eigentlich eine steigend ist.
    aufgabe_3d()

if __name__ == '__main__':
    main()
