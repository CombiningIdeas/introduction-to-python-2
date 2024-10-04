'''
Практическая работа № 55.	
Алгоритмы обработки массивов
'''

#Уровень A. Заполнить массив случайными числами и выполнить циклический сдвиг элементов массива вправо на 1 элемент.

import random 
n = 7

array = [random.randint (0, 6) for i in range(0, 7)]
array2 = list(array)
print("Массив:")
print(*array)

c = array[n - 1]

for ii in range (n - 1, 0, -1):
    array[ii] = array[ii - 1]
    
array[0] = c
print("Результат циклом:")
print (*array)

array2 = [array2[n - 1]] + array2[:n - 1:]
print("Результат срезом:")
print(*array2)

