'''
Практическая работа № 54.	
Поиск максимального элемента массива
'''

#Уровень B. Заполните массив случайными числами и найти два максимальных элемента массива и их номера.

import random

nn = 6

array = []
for i in range(0, nn):
    array.append(random.randint(0,nn))

print("Массив:")
print(*array)


nMax1 = max(array)
number1 = array.index(nMax1)

if nMax1 in array:
    array.remove(nMax1)

array2 = array

nMax2 = max(array2)
number2 = array2.index(nMax2)
    
print(f"Максимальный элемент: array[{number1}] = {nMax1} \nВторой максимум: array[{number2}] = {nMax2} ")
