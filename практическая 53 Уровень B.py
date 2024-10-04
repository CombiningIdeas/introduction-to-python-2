'''
Практическая работа № 53.	
Линейный поиск в массиве
'''

#Уровень B. Заполните массив случайными числами в интервале [0,5]. Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
import random

N = 5
array = [0] * 6

for ii in range(N):
    array[ii] = random.randint(0, 5)

print("Массив")
print(*array)

count = 0

for numX in range(N):
    if array[numX] == array[numX + 1]:
        print(f"Ecть: {array[numX]}")
        count += 1
        
if count == 0:
    print("Нет")
