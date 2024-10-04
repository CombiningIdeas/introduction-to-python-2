'''
Практическая работа № 56.	
Отбор элементов массива по условию
'''

#Уровень A. Заполнить массив случайными числами в интервале [-10,10] и отобрать в другой мас-сив все чётные отрицательные числа.

import random

long = 7

array = [random.randint(-10, 10) for ii in range(long)]
array2 = []

print("Массив А:")
print(*array)

for jj in range(0, long):
    if (array[jj] < 0) and (array[jj] % 2 == 0):
        array2.append(array[jj])


print("Массив B:")
print(*array2)
