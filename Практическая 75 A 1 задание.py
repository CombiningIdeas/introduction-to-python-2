#Практическая 75 А

#1. Найдите длину параболы   на отрезке [0; 10].

import math

def f(x):
    return x**2

a = 0
b = 10
x = a
L = 0
h = 0.001

while x < b:
    y1 = f(x)
    y2 = f(x+h)
    L += math.sqrt(h**2 + (y2-y1)**2)
    x += h
    
print("Длина кривой {:5.3f}".format(L))


