# Вывести целую часть от деления -9 на 4
print(-9 // 4)
#Вывести число 2/3 в 6 позициях с тремя знаками после десятичной точки
print("{:6.3f}".format(2 / 3))
#Вывести число 1/9 в экспоненциальном формате в 10 позициях и двумя знаками после десятичной точки
print("{:10.2e}".format(1 / 9))
#Перевести число 127 в двоичную систему счисления
print(bin(127))
#Подключить модуль math
import math
#Загрузить все функции модуля math
from math import *
#Случайное число от 1 до 10
from random import *
print(randint(1, 10))
#Случайное вещественное число из полуинтервала [0, 1)
print(random())
#Случайное вещественное число из полуинтервала [3, 7)
print(uniform(3, 7))
