from praktikum12_optional.Aufg1_S12_Gruppe9 import Gruppe9_S12_Aufg1
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # a)
    def f(x, y): return 1 - (y/x)

    def f_analytisch(x): return (x/2) + (9/(2*x))

    a = 1
    b = 6
    y0 = 5
    n = 500 # 0.01 => 500 = 5 / 0.01

    x, y = Gruppe9_S12_Aufg1(f, a, b, n, y0)
    print(x)
    print(y)

    plt.figure()
    plt.plot(x, y, label="Runge Kutta")
    plt.plot(x, f_analytisch(x), label="analytische Loesung")
    plt.legend()
    plt.grid(True)
    plt.show()

    # b, c & d) Nicht implementiert aber Begründung:
    # Die Koeffizienten im Runga-Kutta-Verfahren sind so gewählt das die numerische Lösung der exakten lösung einer bestimmten Ordnung approximiert.
    # Beim ändern, wird die Übereinstimmung mit der Taylor Reihe zerstört. Annäherung spielt verrückt keine Konvergenz mehr oder ungenauer.