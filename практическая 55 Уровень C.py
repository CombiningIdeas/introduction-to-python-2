'''
Практическая работа № 55.	
Алгоритмы обработки массивов
'''


#Уровень C. Заполнить массив случайными числами в интервале [-100,100] и переставить элементы так,
#чтобы все положительные элементы стояли в начала массива, а все отрицательные и нули – в конце.
#Вычислите количество положительных элементов.


import random

long = 6
array = [random.randint(-1, 1) for ii in range(0, long)]
print(*array)
count = 0
last = long - 1

for jj in range(long):
    if array[jj] > 0:
        variable = array[count]
        array[count] = array[jj]
        array[jj] = variable
        count += 1
        
print(*array)
array2 = array[long // 2::]
print(*array2)

for hh in range(1):
    if array2[hh] == 0:
        value = array2[last]
        array2[last] = array2[hh]
        array2[hh] = value
        last -= 1

array = array[:long // 2:] + array2
print(*array)

