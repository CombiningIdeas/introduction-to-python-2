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

counterArray = []

for indexes in range(lenght):
    if not array[indexes] in counterArray:
        counterArray.append(array[indexes])


    
for ii in range(lenght-1):
    for jj in range(lenght - 2, ii-1, -1):
        if array[jj+1] < array[jj]:
            array[jj], array[jj+1] = array[jj+1], array[jj]



differentNumbers = len(counterArray)

print("После сортировки:")
print(*array)
print(f"Различных чисел: {differentNumbers}")
