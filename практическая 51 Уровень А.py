
'''
Практическая работа № 51.	
Заполнение массива
'''
#Уровень A. Введите с клавиатуры числа A и B (A < B) и заполните массив случайными числами на отрезке [A; B].

import random

num1, num2 = map(int, input("Введите границы диапазона:\n").split())

array = [random.randint(num1, num2) for index in range(5)]

print("Мaссив:")
print(*array)
