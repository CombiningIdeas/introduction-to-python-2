'''
Практическая работа № 55.	
Алгоритмы обработки массивов
'''

#Уровень B. Массив имеет четное число элементов. Заполнить массив случайными числами и вы-полнить реверс отдельно в первой половине и второй половине.

import random

long = 6
array = [random.randint (0, 6) for i in range(long)]

print ("Массив:")
print (*array)

array2 = array[:long // 2:]
array3 = array[long // 2::]

for ii in range(long // 4):
    c = array2[ii]
    array2[ii] = array2[(long // 2) - 1 - ii]
    array2[(long // 2) - 1 - ii] = c
    c = array3[ii]
    array3[ii] = array3[(long // 2)- 1 - ii]
    array3[(long // 2) - 1 - ii] = c
    
array = array2 + array3

print("Результат:")
print(*array)
