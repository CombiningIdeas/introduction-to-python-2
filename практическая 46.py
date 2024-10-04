'''
Практическая работа № 46.	
Процедуры
'''

#Уровень A. 7.	Напишите процедуру, которая принимает параметр – натуральное число N – и выводит на экран линию из N символов '–'.
'''
digit = int(input("Введите N:\n"))

def digitWorks(variables):
    value = "-"
    print(value * variables)
    
digitWorks(digit)
'''

#Уровень B. Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, начиная с первой.
'''
digit = input("Введите натуральное число: \n")

def worksDigit(variables):
    
    for index in variables:
        print(index)
    
worksDigit(digit)

'''

'''
#УровеньВ второй вариант вариант.
# Процедура выводит на экран в столбик все цифры переданного ей числа,
# начиная с первой
def printNum(n):
    n1 = 0
    while n > 0:			# выполняем реверс числа
        n1 = n1 * 10 + n % 10
        n = n // 10
    while n1 > 0:		# выводим новое число по цифрам на экран
        print(n1 % 10)
        n1 = n1 // 10
        
print("Введите натуральное число: ")
printNum(int(input()))
'''

#Уровень C. Напишите процедуру, которая выводит на экран запись переданного ей числа в рим-ской системе счисления.
'''
digit = input("Введите натуральное число:\n")

def worksToDay(var):

    counter = 0
    for jj in var:
        counter += 1


    
    index1 = var.replace("1", "I")
    index2 = index1.replace("2", "II")
    index3 = index2.replace("3", "III")
    index4 = index3.replace("4", "IV")
    index5 = index4.replace("5", "V")
    index6 = index5.replace("6", "VI")
    index7 = index6.replace("7", "VII")
    index8 = index7.replace("8", "VIII")
    index9 = index8.replace("9", "IX")
    index10 = index9.replace("10", "X")
    index11 = index10.replace("11", "XI")
    index12 = index11.replace("12", "XII")
    index13 = index12.replace("13", "XIII")
    index14 = index13.replace("14", "XIV")
    index15 = index14.replace("15", "XV")
    index16 = index15.replace("16", "XVI")
    index17 = index16.replace("17", "XVII")
    index18 = index17.replace("18", "XVIII")
    index19 = index18.replace("19", "XIX")
    index20 = index19.replace("20", "XX")
    index21 = index20.replace("30", "XXX")
    index22 = index21.replace("40", "XL")
    index23 = index22.replace("50", "L")
    index24 = index23.replace("60", "LX")
    index25 = index24.replace("70", "LXX")
    index26 = index25.replace("80", "LXXX")
    index27 = index26.replace("90", "XC")
    index28 = index27.replace("100", "C")
    index29 = index28.replace("200", "CC")
    index30 = index29.replace("300", "CCC")
    index31 = index30.replace("400", "CD")
    index32 = index31.replace("500", "D")
    index33 = index32.replace("600", "DC")
    index34 = index33.replace("700", "DCC")
    index35 = index34.replace("800", "DCCC")
    index36 = index35.replace("900", "CM")
    index37 = index36.replace("1000", "M")
    index38 = index37.replace("2000", "MM")
    index39 = index38.replace("3000", "MMM")
    index40 = index39.replace("3999", "MMMCMXCIX")
    index41 = index40.replace("4000", "MV")
    index42 = index41.replace("500", "V")
    index43 = index42.replace("6000", "VM")
    index44 = index43.replace("7000", "VMM")
    index45 = index44.replace("8000", "VMMM")
    index46 = index45.replace("9000", "MX")
    index47 = index46.replace("1000", "X")
    
    print(index47)

worksToDay(digit)
'''


#УровеньС
#Процедура выводит на экран запись переданного ей числа в римской системе счисления
def printRim(n):
    k = n // 1000
    print('M'*k, end='')
    n = n % 1000

    k = n // 100
    if k == 9:
        print('CM', end='')
    elif k >= 5:
        print('D', 'C'*(k-5), sep='', end='')
    elif k == 4:
        print('CD', end='')
    else:
        print('C'*k, end='')
    n = n - 100 * k

    k = n // 10
    if k == 9:
        print('XC', end='')
    elif k >= 5:
        print('L', 'X' * (k - 5), sep='', end='')
    elif k == 4:
        print('XL', end='')
    else:
        print('X' * k, end='')
    n = n - 10 * k

    if n == 9:
        print('IX', end='')
    elif n >= 5:
        print('V', 'I' * (n - 5), sep='', end='')
    elif n == 4:
        print('IV', end='')
    else:
        print('I' * n, end='')

print("Введите натуральное число:")
printRim(int(input()))
