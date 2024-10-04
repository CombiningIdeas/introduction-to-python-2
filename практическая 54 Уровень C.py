'''
Практическая работа № 54.	
Поиск максимального элемента массива
'''

#Уровень C. Введите массив с клавиатуры и найдите (за один проход) количество элементов, имеющих максимальное значение.


import random

long = 7
array = []
for i in range(0, long):
    array.append(random.randint(0, long))
print("Массив:")
print(*array)

nMax = max(array)
count = 0
for ii in range (0, long) :
    if array[ii] == nMax :
        count += 1


print("Максимальное значение", nMax)
print("Количество элементов", count)
