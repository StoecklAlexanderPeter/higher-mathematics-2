import numpy as np

radius_in_km = np.array([0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370])
radius_in_m = radius_in_km * 1000

dichte_in_kg_m = np.array([13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300])

def f(r, rho): return rho * 4 * np.pi * r**2;

def trapez_tab():
    total = 0
    for i in range(0, len(radius_in_m)-1):
        x_i = radius_in_m[i]
        x_i_plus_1 = radius_in_m[i+1]

        y_i = f(x_i, dichte_in_kg_m[i])
        y_i_plus_1 = f(x_i_plus_1, dichte_in_kg_m[i+1])

        total += ((y_i + y_i_plus_1)/2)*(x_i_plus_1 - x_i)

    return total

result = trapez_tab()
print(result)

# Erdmasse von Wikipedia 5,9722* 10^24, https://de.wikipedia.org/wiki/Erdmasse
totaler_wert = 5.9722*10**24
absoluter_Fehler =np.abs(totaler_wert - result)
print(f"absoluter Fehler={absoluter_Fehler}")
relativer_Fehler = np.abs(result - totaler_wert)/totaler_wert
print(f"relativer Fehler={relativer_Fehler}")

