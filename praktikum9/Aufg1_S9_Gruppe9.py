import sympy

# Wie gross ist h, die Anzahl benötigter Subintervalle n, um Integral auf Fehler
# von max 10**−5 zu berchnen
# Integral: f(x) = (ln(x**2) von [1, 2]
# Integral von Hand aus berechnen:
# f(x) = 2 * ln(x) von [1, 2]
# x * ln(x)− x + C
# (2 * ln(2) − 2) - (1 * ln(1) -1)
# 2 * ln(2) − 1
# 4 * ln(2) - 2

b = 2
a = 1
tol = 10**-5

def f(x): return 2*sympy.ln(x)
def df(x): return 2/x
def ddf(x): return -2/x**2
def dddf(x): return 4/x**3
def ddddf(x): return -12/x**4


# für die summierten Rechtecksregel
# aus ablesen an Start: f'' am grössten bei x = 1;
# |f''(1)| = 2;
# einsetzen:
# (h**2)/24 * (b-a) * | max f''(x) | <= 10**−5
# (h**2)/24 * (2-1) * |f''(1)| <= 10**−5
# (h**2)/24 * 2 <= 10**−5
# (h**2)/12 <= 10**−5
# (h**2)/12 <= 10**−5 | = *12
# (h**2) <= 12 * 10**−5 | Wurzelziehen
# h <= sqrt(12 * 10**−5)
# h <= 0.01095445115
# einsetzten
h1 = 0.01095445115
print("Rechtecksregel)")
print(f"kalkuliertes h: {h1}")
result1 = (h1**2)/24 * (b-a) * 2
print(f"Absoluter Fehler={result1}; Kleiner als Toleranz={result1 < tol}")
n1 = (b-a)/h1
print(f"Anzahl Teilintervale: {n1}")
# Anzahl Teilintervale 92

# für die summierte Trapezregel
# aus ablesen an Start: f'' am grössten bei x = 1;
# |f''(1)| = 2;
# einsetzen:
# (h**2)/12 * (b-a) * | max f''(x) | <= 10**−5
# (h**2)/12 * (2-1) * |f''(1)| <= 10**−5
# (h**2)/12 * 2 <= 10**−5
# (h**2)/6 <= 10**−5
# (h**2)/6 <= 10**−5 | = *6
# (h**2) <= 6 * 10**−5 | Wurzelziehen
# h <= sqrt(6 * 10**−5)
# h <= 0.00774596669
# einsetzten
h2 = 0.00774596669
print("Trapezregel)")
print(f"kalkuliertes h: {h2}")
result2 = (h2**2)/12 * (b-a) * 2
print(f"Absoluter Fehler={result2}; Kleiner als Toleranz={result2 < tol}")
n2 = (b-a)/h2
print(f"Anzahl Teilintervale: {n2}")
# Anzahl Teilintervale 130

# für die summierte Simpsonregel?
# (h**4)/2880 * (b-a) * | max f''''(x) | <= 10**−5
# |f''''(x)| wird bei x = 1 maximal, da Funktion stetig abnehmend
# |f''''(1)|  = -12/1**4 => -12 => 12
# einsetzen
# (h**4)/2880 * 1 * 12 <= 10**−5
# (h**4)/240 <= 10**−5 | * 240
# (h**4) <= 240 * 10**−5 | 4te Wurzel Ziehen
# h <= sqrt4(240 * 10**−5)
# h <= 0.221336
# einsetzten
h3 = 0.221336
print("Simpsonregel)")
print(f"kalkuliertes h: {h3}")
result3 = (h3**4)/2880 * (b-a) * 12
print(f"Absoluter Fehler={result3}; Kleiner als Toleranz={result3 < tol}")
n3 = (b-a)/h3
print(f"Anzahl Teilintervale: {n3}")
# Anzahl Teilintervale: 5