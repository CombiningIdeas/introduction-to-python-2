# Контрольная работа №4 «Массивы»

'''
Задание 1. Введите  массив из 5 элементов с клавиатуры и найдите количество элементов,
запись которых в двоичной системе - палиндром(например, 10101 = 21).
'''

array1, array2, array3, array4, array5  = map(int, input("Введите массив из 5 элементов(через пробел): \n").split())

array = [array1, array2, array3, array4, array5]

print("Массив:")
print(*array)

counter = 0
def palindrome(array):
    global counter
    for ii in range(len(array)):
        digit1 = bin(array[ii])[2:]
        digit1 = int(digit1)

        digit2 = 0
        reversed_digit = 0
        specialDgit = digit1
        
        while specialDgit != 0:
            digit2 = specialDgit % 10
            reversed_digit = reversed_digit * 10 + digit2
            specialDgit //= 10
            
        if digit1 == reversed_digit:
            counter += 1

    return counter
    
print("Количество полиндромов:",palindrome(array))

