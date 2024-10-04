'''
Практическая работа № 60.	
Двоичный поиск
'''

'''
Уровень B. Заполнить массив случайными числами и отсортировать его. Ввести число X.
Исполь-зуя двоичный поиск, определить, сколько чисел, равных X, находится в массиве.
'''

import random

start = 0
end = 9

oldArray = [random.randint(0, 10) for ii in range(start, end)]

print(f"Массив:")
print(*oldArray)

sortedArray = list(oldArray)

def QuickSort(sortArray, first, last):
    if first >= last:
        return sortedArray
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

QuickSort(sortedArray, start, len(oldArray) - 1)

print("После сортировки:")
print(*sortedArray)

numberSearch = int(input("Введите число Х: \n"))

sorting = 0
counter = 0
def SearchInSortedList(hiddenDigit, sortArray):
    global counter, sorting
    left, right = 0, len(sortArray) - 1
    while sortArray[right] != sortArray[left]:
        
        if hiddenDigit == sortArray[(right + left) // 2]:
            counter += 1
            sorting = sortArray[(right + left) // 2]
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            while (sortArray[(right + left) // 2 + count1] == sortArray[(right + left) // 2 + 1 + count2]):
                if sortArray[(right + left) // 2 + 1 + count2] in sortArray:
                    counter += 1
                    count1 += 1
                    count2 += 1
                
            
            while (sortArray[(right + left) // 2 - count3] == sortArray[(right + left) // 2 - 1 - count4]):
                if sortArray[(right + left) // 2 - 1 - count4] in sortArray:
                    counter += 1
                    count3 += 1
                    count4 += 1
                
        
        if hiddenDigit < sortArray[(right + left) // 2]:
            right = (right + left) // 2
        else:
            left = (right + left) // 2 + 1

    if hiddenDigit == sortArray[(right + left) // 2]:
            counter += 1
            sorting = sortArray[(right + left) // 2]
            
    return sorting
    

if (SearchInSortedList(numberSearch, sortedArray)) == numberSearch:
    print(f"Число {numberSearch} встречается {counter} раз(а).")
else:
    print(f"Число {numberSearch} не встречается.")


