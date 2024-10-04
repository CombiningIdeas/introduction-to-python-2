'''
Практическая работа № 58.	
Сортировка слиянием
'''

#Уровень A. Массив содержит четное количество элементов. Напишите программу, которая сортирует первую половину массива по возрастанию,
#а вторую – по убыванию.
#Каждый элемент должен остаться в «своей» половине.

import random

lenght = 8

array = [random.randint(0, 10) for ss in range(0, lenght)]

print("Массив до обработки:")
print(*array)

array2 = array[:lenght// 2:]
array3 = array[lenght// 2::]

for ii in range((lenght//2)-1):
    for jj in range((lenght//2)-2, ii-1, -1):
        if array2[jj+1] < array2[jj]:
            array2[jj], array2[jj+1] = array2[jj+1], array2[jj]

print("Массив2 после обратобке:")
print(*array2)

for ii in range((lenght//2)-1):
    for jj in range((lenght//2)-2, ii-1, -1):
        if array3[jj+1] > array3[jj]:
            array3[jj], array3[jj+1] = array3[jj+1], array3[jj]
            

print("Массив3 после обработки:")
print(*array3)

array = array2 + array3

print("Массив после обрабтки:")
print(*array)
