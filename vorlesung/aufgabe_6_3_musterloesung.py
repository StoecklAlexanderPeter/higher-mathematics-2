def calculate_Pn_of_x(x):
    """
    Berechnet den Wert des Polynoms P_n(x) für ein gegebenes x.
    Das Polynom ist definiert als:
    P_n(x) = (13/240)x^3 - (133/80)x^2 + (2137/120)x - (263/5)

    Args:
        x (float oder int): Der Wert, für den das Polynom berechnet werden soll.

    Returns:
        float: Der berechnete Wert des Polynoms P_n(x).
    """
    term1 = (13 / 240) * (x**3)
    term2 = -(133 / 80) * (x**2)
    term3 = (2137 / 120) * x
    term4 = -(263 / 5)

    Pn_x = term1 + term2 + term3 + term4
    return Pn_x

# Beispielhafte Verwendung:
x_value = 11.0 # Beispiel: Temperatur um 11 Uhr (repräsentiert durch x=11, da 8.00 Uhr x=8 ist)
result = calculate_Pn_of_x(x_value)
print(f"Der Wert von P_n({x_value}) ist: {result}")

x_value_2 = 10.0
result_2 = calculate_Pn_of_x(x_value_2)
print(f"Der Wert von P_n({x_value_2}) ist: {result_2}") # Sollte 13.4 sein, da x_value_2 ein Stützpunkt ist