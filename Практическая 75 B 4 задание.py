#Практическая 75 А

#4. Найдите площадь фигуры, ограниченной графиками функций.

import math

def f1(x):
    return 4*math.cos(math.radians(x))

def f2(x):
    return x**2


a = -1.15 
b = 1.15
x = a
S = 0
h = 0.001 

while x < b:
    S += f1(x) - f2(x) + f1(x+h) - f2(x+h)
    x += h

S *= h/2
print("Площадь {:8.3f}".format(S))
