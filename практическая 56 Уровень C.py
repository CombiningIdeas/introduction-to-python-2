'''
Практическая работа № 56.	
Отбор элементов массива по условию
'''


#Уровень C. Заполнить массив случайными числами и отобрать в другой массив все числа Фибо-наччи.
#Используйте логическую функцию, которая определяет, является ли переданное ей число числом Фибоначчи.

import random

long = 20

array = [random.randint(0, 100) for ii in range(long)]
array2 = []

print("Массив А:")
print(*array)

def fibonacci(n):
  a, b = 1, 1
  for kk in range(2, 1000):
    a, b = b, a + b
    if a == n:
        return True

for jj in range(long):
    if fibonacci(array[jj]) == True:
        array2.append(array[jj])

print("Массив B:")
print(*array2)
