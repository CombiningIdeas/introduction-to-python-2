#Самостоятельная работа «Массивы»

#Вариант 3

#Задание №1. Отсортировать массив случайных чисел из диапазона [0, 1000] по убыванию количества в числе четных цифр.

import random

length = 10

array = [random.randint(0, 1000) for rand in range(length)]

print("Массив до сортировки:")
print(*array)

def evenNumbers(number):
    counter = 0
    for indexes in str(number):
        if int(indexes) % 2 == 0:
            counter += 1
    return counter

array.sort(key = evenNumbers, reverse = True)

print("Масcив после сортировки:")
print(*array)
