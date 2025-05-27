import numpy as np

def f(x): return np.cos(x**2)

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

# result = Gruppe9_S9_Aufg3(f, 0, np.pi, 4)
# print(result)
# stimmt überein