'''
Практическая работа № 52.	
Перебор элементов массива
'''
#Уровень A. Заполните массив случайными числами в интервале [0,100] и найдите среднее ариф-метическое его значений.
import random

print("Массив: ")

N = random.randint(0, 25)
array = [0] * N

counter = 0
summ = 0

for index in range(N):
    array[index] = random.randint(0, 100)
    counter += 1
    summ += array[index]

print(array)
print(f"Средне арифметическое {summ/counter}")
