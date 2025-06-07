import numpy as np


# --- Funktionen für Aufgabe 5.6 a) (Bestimmung von k1, k2, k3) ---

# Definiert das nichtlineare Gleichungssystem f(k) = 0
# k ist ein numpy-Array der Form [[k1], [k2], [k3]]
def f_system_a(k):
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
def J_matrix_a(k):
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


# --- Allgemeine Newton-Löser-Funktion ---
def newton_solver(f_func, J_func, x_start, eps=1e-6, max_iter=100):
    """
    Löst ein nichtlineares Gleichungssystem f(x) = 0 mittels des Newton-Verfahrens.

    Args:
        f_func (function): Funktion, die den Vektor f(x) zurückgibt.
        J_func (function): Funktion, die die Jacobi-Matrix J(x) zurückgibt.
        x_start (np.array): Startvektor für die Iteration.
        eps (float): Toleranz für die Konvergenz (euklidische Norm von delta).
        max_iter (int): Maximale Anzahl von Iterationen.

    Returns:
        np.array: Die gefundene Lösung x.
    """
    x_current = x_start.copy()  # Kopie, um den Original-Startvektor nicht zu ändern
    print(f"Startpunkt (x^(0)):\n{x_current.flatten()}\n")

    for i in range(1, max_iter + 1):
        print(f"--- Iteration {i} ---")

        jacobian_matrix = J_func(x_current)
        function_value = f_func(x_current)

        # Überprüfe, ob die Jacobi-Matrix singulär ist (Determinante nahe Null)
        det_jacobian = np.linalg.det(jacobian_matrix)
        if abs(det_jacobian) < 1e-15:
            print(f"FEHLER: Jacobi-Matrix ist in Iteration {i} singulär (Determinante: {det_jacobian:.2e}). Abbruch.")
            break

        # Löse das lineare Gleichungssystem J(x) * delta = -f(x)
        # np.linalg.solve ist numerisch stabiler und effizienter als explizite Inversion
        delta = np.linalg.solve(jacobian_matrix, -function_value)

        # Berechne die euklidische Norm von delta für die Konvergenzprüfung
        norm_delta = np.linalg.norm(delta)

        print(f"Aktueller Wert (x^(i-1)):\n{x_current.flatten()}")
        print(f"Korrektur (delta^(i-1)):\n{delta.flatten()}")
        print(f"||delta^(i-1)|| (Euklidische Norm): {norm_delta:.8e}")

        # Aktualisiere x
        x_current = x_current + delta
        print(f"Neuer Wert (x^{i}):\n{x_current.flatten()}")

        # Überprüfe die Abbruchbedingung
        if norm_delta < eps:
            print(f"\nKonvergenz erreicht! ||delta|| < eps ({norm_delta:.8e} < {eps:.8e}).")
            break
        print("-" * 40)  # Trennlinie zwischen Iterationen
    else:  # Wird ausgeführt, wenn die Schleife ohne 'break' endet
        print("\nWARNUNG: Maximale Iterationszahl erreicht, Konvergenz wurde nicht erzielt.")

    return x_current


# --- Aufgabe 5.6 a) lösen ---
print("### Aufgabe 5.6 a) - Bestimmung von k1, k2, k3 ###\n")

# Startvektor k^(0)
k0_start = np.array([[10.0], [0.1], [1.0]])

# Löse das System
solution_k = newton_solver(f_system_a, J_matrix_a, k0_start, eps=1e-6)

print("\n--- Endergebnis für k1, k2, k3 ---")
print(f"k1 = {solution_k[0, 0]:.6f}")
print(f"k2 = {solution_k[1, 0]:.6f}")
print(f"k3 = {solution_k[2, 0]:.6f}")

# --- Aufgabe 5.6 b) lösen ---
# Die gefundenen k-Werte müssen in die Funktionen für Teil b) übernommen werden
k1_sol = solution_k[0, 0]
k2_sol = solution_k[1, 0]
k3_sol = solution_k[2, 0]


# Definiert die Funktion h(r) = 0 für Teil b)
# p_required = k1*exp(k2*r) + k3*r
# p_generated = 500 / (pi*r^2)
# Wir suchen r, so dass p_required = p_generated, also h(r) = p_required - p_generated = 0
def h_function_b(r_val_array):
    r = r_val_array[0, 0]  # r ist ein Skalar, aber wird in ein 2D-Array gepackt übergeben
    val = k1_sol * np.exp(k2_sol * r) + k3_sol * r - 500 / (np.pi * r ** 2)
    return np.array([[val]])  # Rückgabe als 2D-Array für den Newton-Solver


# Definiert die Ableitung h'(r) für Teil b)
def h_prime_function_b(r_val_array):
    r = r_val_array[0, 0]  # r ist ein Skalar
    val = k1_sol * k2_sol * np.exp(k2_sol * r) + k3_sol + 1000 / (np.pi * r ** 3)
    return np.array([[val]])  # Rückgabe als 2D-Array


print("\n\n### Aufgabe 5.6 b) - Bestimmung der minimalen Grösse r ###")

# Schätzung für den Startpunkt von r. Die gegebenen r waren 1, 2, 3.
# Bei 500 N Last wird r wahrscheinlich größer sein. Ein Versuch mit r=4.0
r0_start_b = np.array([[15.0]])

# Löse die Gleichung h(r) = 0
solution_r = newton_solver(h_function_b, h_prime_function_b, r0_start_b, eps=1e-6)

print("\n--- Endergebnis für minimale Grösse r ---")
print(f"Minimale Grösse (Radius r) = {solution_r[0, 0]:.6f} cm")

# --- Überprüfung der Ergebnisse (Optional) ---
print("\n--- Überprüfung der Ergebnisse ---")
# Für k1, k2, k3
f_at_solution_k = f_system_a(solution_k)
print(f"f(k_solution) (sollte nahe Null sein):\n{f_at_solution_k.flatten()}")

# Für r
h_at_solution_r = h_function_b(solution_r)
print(f"h(r_solution) (sollte nahe Null sein):\n{h_at_solution_r.flatten()}")

# Check the pressure values for the found r
final_r = solution_r[0, 0]
pressure_required_at_final_r = k1_sol * np.exp(k2_sol * final_r) + k3_sol * final_r
pressure_from_500N = 500 / (np.pi * final_r ** 2)
print(f"\nBenötigter Druck bei r={final_r:.4f} cm: {pressure_required_at_final_r:.4f} N/cm^2")
print(f"Druck, der durch 500N Last bei r={final_r:.4f} cm entsteht: {pressure_from_500N:.4f} N/cm^2")