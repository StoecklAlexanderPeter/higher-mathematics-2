import numpy as np


# Definiert das nichtlineare Gleichungssystem f(k) = 0
# k ist ein numpy-Array der Form [[k1], [k2], [k3]]
def f(k):
    k1 = k[0, 0]
    k2 = k[1, 0]
    k3 = k[2, 0]

    # r = 1, p = 10
    eq1 = k1 * np.exp(k2 * 1) + k3 * 1 - 10
    # r = 2, p = 12
    eq2 = k1 * np.exp(k2 * 2) + k3 * 2 - 12
    # r = 3, p = 15
    eq3 = k1 * np.exp(k2 * 3) + k3 * 3 - 15
    return np.array([[eq1], [eq2], [eq3]])


# Definiert die Jacobi-Matrix J(k) für das System f_system_a
def Df(k):
    k1 = k[0, 0]
    k2 = k[1, 0]
    # k3 ist nicht direkt in den Ableitungen k1 und k2 enthalten, aber in den Ableitungen nach k3

    # Partielle Ableitungen: J_ij = df_i / dk_j
    j11 = np.exp(k2)
    j12 = k1 * np.exp(k2)
    j13 = 1.0

    j21 = np.exp(2 * k2)
    j22 = 2 * k1 * np.exp(2 * k2)
    j23 = 2.0

    j31 = np.exp(3 * k2)
    j32 = 3 * k1 * np.exp(3 * k2)
    j33 = 3.0

    return np.array([[j11, j12, j13],
                     [j21, j22, j23],
                     [j31, j32, j33]])

def gedaempftes_newton(x, kmax):
    for i in np.arange(1, 6):
        df = Df(x)
        delta = np.linalg.solve(df, -f(x))

        ## Schritt 2: finde minimales k
        min_k = 0
        min_found_value = np.linalg.norm(f(x))
        for k in np.arange(0, kmax+1):
            norm_f_test = np.linalg.norm(f(x) + (delta/(2**k)))
            if norm_f_test < min_found_value:
                min_k = k
                min_found_value = norm_f_test

        x = x + (delta/(2**min_k))
        print("Iteration", i)
        print("x = ", x)
        print("eps = ", np.linalg.norm(f(x)))

x0_1 = np.array([[10.0], [0.1], [1.0]])
gedaempftes_newton(x0_1, 4)
# k =  [[ 8.77128645] [ 0.25969545] [-1.37228132]]
# in Funktion einsetzten gibt: p = 8.771286 * e^(0.259695*r) - 1.372281 * r

# Aufgabe b) minimale Grösse eines runden Gegensatndes welcher Belastung von 500N aushält und weniger als 30 cm tief sinkt.

# Wenn wir das mit r=30 visualisieren würden, würden wir sehen das dies bei circa 15 cm ist.
# r_n+1 = r_n - (f(r_n)/f'(r_n))

def gefundene_f(r):
    return 8.771286 * np.exp(0.259695 * r) - 1.372281 * r - 500

def d_gefundene_f(r):
    return 8.771286 * 0.259695 * np.exp(0.259695 * r) - 1.372281

r = 15
for i in np.arange(1, 10):
    r = r - (gefundene_f(r)/d_gefundene_f(r))
    print(i)
    print(r)

# Lösung konvergiert gegen r_0 = 15.731511 cm





