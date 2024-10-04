## Черновик

## Контрольная работа №4 «Массивы»

#'''
#Задание 3. Заполните массиве случайными числами в интервале [0, 1000] и выведите номера трех различных максимальных элементов.
#Разрешается только один проход по массиву.
#'''


#import random

#array = [random.randint(0, 1000) for ii in range(0, 10)]

#print("Массив:")
#print(*array)

#numberMax1 = 0
#numberMax2 = 0
#numberMax3 = 0
#commonNumberMax1 = 0
#commonNumberMax2 = 0
#commonNumberMax3 = 0

#for ii in range(len(array) - 1):
#    if commonNumberMax1 < array[ii]:
#        if commonNumberMax3 < array[ii]:
#            if commonNumberMax3 != commonNumberMax2 and commonNumberMax3 != commonNumberMax1:
#                commonNumberMax3 = array[ii]
#                numberMax3 = commonNumberMax3
            
#        if commonNumberMax2 < array[ii]:
#            if commonNumberMax2 != commonNumberMax1:
#                commonNumberMax2 = array[ii]
#                numberMax2 = commonNumberMax1

        
#        commonNumberMax1 = array[ii]
#        numberMax1 = commonNumberMax1
    
#'''
#    if array[ii] < array[ii+1]:
#        if commonNumberMax3 < array[ii+1]:
#            if commonNumberMax2 != array[ii+1]:
#                commonNumberMax3 = array[ii+1]
#                numberMax3 = commonNumberMax3
#    else:
#        if commonNumberMax3 < array[ii]:
#            if commonNumberMax3 != commonNumberMax2:
#                commonNumberMax3 = array[ii+1]
#                numberMax3 = commonNumberMax3
        
#    if array[ii] < array[ii+1]:
#        if commonNumberMax2 < array[ii+1]:
#            if commonNumberMax1 != array[ii+1]:
#                commonNumberMax2 = array[ii+1]
#                numberMax2 = commonNumberMax2
#    else:
#        if commonNumberMax2 < array[ii]:
#            if commonNumberMax2 != commonNumberMax1:
#                commonNumberMax2 = array[ii+1]
#                numberMax2 = commonNumberMax2
        
#    if array[ii] < array[ii+1]:
#        if commonNumberMax1 < array[ii+1]:
#            commonNumberMax1 = array[ii+1]
#            numberMax1 = commonNumberMax1
#    else:
#        if commonNumberMax1 < array[ii]:
#            commonNumberMax1 = array[ii]
#            numberMax1 = commonNumberMax1
#'''
#print(f"Максимальное значение №1: {numberMax1}; Максимальное значение №2: {numberMax2}; Максимальное значение №3: {numberMax3}.")




#print("\nТаблица умножения:")
#for ii in range(1, 11):
#    for jj in range(1, 11):
#        print(f"число {ii}: {ii} * {jj} = " ,ii * jj, "; ", sep="")
#    print('\n')


#counter = 0
#for i in range(0, 3):
#    num = int(input())
#    if num > 10:
#        counter += 1

#print('Было введено',counter,'чисел, больших 10.')



#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (((x <= y) == (w <= x)) and (z <= w)):
#                    print(x, y, z, w)

#print("Ответ: ", y, z, w, x)




#for ii in range(390):
#    if ((ii % 3 == 0) and (ii % 10 == 4)):
#        print(ii)



# for ii in range(100, 1000):
#     S = int(str(ii)[0]) + int(str(ii)[1]) + int(str(ii)[2])
    
#     if (ii * S) == 1105:
#         print(ii)
    


# length = 0
# num_max = 0
# s = []
# for ii in open('numbers.txt'):
#     s.append(int(ii))
#     length += 1
#     if length == 6:
#         num_max = max(s[0] + s[5], num_max)
#         s.pop(0)
#         length -= 1

# print(num_max)





# length = 0
# num_max = 0
# s = []
# for ii in open('numbers.txt'):
#     s.append(int(ii))
#     length += 1
#     if length == 5:
#         num_max = max(s[0] + s[4], s[0] + s[3], s[0] + s[2], s[0] + s[1], num_max)
#         s.pop(0)
#         length -= 1

# print(num_max)



# num_max = 0
# sum_max = 0
# s = []
# for ii in open('numbers.txt'):
#     s.append(int(ii))
#     if len(s) > 6:
#         num_max = max(s.pop(0), num_max)
#         sum_max = max(num_max + s[-1], sum_max)

# print(sum_max)


# for ii in range(-1000, 1000):
#     if (not(ii <= 9)) and (not(ii >= 17)) and (ii % 2 == 0):
#         print(ii)


# a = int(input())
# kc = 0
# k = 0
# while a > 0:
#     c = a % 8
#     if c % 2 == 0:
#         kc = kc + 1
#     k = k + 1
#     a = a//8
# print(kc)
# if (kc == k):
#     print("да")
# else:
#     print("нет")


# n = int(input())
# S = 5
# i = 20
# if (i <= n):
#     S = S + n * 2 
#     i = n - 2
#     print(S)
#     print(i)
# else:
#     S = S - n / 2 
#     i = n + 2
#     print(S)
#     print(i)
    
# counter = 0
# from itertools import permutations
# for ii in permutations("paksin", 4):
#     a = (''.join(ii))[:3:]
#     print(''.join(ii))
#     if (a == "ksn"):
#         counter += 1
    
# print(counter)



# s = int(input())
# t = int(input())
# A = int(input())

# if (s > A) or (t > 12):
#     print("YES")
# else:
#     print("NO")



# a = 6
# b = 26
# b = a % b + 4
# c = a % b + 1
# print(c)

# a = 10
# b = 5
# if (a > 1) and (a < b):
#     a = -5
# if (a > 1) and (a == b):
#     a += 5
    
# print(a)

# a = 17
# b = 3
# b = a//b

# c = a % (b+1)
# print(c)


# a = 10
# b = 5
# if (a < 1) (a > b):
#     a = -5
# else:
#     a += 5
# print(a)

# a = 13
# if (a > 5):
#     a = 12
# print(a)


# a = 10
# b = 3
# if a > b:
#     b += 12
# else:
#     a -= 8
# if a > b:
#     a += 12
# else:
#     a -= 8
# print(a)

# a = 13
# if (a < 16):
#     a += 7
# else:
#     a -= 12
# print(a)


# a = 25
# b = 7
# b = a // b + b
# c = a % b + a
# print(c)


# a = 7
# if a > 5:
#     a += 12
# else:
#     a -= 7
# if a < 5:
#     a += 12
# else:
#     a -= 7
# print(a)


# a = 14
# if a < 15:
#     a += 12
# else:
#     a -= 7
# if a < 13:
#     a += 12
# else:
#     a -= 7
# print(a)

# a = 13
# b = 7
# if a > 5 and a < b:
#     a -= 5
# print(a)


# a = 33
# b = 8
# b = a % b
# c = a // (b+1)
# print(c)

# a = 23
# b = 4
# b = a // b
# c = a // b
# print(c)

# a = 13
# b = 5
# if a > 1 or a < b:
#     a -= 5
# if a > 1 and a == b:
#     a -= 5
# print(a)

# a = 10 
# b = 5
# if a > 1 and a < b:
#     a -=7
# else:
#     a += 7
# print(a)

# a = int("53", 6)
# #33
# print(33-5)






# counter = 0
# def fun(n, max_num):
#     global counter
#     if n == max_num:
#         counter += 1
#         return 0
#     if n > max_num or "14" in str(n):
#         return 0
#     return fun(n+1, max_num) + fun(n+2, max_num) +  fun(n*3, max_num) 

# fun(2, 16)
# print(counter)
        

# counter = int(input())
# a = str(counter)
# print(a[:1:])
# print(a[-1::])


# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))

# if (num1 % num2 == 0):
#     print(f"Число {num1} делитья без остатка на число {num2}")
# else:
#     print(f"Число {num1} не делитья без остатка на число {num2}")



# def convert(x):
#     notation = 2
#     s = ''
#     while x > 0:
#         s = str(x % notation) + s
#         x = x // notation

#     return s

# number = 555
# print(convert(number))






# n, k = map(int, input().split())

# fucktorial_N = 1
# for ii in range(1, n+1):
#     fucktorial_N *= ii
    
# fucktorial_K = 1
# for ii in range(1, k+1):
#     fucktorial_K *= ii
    

# fucktorial_N_K = 1
# for ii in range(1, (n-k)+1):
#     fucktorial_N_K *= ii
    

# C = int(fucktorial_N / (fucktorial_K * fucktorial_N_K))
# print(C)



# new_number = ""
# for ii in range(1000, 9999+1):
#     digit1 = int(str(ii)[0]) + int(str(ii)[1])
#     digit2 = int(str(ii)[2]) + int(str(ii)[3])

#     if (digit1 > digit2):
#         new_number = str(digit2) + str(digit1)
#     else:
#         new_number = str(digit1) + str(digit2)
        

#     if (new_number == "1515"):
#         print(ii, new_number)
        

#Для четырех значных чисел ответ: 9696





# def F(n):
#     print(n)
#     if (n< 5):
#         F (n + 1); F (n + 2)        


# print(F(1))



# from itertools import * 

# letters = ['П', 'Е', 'С', 'Н', 'Я']
# valid_words = 0

# # Генерация всех возможных комбинаций длиной 6
# for word in product(letters, repeat=6):
#     word_str = ''.join(word)
    
#     # Проверка, что слово содержит хотя бы одну букву "Я"
#     if 'Я' in word_str:
#         # Проверка, что слово не начинается с гласной буквы
#         if (word_str[0] not in ['Е', 'Я']):
#             valid_words += 1
            

# print(valid_words)
# #Ответ: 6303






# def count_divisors(n):
#     """Функция для подсчета количества делителей числа n"""
#     count = 0
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             count += 1
#             if i != n // i:  # Если i не является квадратным корнем n
#                 count += 1
#     return count

# def find_numbers_with_k_divisors(a, b, k):
#     """Функция для поиска чисел в диапазоне [a, b] с ровно k различными делителями"""
#     result = []
#     for number in range(a, b + 1):
#         if count_divisors(number) == k:
#             result.append(number)
#     return result

# # Ввод значений
# a = int(input("Введите значение a: "))
# b = int(input("Введите значение b: "))
# k = int(input("Введите значение k: "))

# # Поиск чисел с ровно k делителями
# numbers_with_k_divisors = find_numbers_with_k_divisors(a, b, k)

# # Вывод результата
# # for idx, number in enumerate(numbers_with_k_divisors, start=1):
# #     print(f"{idx}. {number}")


# for ii in range(0, len(numbers_with_k_divisors)):
#     print(ii+1, '. ', numbers_with_k_divisors[ii], sep = '')
    






# def find_longest_substring(input_str):
#     # Определяем допустимые символы
#     valid_chars = {'I', 'T', 'Z'}
    
#     # Переменные для хранения текущей подцепочки и самой длинной подцепочки
#     max_substring = ""
#     current_substring = ""
    
#     for char in input_str:
#         if char in valid_chars:
#             current_substring += char
#             if len(current_substring) > len(max_substring):
#                 max_substring = current_substring
#         else:
#             current_substring = ""
    
#     return max_substring

# # Чтение строки из файла Input.txt
# with open('Input.txt', 'r') as file:
#     input_string = file.readline().strip()

# # Поиск самой длинной подцепочки
# longest_substring = find_longest_substring(input_string)

# # Вывод результата
# print("Самая длинная подцепочка:", longest_substring)








# def find_longest_substring(input_str):
#     # Определяем допустимые символы
#     valid_chars = {'I', 'T', 'Z'}
    
#     # Переменные для хранения текущей подцепочки и самой длинной подцепочки
#     max_substring = ""
#     current_substring = ""
    
#     for char in input_str:
#         if char in valid_chars:
#             current_substring += char
#             if len(current_substring) > len(max_substring):
#                 max_substring = current_substring
#         else:
#             current_substring = ""
    
#     return max_substring

# # Чтение строки из файла Input.txt
# file = open('Input.txt', 'r')
# input_string = file.readline().strip()
# file.close()

# # Поиск самой длинной подцепочки
# longest_substring = find_longest_substring(input_string)

# # Вывод результата
# print("Самая длинная подцепочка:", longest_substring)






def count_adjacent_pairs_divisible_by_21(sequence):
    count = 0
    for ii in range(0, len(sequence) - 1):
        if (sequence[ii] * sequence[ii + 1]) % 21 == 0:
            count += 1
    return count

# Ввод последовательности чисел с клавиатуры
N = int(input("Введите количество чисел в последовательности: "))
sequence = []

print("Введите числа последовательности:")
for _ in range(N):
    sequence.append(int(input()))

# Подсчет и вывод количества пар
result = count_adjacent_pairs_divisible_by_21(sequence)
print("Количество пар, произведение которых кратно 21:", result)
