'''
Практическая работа № 57.	
Простые методы сортировки 
'''

#Уровень C. Напишите программу, которая сортирует массив по убыванию суммы цифр числа. Используйте функцию, которая определяет сумму цифр числа.

import random

lenght = 10

array = [random.randint(10, 100) for ss in range(0, lenght)]

print("Массив до обработки:")
print(*array)

def sumDigit(summ):
    counter = 0
    for index in str(summ):
        counter += int(index)
        #print(index) закоментированными строчками проверял как работает функция, вроде все верно, сортировка по сумма цифр числа от большего к меньшему.
    return counter, #print(counter)

for ii in range(lenght-1):
    for jj in range(lenght-2, ii-1, -1):
        if sumDigit(array[jj+1]) > sumDigit(array[jj]):
            array[jj], array[jj+1] = array[jj+1], array[jj]
            

print("Массив после обработки:")
print(*array)
