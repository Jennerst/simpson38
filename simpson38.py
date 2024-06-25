import math

def simpson_3_8(f, a, b):
    h = (b - a) / 3
    
    x0 = a
    x1 = a + h
    x2 = a + 2 * h
    x3 = b
    
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    
    integral = 3 * h * (f0 + 3*f1 + 3*f2 + f3) / 8
    return integral

def f(x):
    return math.exp(-x**2)

a = 0
b = 1

approx_integral = simpson_3_8(f, a, b)

print(f"Aproximación de la integral de e^(-x^2) en [0, 1] usando la Regla de Simpson 3/8: {approx_integral:.4f}")