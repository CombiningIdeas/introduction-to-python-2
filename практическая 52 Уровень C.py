'''
Практическая работа № 52.	
Перебор элементов массива
'''
#Уровень C. Заполните массив случайными числами в интервале [2,100] и подсчитайте среднее значение всех элементов,
#которые представляют собой простые числа.
import random

print("Массив: ")
arrayN = []

def isPrime(n):
    k = 2
    while k*k <= n and n % k != 0:
        k += 1
    if k*k > n:
        return arrayN.append(n)



N = random.randint(1, 15)
array = [0] * N

for index in range(N):
    array[index] = random.randint(2, 100)
    isPrime(array[index])


    
counter = 0
summ = 0

for jj in arrayN:
    counter += 1
    summ += jj
if counter == 0:
    counter = 1#чтобы не делил на 0 иначе ошибка будет
    
print(array)
print("Простые числа: ")
print(arrayN)
print(f"Среднее арифметическое: {summ/counter}")
