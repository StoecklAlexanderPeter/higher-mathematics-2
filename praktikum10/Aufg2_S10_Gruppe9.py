import numpy as np
from matplotlib import pyplot as plt

# Vertikal steigende Rakete
# a(t) = h''(t) = v_rel * (μ / (m_A - μ*t))-g
# μ = (dm/dt) = (m_A - m_E)/t_E

v_rel = 2600 # Ausströmgeschwindigket des Treibsofts 2600 m/s
m_A = 300000 # Anfangsmasse Ariane 4 m_A = 300'000 kg
m_E = 80000 # Endmasse Ariane 4 m_E = 80'000 kg
t_E = 190 # Zeit bis vollständig abgebrannt Arianne 4 = 190s
g = 9.81 # Fallbeschleunigung konstant 9.81m/s**2
mu = (m_A - m_E)/t_E # Massenstrom konstant
n = 100 # calculate in 100 steps

# h'(t) = v(t) = Integral(h''(t)) dt = Integral(a(t)) dt

def a(t):
    return v_rel * (mu / (m_A - mu * t)) - g

def Gruppe9_S8_Aufg_3(x, y):
    total = 0
    for i in range(0, len(x)-1):
        total += ((y[i] + y[i+1])/2)*(x[i+1] - x[i])

    return total

t = np.linspace(0, t_E, n)
a_y = np.zeros_like(t)
v_y = np.zeros_like(t)
h_y = np.zeros_like(t)

for k in range (1, len(t)):
    a_y[k] = a(t[k])
    v_y[k] = Gruppe9_S8_Aufg_3(t[:k+1], a_y[:k+1])

for k in range (1, len(t)):
    a_y[k] = a(t[k])
    h_y[k] = Gruppe9_S8_Aufg_3(t[:k+1], v_y[:k+1])

print(f"a) a(t_E)={a_y[-1]}m/s**2")
print(f"a) v(t_E)={v_y[-1]}m/s")
print(f"a) h(t_E)={h_y[-1]}m")

# b)
def v_analytisch(t):
    return v_rel * np.log(m_A / (m_A - mu * t)) - g * t

def h_analytisch(t):
    return - ((v_rel*(m_A - mu * t))/mu) * np.log(m_A / (m_A - mu * t)) + v_rel * t - 0.5 * g * t**2

v_analytische_loesung = v_analytisch(t[-1])
h_analytische_loesung = h_analytisch(t[-1])

print(f"Abweichung v: Berechnet={v_y[-1]}; Analytische Lösung ={v_analytische_loesung}; Absoluter Fehler={np.abs(v_y[-1]-v_analytische_loesung)}; Relativer Fehler={np.abs(h_y[-1]-h_analytische_loesung)/h_analytische_loesung}")
print(f"Abweichung h: Berechnet={h_y[-1]}; Analytische Lösung ={h_analytische_loesung}; Absoluter Fehler={np.abs(h_y[-1]-h_analytische_loesung)}; Relativer Fehler={np.abs(h_y[-1]-h_analytische_loesung)/h_analytische_loesung}")
# Wir sehen die Lösung ist bereits sehr genau.

plt.figure()
plt.plot(t, a_y, label="a(t)")
plt.legend()
plt.xlabel('t')
plt.ylabel('a(t)')
plt.title('Beschleunigung a(t)')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(t, v_y, label="v(t)")
plt.plot(t, v_analytisch(t), label="v_analytisch(t)")
plt.legend()
plt.xlabel('t')
plt.ylabel('v(t)')
plt.title('Geschwindigkeit v(t)')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(t, h_y, label="h(t)")
plt.plot(t, h_analytisch(t), label="h_analytisch(t)")
plt.legend()
plt.xlabel('t')
plt.ylabel('h(t)')
plt.title('Höhe h(t)')
plt.grid(True)
plt.show()



"""
def Gruppe9_S8_Aufg_3(f, a, b, n): # Trapezregel
    h = (b-a)/n
    sum = 0
    for i in range(1, n):
        x_i = a + i * h
        print(x_i)
        sum += f(x_i)
    return h * ((f(a) + f(b))/2 + sum)
"""