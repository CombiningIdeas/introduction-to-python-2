'''
Практическая работа № 57.	
Простые методы сортировки 
'''

#Уровень A. Напишите программу, в которой сортировка выполняется «методом камня» – самый «тяжёлый» элемент опускается в конец массива.

import random

lenght = 10

array = [random.randint(10, 100) for jj in range(0, lenght)]

print("Массив до обратобки:")
print(*array)


for ii in range(lenght):
    for kk in range(lenght-ii-1):
        if array[kk+1] < array[kk]:
            array[kk], array[kk+1] = array[kk+1], array[kk]


print("Массив после обратобки:")
print(*array)

