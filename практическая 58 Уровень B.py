'''
Практическая работа № 58.	
Сортировка слиянием
'''

#Уровень B. Напишите программу, которая сортирует массив и находит количество различных чисел в нем.

import random

lenght = 10

array = [random.randint(0, 10) for ss in range(0, lenght)]

print("Массив:")
print(*array)

count = 0

for ii in range(lenght-1):
    for jj in range(lenght - 2, ii-1, -1):
        if array[jj+1] < array[jj]:
            array[jj], array[jj+1] = array[jj+1], array[jj]

for indexes in range(lenght-1):
    if array[indexes] == array[indexes+1]:
        count += 1


differentNumbers = lenght - count

print("После сортировки:")
print(*array)
print(f"Различных чисел: {differentNumbers}")
