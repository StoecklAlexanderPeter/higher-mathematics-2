import numpy as np

def f(x):
    return np.array([[float(2*x[0]+4*x[1])], [float(4*x[0]+8*x[1]**3)]])

def Df(x):
    return np.array([[2,4], [4, float(24 * x[1]**2)]])

def newton(x):
    for i in np.arange(1, 6):
        delta = np.linalg.solve(Df(x), -f(x))
        x = x + delta
        print("Iteration", i)
        print("x = ", x)

x0_1 = np.array([[4], [2]])
newton(x0_1)
print("----")
x0_2 = np.array([[-4],[-2]])
newton(x0_2)
print("----")
x0_3 = np.array([[1],[0.4]])
newton(x0_3)