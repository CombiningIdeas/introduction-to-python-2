'''
Практическая работа № 57.	
Простые методы сортировки 
'''

#Уровень B. Напишите вариант метода пузырька, который заканчивает работу, если на очеред-ном шаге внешнего цикла не было перестановок.

import random

lenght = 10

array = [random.randint(1, 10) for ss in range(0, lenght)]

print("Массив до обратобки:")
print(*array)

for ii in range(lenght-1):
    count = 0
    for jj in range(lenght-2, ii-1, -1):
        if array[jj+1] < array[jj]:
            array[jj], array[jj+1] = array[jj+1], array[jj]
            count = 1
            
    if count == 0:
        break
print("Массив после обратобки:")
print(*array)
