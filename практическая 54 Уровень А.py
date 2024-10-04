'''
Практическая работа № 54.	
Поиск максимального элемента массива
'''

#Уровень A. Заполните массив случайными числами и найти минимальный и максимальный эле-менты массива и их номера.

'''
import random

print("Массив")
long = 6

array = []
for index in range(0, long):
    array.append(random.randint(0,long))
    
print(*array)

arMin = 0
arMax = 0
nMax = array[0]
nMin = array[0]
for ii in range(long):
    if array[ii] > nMax:
        nMax = array[ii]
        arMax = ii
    if nMin > array[ii]:
        nMin = array[ii]
        arMin = ii


print(f"Минимальный элемент: array[{arMin}] = {nMin} \nМаксимальный элемент: array[{arMax}] = {nMax}")
'''

import random

print("Массив")
long = 6

array = []
for index in range(0, long):
    array.append(random.randint(0,long))
    
print(*array)


nMax = max(array)
nMin = min(array)

arMin = array.index(nMin)
arMax = array.index(nMax)


print(f"Минимальный элемент: array[{arMin}] = {nMin} \nМаксимальный элемент: array[{arMax}] = {nMax}")













