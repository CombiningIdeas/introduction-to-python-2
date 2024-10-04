import random

start = 0
end = 15

oldArray = [random.randint(0, 100) for ii in range(start, end)]

print(f"Массив до сортировки: {oldArray}")

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

print(f"Массив после сортировки: {sortedArray}")

def SearchInSortedList(hiddenDigit, sortArray):
    left, right = 0, len(sortArray) - 1
    while right != left:
        if sortArray[(right + left) // 2] < hiddenDigit:
            left = (right + left) // 2 + 1
        else:
            right = (right + left) // 2

    if sortArray[left] == hiddenDigit:
        return left
    else:
        return -1
    
#Чтобы определить есть ли число равное X его нужно загадать сначало:
#Тут число в диапазоне от -10 до 27 ключительно
numberSearch = random.randint(0, 100)

sortingResult = SearchInSortedList(numberSearch, sortedArray)

print(f"Загаданное число: {numberSearch}")

if (sortingResult == -1):
    print("Число не найдено в массиве поэтому получает индекс: -1")

print(f"Загаданное число имеет индекс в массиве: {sortingResult}")












