# Контрольная работа №4 «Массивы»

'''
Задание 3. Заполните массиве случайными числами в интервале [0, 1000] и выведите номера трех различных максимальных элементов.
Разрешается только один проход по массиву.
'''


import random

array = [random.randint(0, 1000) for ii in range(0, 10)]

print("Массив:")
print(*array)

numberMax1 = array[0]
numberMax2 = array[1]
numberMax3 = array[2]
array2 = [numberMax1, numberMax2, numberMax3]

for ii in range(3, len(array)):
    
    numberMin = numberMax1
    if numberMin > numberMax2:
        numberMin = numberMax2
        if numberMin > numberMax3:
            numberMin = numberMax3
        
    if numberMin > numberMax3:
        numberMin = numberMax3
        if numberMin > numberMax2:
            numberMin = numberMax2
        
    if numberMin < array[ii]:
        array2.remove(numberMin)
        array2.append(array[ii])
        numberMax1 = array2[0]
        numberMax2 = array2[1]
        numberMax3 = array2[2]


'''
array.sort()

for ii in range(len(array)):
    if numberMax1 < array[ii]:
        numberMax3 = numberMax2
        numberMax2 = numberMax1
        numberMax1 = array[ii]

'''


print("Максимальные значения: ", *array2)





