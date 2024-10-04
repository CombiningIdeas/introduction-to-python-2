'''
Практическая работа № 47.	
Процедуры-2 
'''

#Уровень A. Напишите процедуру, которая переставляет три переданные ей числа в порядке воз-растания.
'''
print("Введите три натуральных числа:")
digitA, digitB, digitC = map(int, input().split())

def digitWorks():

    global digitA, digitB, digitC

    num1 = max(digitA, digitB, digitC)
    num3 = min(digitA, digitB, digitC)
    num2 = 0
    
    if num1 == digitA and num3 == digitB:
        num2 = digitC
    elif num1 == digitA and num3 == digitC:
        num2 = digitB
    elif num1 == digitB and num3 == digitC:
        num2 = digitA
    elif num1 == digitB and num3 == digitA:
        num2 = digitC
    elif num1 == digitC and num3 == digitA:
        num2 = digitB
    elif num1 == digitC and num3 == digitB:
        num2 = digitA

    print(num3, num2, num1)

digitWorks()
'''

#Уровень B. Напишите процедуру, которая сокращает дробь вида M/N. Числитель и знаменатель дроби передаются как изменяемые параметры.
#Процедура возвращает пару чисел (кортеж) – числитель и знаменатель сокращённой дроби.



print("Введите числитель и знаменатель дроби:")
digitA, digitB = map(int, input().split())
'''
def worksDigit():

    global digitA, digitB

    if digitA != 0 or digitB != 0:
        while digitA % 2 == 0 and digitB % 2 == 0:
                digitA = digitA // 2
                digitB = digitB // 2

        while digitA % 3 == 0 and digitB % 3 == 0:
                digitA = digitA // 3
                digitB = digitB // 3

        while digitA % 5 == 0 and digitB % 5 == 0:
                digitA = digitA // 5
                digitB = digitB // 5

        while digitA % 7 == 0 and digitB % 7 == 0:
                digitA = digitA // 7
                digitB = digitB // 7

    
    print(f"После сокращения: {digitA}/{digitB}")

worksDigit()
'''

#Уровень C. Напишите процедуру, которая возвращает пару чисел (кортеж):
#наибольший общий делитель и наименьшее общее кратное двух натуральных чисел.
'''

print("Введите два натуральных числа: ")
digitA, digitB = map(int, input().split())

def digitEuclidWorks(num1, num2):

    counter = 0

    while num1 != num2:
        counter += 1
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    #print(num1, num2)- убеждаемся что алгоритм евкилда сработал
    print(f"НОД({digitA},{digitB})={num1}")

    numbers = (num1 + num2 * counter) * 2#Не важно какой num мы умножаем, главное  умножить один раз на число счетка ровно один любой num
    # счетчик написан в кицле while для провреки сколько раз мы прошлись по циклу.
    #Умножаем на 2 потому что при числах 15 и 10 получим 15, а нам надо 30, если же дальше не писать,то при 10 и 20 выдаст 40
    #а тут уже походит 20, поэтому делаем проверки с помощуью if на то какие нам числа попались.
    #важно учесть случайные числа по типу 31 и 52, чтобы алгоритм перемножил такие числа, и НЕЦЕЛОЧИСЛЕННЫМ делением делил простыми числами
    #чтобы максимальное составное число превратилось в максимально малое составное, и пишем условие для этих проверок.
    maximum = max(digitA, digitB)
    
    if digitB % digitA == 0:
        numbers = digitB

    elif digitA % digitB == 0:
        numbers = digitA

    elif numbers > maximum and numbers % digitA == 0 and numbers % digitB == 0:
        numbers = (num1 + num2 * counter) * 2

    else:
        numbers = digitA * digitB
        

        if numbers % 2 == 0 and numbers >= maximum and numbers % digitA == 0 and numbers % digitB == 0 and numbers % 2 >= maximum and \
           (numbers % 2) % digitB == 0 and (numbers % 2) % digitA == 0:
            numbers = numbers % 2
            
        elif numbers % 3 == 0 and numbers >= maximum and numbers % digitA == 0 and numbers % digitB == 0 and numbers % 3 >= maximum and \
             (numbers % 3) % digitB == 0 and (numbers % 3) % digitA == 0:
            numbers = numbers % 3

        elif numbers % 5 == 0 and numbers >= maximum and numbers % digitA == 0 and numbers % digitB == 0 and numbers % 5 >= maximum and \
             (numbers % 5) % digitB == 0 and (numbers % 5) % digitA == 0:
            numbers = numbers % 5

        elif numbers % 7 == 0 and numbers >= maximum and numbers % digitA == 0 and numbers % digitB == 0 and numbers % 7 >= maximum and \
             (numbers % 7) % digitB == 0 and (numbers % 7) % digitA == 0:
            numbers = numbers % 7
        
    print(f"НОК({digitA},{digitB})={numbers}")

digitEuclidWorks(digitA, digitB) 

'''
