'''
Практическая работа № 56.	
Отбор элементов массива по условию
'''

#Уровень B. Заполнить массив случайными числами в интервале [0,100] и отобрать в другой мас-сив все простые числа.
#Используйте логическую функцию, которая определяет, является ли переданное ей число простым.


import random

long = 10

array = [random.randint(0, 100) for ii in range(long)]
array2 = []

print("Массив А:")
print(*array)

def isPrime(n):
    k = 2
    while k*k <= n and n % k != 0:
        k += 1
    return (k*k > n)

for jj in range(long):
    if isPrime(array[jj]) == True:
        array2.append(array[jj])

print("Массив B:")
print(*array2)





