#Практическая работа № 45аВложенные циклы

#Уровень A. В магазине продается мастика в ящиках по 15 кг, 17 кг, 21 кг.
#Как купить ровно 185 кг мастики, не вскрывая ящики? Сколькими способами можно это сделать?
'''
mac = 0
count = 0

for ii in range(185//15):
    for jj in range(185//17):
        for kk in range(185//21):
            mac = ii * 15 + jj * 17 + kk * 21
            if mac > 185:
                break
            if mac == 185:
                count += 1
                print(f"15*{ii} + 17*{jj} + 21*{kk}=185")
print("способов всего:", count)
'''

#Уровень B. Ввести натуральное число N и вывести все натуральные числа, не превосходящие N и делящиеся на каждую из своих цифр
import sys
digitN = int(input("Введите N\n"))

for index in range(1, digitN):

    oneDigit = digitN % 10
    tenDigit = digitN // 10
    
        
    if index / oneDigit != 0 and index / tenDigit != 0:
        if tenDigit == 0:
            continue

        if oneDigit == 0:
            continue
        print(index)

#Уровень C. Напишите программу, которая получает натуральные числа A и B (A<B) и выводит все простые числа на отрезке [A; B].
'''
print("Введите границы диапазона:")
digitA, digitB = map(int, input().split())

for index in range(digitA, digitB + 1):
    if index == 2 or index == 3 or index == 5 or index == 7:
        print(index)
    elif index % 2 != 0 and index % 3 != 0 and index % 5 != 0 and index % 7 != 0:
        print(index)
'''

#Уровень D. Напишите программу, которая получает натуральные числа A и B (A<B) и выводит все на отрезке [A; B], у которых ровно 4 разных делителя.
'''
print("Введите границы диапазона:")
digitA, digitB = map(int, input().split())

counter = 0
numbers = 1

for index in range(digitA, digitB + 1):
    if index % numbers == 0:
        counter += 1
    numbers += 1
'''
