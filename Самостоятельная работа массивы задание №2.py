#Самостоятельная работа «Массивы»

#Вариант 3

'''
Задание №2. В массиве случайных чисел элементы могут принимать целые значения от -10 000 до 10 000 включительно.
Определите и запишите в ответе сначала количество пар элементов, сумма которых кратна 3 и не кратна 6,
а произведение оканчивается на 8, затем максимальную из сумм элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента массива.
'''

import sys
import random

length = 100

array = [random.randint(-10000, 10000) for rand in range(length)]


specialNumbers = []
def coupleElements(long):
    for indexes in range(long - 1):
        if (abs(array[indexes] + array[indexes+1]) % 3 == 0) and (abs(array[indexes] + array[indexes+1]) % 6 != 0) and \
        (abs(array[indexes] * array[indexes+1]) % 10 == 8):
            digit = array[indexes] + array[indexes+1]
            specialNumbers.append(digit)
            
coupleElements(length)

if not specialNumbers:
    print("Массив пустой")
    sys.exit([])

print("Массив особых чисел:")
print(*specialNumbers)
#Можно было проверку на пустоту еще так записать:
'''
if len(specialNumbers) == 0:
    print("Массив пустой")
    sys.exit([])
'''
quantity = len(specialNumbers)
maximumElement = max(specialNumbers)

print("Количество нужных эелментов:")
print(quantity)

print(f"Максимальных из нужных элементов: {maximumElement}")

