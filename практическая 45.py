'''
Практическая работа № 45.	
Циклы по переменной
'''

#Уровень A. Найдите все пятизначные числа, которые при делении на 133 дают в остатке 125, а при делении на 134 дают в остатке 111.
'''
counter = 0
for index in range(10000, 99999 + 1):
    if index % 133 == 125 and index % 124 == 111:
        counter += 1

print(counter)
'''
#Уровень B. Натуральное число называется числом Армстронга, если сумма цифр числа,
#возве-денных в N-ную степень (где N – количество цифр в числе) равна самому числу. Например, 
#153 = 13 + 53 + 33. Найдите все трёхзначные Армстронга.
'''

for index in range(100, 999 + 1):

    digitHundred = index // 100
    digitTen = index // 10 % 10
    digitOne = index % 10

    number1 = digitHundred**3
    number2 = digitTen**3
    number3 = digitOne**3

    digitMain = number1 + number2 + number3
    
    if index == digitMain:
        print(index)
'''    
#Уровень C. Натуральное число называется автоморфным, если оно равно последним цифрам своего квадрата.
#Например, 252 = 625. Напишите программу, которая получает натуральное число N и выводит на экран все автоморфные числа, не превосходящие N.
#Мой спосб, он универсальный, но более сложный.
'''
print("Введите N:")

nDigit = int(input())

point = 10
for index in range(1, nDigit+1):
    if index >= point:
        point *= 10
    check = 2 * index - 1
    if (check * check - 1) % (4 * point) == 0:
        print(f"{index}*{index} = {index*index}")

'''

#Второй спосб
'''
N = int(input("Введите N:\n"))
for i in raange(1, N + 1):
    x = i
    x2 = i**2
    while x > 0:
        if x%10 != x2%10: break
        x = x // 10
        x2 = x2 // 10
    if x == 0: print(f"{i}*{i}=={i*i}")
'''

#Третий способ
'''
N = int(input("Введите N:\n"))
for x in range(1, N + 1):
    n = x
    k = 0
    while n > 0:
        k += 1
        n //= 10
    of x**2 % 10**k == x: print("%d*%d=%d" % (x, x, x**2))
'''

#Четвертый способ, тоже универсальный, более простой для понимания.

N = int(input("Введите N:\n"))
a = 10
for x in range(1, N + 1):
    if x**2 % a == x: print("%d*%d=%d" % (x, x, x**2))
    if x >=a: a*=10
