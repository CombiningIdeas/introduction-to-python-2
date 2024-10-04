'''
Практическая работа № 48.	
Функции
'''

#Уровень A. Напишите функцию, которая определяет сумму цифр переданного ей числа.
'''
number = int(input("Введите натуральное число:\n"))

def sumDigits(number):
    summ = 0
    while number != 0:
        summ += number % 10
        number = number // 10
    return summ
totalAmount = sumDigits(number)
print(f"Сумма цифр числа {number} равна {totalAmount}.")
'''    
#Уровень B. Напишите функцию, которая находит наибольший общий делитель двух натуральных чисел.
'''
print("Введите два натуральных числа: ")
digitA, digitB = map(int, input().split())

def digitEuclidWorks(num1, num2):


    while num1 != num2:

        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

 
    return num1

numS = digitEuclidWorks(digitA, digitB)
print(f"НОД({digitA},{digitB})={numS}")
'''
#Уровень C. Напишите функцию, которая «переворачивает» число, то есть возвращает число, в котором цифры стоят в обратном порядке.

number = int(input("Введите натуральное число:\n"))

def invertedNumber(numbers):

    #Способ 1, самый короткий через обратный срез строки:
    #Только без преравнивания к int.
    #number1 = numbers[::-1]
    #return number1
        
    #Способ 2:
    #Только без преравнивания к int.
    #numbers = list(numbers)
    #numbers.reverse()
    #number1 = "".join(numbers)#стркоовый метод join преобразует обратно в строку обратный список.  
    #return number1

    #Способ 3:
    
    num2 = 0
    if numbers < 0:
        numbers = abs(numbers)#чтобы отрицательные числа тоже возращались.
        while numbers > 0:
            num1 = numbers % 10
            numbers = numbers // 10
            num2 = num2 * 10
            num2 = num2 + num1
            
        return -num2

    elif numbers >= 0:
        while numbers > 0:
            num1 = numbers % 10
            numbers = numbers // 10
            num2 = num2 * 10
            num2 = num2 + num1
            
        return num2

num = invertedNumber(number)
print(f"После переворота: {num}.")
