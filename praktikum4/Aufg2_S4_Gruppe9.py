import sympy as sp

def larange_int(x, y, x_int):
    x_sym = sp.symbols("x")
    l = sp.MutableDenseMatrix(x.rows, x.cols, [1]*x.rows)  # initialize with ones

    for i in range(x.rows):
        for j in range(x.rows):
            if i != j:
                l[i] *= (x_sym - x[j]) / (x[i] - x[j])

    # p aufbauen
    p = 0
    for i in range(x.rows):
        p += y[i] * l[i]

    # p evaluieren
    result = p.subs(x_sym, x_int)

    return sp.simplify(p), result


if __name__ == '__main__':
    x1 = sp.Matrix([0, 2500, 5000, 10000])
    y1 = sp.Matrix([1013, 747, 540, 226])

    print(x1)

    poly, value = larange_int(x1, y1, 3750)

    print("Interpolating Polynomial:")
    sp.pprint(poly, use_unicode=True)

    print("\nValue at x = 3750:")
    print(value) # stimmt überein.