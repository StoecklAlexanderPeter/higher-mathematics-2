import numpy as np
import matplotlib.pyplot as plt

def lagrange_int(x, y, x_int):
    x = np.array(x)
    y = np.array(y)

    if np.isscalar(x_int):
        x_int = np.array([x_int])
    else:
        x_int = np.array(x_int)

    n = len(x)
    y_int = np.zeros_like(x_int, dtype=float)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_int - x[j]) / (x[i] - x[j])
        y_int += term

    if y_int.size == 1:
        return y_int.item()
    return y_int


def aufgabe_2():
    x_int = 3750
    y_int = lagrange_int([0, 2500, 5000, 10000], [1013, 747, 540, 226], x_int)
    print(f"Calculated value for x+{x_int} is {y_int}")

    # Die resultate unserer lagrange_int funktion stimmen mit dem in Aufgabe 1 berechneten resultat überein

def aufgabe_3_a():
    years = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
    pct = np.array([.05, .082, .15, .229, .366, .51, .563, .618, .65, .767])

    degree = len(years) - 1
    coeffs = np.polyfit(years, pct, degree)

    x_new = np.linspace(1980, 2020, 41)
    y_new = np.polyval(coeffs, x_new)

    plt.figure(figsize=(8, 5))
    plt.plot(years, pct, 'o', label='Original Data')
    plt.plot(x_new, y_new, '-', label='Interpolation Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Households with Computer (%)')
    plt.title('Exact Polynomial Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

    # In der theorie verläuft das polynom zwar durch alle punkte, da aber relativ grosse zahlen verwendet werden kann es zu rundungsfehler kommen.
    # Ausserdem ist das hochgradige polynom nicht geeignet ausserhalb des Wertebereiches.
    # So steigt der Wert ab 2017 auf über 100%

def aufgabe_3_b():

    years = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
    pct = np.array([.05, .082, .15, .229, .366, .51, .563, .618, .65, .767])

    years_centered = years - years.mean()
    degree = len(years) - 1
    coeffs = np.polyfit(years_centered, pct, degree)

    print("Polynomial coefficients (highest power first):")
    print(coeffs)

    x_new = np.linspace(1975-years.mean(), 2020-years.mean(), 41)
    y_new = np.polyval(coeffs, x_new)

    plt.figure(figsize=(8, 5))
    plt.plot(years_centered, pct, 'o', label='Original Data')
    plt.plot(x_new, y_new, '-', label='Interpolation Polynomial')
    plt.xlabel('Year')
    plt.ylabel('Households with Computer (%)')
    plt.title('Exact Polynomial Interpolation (x - x.mean())')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Im vergleich zu Teil a verläuft dieser Plot zwar genauer durch die originalen Datenpunkte, jedoch ist der verlauf ausserhalb des Wertebereiches deutlich schneller unbrauchbar.

def aufgabe_3_d():
    years = np.array([1984, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2016], dtype=float)
    pct = np.array([8.2, 15, 22.8, 36.6, 56.3, 67.8, 77, 83.8, 89.3], dtype=float)

    degree = len(years) - 1
    coeffs = np.polyfit(years - years.mean(), pct, degree)

    y_new = np.polyval(coeffs, years - years.mean())

    x_lagrange = np.linspace(1981, 2020, 46)
    y_lagrange = lagrange_int(years - years.mean(), pct, x_lagrange - years.mean())

    plt.figure(figsize=(8, 5))
    plt.plot(years, pct, 'o', label='Original Data')
    plt.plot(years, y_new, '-', label='Interpolation Polynomial')
    plt.plot(x_lagrange, y_lagrange, label='Lagrange Interpolation', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Households with Computer (%)')
    plt.title('Exact Lagrange Interpolation (x - x.mean())')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Die Lagrange Interpolation produziert ähnliche resultate wie das resultat aus Aufgabe b.
    # Jedoch fällt auf, dass Lagrange kurviger ist.
    # So gab es, laut Lagrange, einen Abfall um ca. 1986 auf 0%, was eher unwahrscheinlich ist.

def main():
    # aufgabe_2()
    aufgabe_3_a()
    aufgabe_3_b()
    # Aufgabe 3c: Teil a produziert für das Jahr 2020 eine vorhersage von 120%, Teil b sogar über 300%
    # Wie bereits in den vorhergehenden Teilen beschrieben ist dieses Polynom nicht wirklich brauchbar für werte Ausserhalb des Wertebereiches des originalen Datensets.
    # aufgabe_3_d()

if __name__ == '__main__':
    main()
