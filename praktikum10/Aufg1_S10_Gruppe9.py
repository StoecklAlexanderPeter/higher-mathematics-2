import numpy as np

def rhomberg(T: np.array, i = 0):
    print(T)
    T_next = np.empty(len(T)-1)
    i = i + 1
    for j in range(0, len(T)-1):
        T_next[j] = ((4**i)*T[j+1]-T[j])/((4**i)-1)
    if len(T_next) == 1:
        return T_next[0]
    return rhomberg(T_next, i)

def Gruppe9_S9_Aufg3(f, a, b, m):
    T0i = np.empty(m+1)
    for i in range(0, m+1):
        n_i = 2**i
        h_i = (b-a)/(2**i)
        i0_sum = 0
        for j in range(1, n_i):
            i0_sum = i0_sum + f(a + (j * h_i))

        Ti0 = h_i*(((f(a) + f(b))/2) + i0_sum)
        T0i[i] = Ti0

    return rhomberg(T0i)

# Aufgabe 1:
# Bei Landung:
# Zeit t = 0s; Koordinate x_0 = 0m;
# Geschwindigkeit v_0 = 100 m/s; Masse m = 97'000 kg
# c = 570000
# Bremskraft F = -5 * x'^2 - c

# a)
# Bewegungsgleichung DGL 2 Ordnung: m * x'' = -5 * x'^2 - c
# => x'' = (-5 * x'^2 - c) / m | v = x'
# => v' = (-5 * v'^2 - c) / m

# (dv/dt) = (-5v**2 - c)/m
# dv = ((-5v**2 - c)/m) dt
# (m / (-5v**2 - c)) dv = dt

# In Integral zeiten einsetzen = Von Startgeschwindigkeit zu Stillstand
# Integral(von v_0 bis 0)(m/(-5v**2-c))
# In unserer Funktion von Serie 0 muss a kleiner als b sein, dementsprechend können wir das Integral dem anpassen
# - Integral(von 0 bis v_0)(m/(-5v**2-c))

m = 97000
c = 570000
v_0 = 100

def dv(v):
    return m/(-5 * v**2 - c)

t_E = -Gruppe9_S9_Aufg3(dv, 0, v_0, 5)
print(t_E)

# t_E = 16.544607316744223
# Stillstand nach 16.5 Sekunden

# b)
# dx/dt = v
# dx = v * dt
# (m/(-5*v**2-c)) dv = dt | * v
# dx = (m*v/(-5v**2-c)) dv

# Integral(von v_0 bis 0)((m*v)/(-5v**2-c))
# In unserer Funktion von Serie 0 muss a kleiner als b sein, dementsprechend können wir das Integral dem anpassen
# - Integral(von 0 bis v_0)((m*v)/(-5v**2-c))

def dx(v):
    return (m * v)/(-5 * v**2 - c)

x_E = -Gruppe9_S9_Aufg3(dx, 0, v_0, 5)
print(x_E)

# x_E = 815.606236942252
# Stillstand nach 815.6 Meter