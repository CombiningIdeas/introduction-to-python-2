'''
Практическая работа № 53.	
Линейный поиск в массиве
'''

#Уровень A. Заполните массив случайными числами в интервале [0,5]. Введите число X и найдите все значения, равные X.
import random

N = 5
array = [0] * 5

for ii in range(N):
    array[ii] = random.randint(0, 5)

print("Массив")
print(*array)

X = int(input("Что ищем:\n"))

numX = 0
counter1 = 0
counter2 = 0

for numX in range(N):
    if array[numX] == X:
        counter1 += 1
        if counter1 > 0:
            print("Нашли: ", end = "")
            counter = -10
        print(f"array[{numX}] = {X} ", end = "")

    numX += 1
    
if counter1 == 0:
    print("Ничего не нашли")

    

