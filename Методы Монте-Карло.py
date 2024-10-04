
#from random import random
#from random import *
import random

N = 100000
M = 0

#random.rabdom() - выводит случайное число в диапозоне от [0;1), тоесть
#включая 0 но не включая 1. не всегда можно сделать многостроынй коментарий 
#с помощью многострочного литерала

for i in range(N):
    x = random.random()
    y = random.random()
    if x*x+y*y <= 1:
        M += 1
print("PI =", 4*M/N)


#from random import random, randint
import random

L = 480#это в минутах рабочий день, в часах 8 часов
Pmax = 4#максимальное число входящих за 1 минуту
Tmin = 1#минимальное время обслуживания
Tmax = 1#минимальное время обслуживания
M = 15#допустимое время ожидания
T = 0#сначала в банке никого нет
count = 0#счетчик плохих минут
# нужно еще ввести число кассиров K

for i in range(L):
    P = random.randint(0, Pmax)
    T = Tmin + random.random() * (Tmax-Tmin)
    R = round(K/T)
    #round() - округление чисел, если дробная часть числа меньше 0.5 то округляется вниз
    N += P - R
    if N < 0:
        N = 0
        dT = N / K * T
    if dT > M:
        count += 1

