import numpy as np

def f(x_vector):
    x, y = x_vector
    return np.array([
        x ** 2 / 186 ** 2 - y ** 2 / (300 ** 2 - 186 ** 2) - 1,
        (y - 500) ** 2 / 279 ** 2 - (x - 300) ** 2 / (500 ** 2 - 279 ** 2) - 1
    ])


def jacobian(x_vector):
    x, y = x_vector
    return np.array([
        [ (2 * x) / (186 ** 2), (-2 * y) / (300 ** 2 - 186 ** 2)],
        [ (-2 * (x - 300)) / (500 ** 2 - 279 ** 2), (2 * (y - 500)) / (279 ** 2)]
    ])

def newton_method(x0, tol=1e-5, iterations=100):
    x_vector = np.array(x0, dtype=float)
    for i in range(iterations):
        J = jacobian(x_vector)
        delta_x = np.linalg.solve(J, -f(x_vector))
        x_new_vector = x_vector + delta_x

        f_x_k_normiert = np.linalg.norm(f(x_new_vector))

        x_vector = x_new_vector

        if f_x_k_normiert <= tol:
            return x_new_vector

# gefundene angenäherte Koordinaten aus Aufgabe 1
sp0 = [700, 910]
sp1 = [-1300, 1600]
sp2 = [250, -230]
sp3 = [-200, 70]

print(f"SP 1 = {newton_method(sp0)}")
print(f"SP 2 = {newton_method(sp1)}")
print(f"SP 3 = {newton_method(sp2)}")
print(f"SP 4 = {newton_method(sp3)}")