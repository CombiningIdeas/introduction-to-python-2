#Практическая 75 B

#3. Для примера «Полет мяча» вычислите длину траектории движения шарика для углов вылета 35,5° и 65,8°.
#Сравните полученные результаты. 

import math

def f(x):
    return x - math.cos(x)

eps = 0.001
x = 0
delta = 2*eps

# 1 радиан равен 57,2958 градусов. перевод из градусов в радианы:
startAlpha = 35.5
u = startAlpha # в радианах
while u < math.pi/2:
    if f(u)*f(u+delta) <= 0:
        alpha = (u + eps)*180/math.pi
        print("Угол: {:4.1f}".format(alpha), " градусов")
    u += delta

