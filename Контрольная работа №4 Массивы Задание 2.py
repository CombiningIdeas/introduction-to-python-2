# Контрольная работа №4 «Массивы»

'''
Задание №2. Заполните массив случайными числами в нтервале[100, 999] и представте их по убыванию количества делителей
'''

import random

array = [random.randint(10, 20) for ii in range(0, 10)]

print("Массив:")
print(*array)
array2 = list(array)


def divisors(n):
    counter = 0
    k = 1
    while k <= n:
        if n % k == 0:
            counter += 1
        k += 1
    return counter


def QuickSort(sortArray, first, last):
    if first >= last:
        return array2
    flag = sortArray[random.randint(first, last)]
    left, right = first, last
    while left <= right:
        while sortArray[left] < flag:
            left = left + 1
        while sortArray[right] > flag:
            right = right - 1
        if left <= right:
            sortArray[left], sortArray[right] = sortArray[right], sortArray[left]
            left, right = left + 1, right - 1

    QuickSort(sortArray, first, right)
    QuickSort(sortArray, left, last)

QuickSort(array2, 0, len(array2) - 1)
       


array2.sort(key = divisors, reverse = True)


print("Итоговый массив:", *array2)






