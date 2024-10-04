
'''
Практическая работа № 53.	
Линейный поиск в массиве
'''

#Уровень C. Заполните массив случайными числами. Определить, есть ли в нем элементы с одинаковыми значениями, не обязательно стоящие рядом.

import random 
nn = 6

array = []
for i in range(0, nn):
    array.append(random.randint(0,nn))
    
print(*array)

array2 = []
count = 0
for ii in range(0, nn):
    for jj in range(0, nn):
        if ii != jj and array[ii] == array[jj]:
            if count == 0:
                array2.append(array[jj])
                count = 1
            elif count == 1:
                if not (array[ii] in array2):
                    array2.append(array[ii])


if count == 0:
    count = "Нет"
elif count == 1:
    count = "Есть"

    
print(count, *array2)

