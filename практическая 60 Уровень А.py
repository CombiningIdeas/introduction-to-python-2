'''
Практическая работа № 60.	
Двоичный поиск
'''

'''
Уровень A. Заполнить массив случайными числами и отсортировать его.
Ввести число X. Исполь-зуя двоичный поиск, определить, есть ли в массиве число, равное X.
Подсчитать количество сравнений.
'''

import random

start = 0
end = 9

oldArray = [random.randint(0, 100) for ii in range(start, end)]

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

counter = 0
def SearchInSortedList(hiddenDigit, sortArray):
    global counter
    left, right = 0, len(sortArray) - 1
    while sortArray[right] != sortArray[left]:
        if hiddenDigit == sortArray[(right + left) // 2]:
            break
        elif hiddenDigit < sortArray[(right + left) // 2]:
            right = (right + left) // 2 
            counter += 1
            
        else:
            left = (right + left) // 2 + 1
            counter += 1

    return sortArray[(right + left) // 2]
    


if ((SearchInSortedList(numberSearch, sortedArray)) == numberSearch):
    print(f"Число {numberSearch} найдено.")
    print(f"Количество сравнений: {counter}")
else:
    print(f"Число {numberSearch} НЕ найдено.")






