'''
Практическая работа № 63.	
Преобразования «строка-число»
Уровень C. Напишите программу, которая вычисляет выражение, состоящее из трех чисел и двух знаков (допускаются знаки «+», «–», «*» и «/»).
Выражение вводится как символьная строка, все числа целые. Операция «/» выполняется как целочисленное деление (div).
'''

s = str(input("Введите выражение: \n"))
digit1 = 0
digit2 = 0
digit3 = 0
strVariable = ""
arrayDigit = []
arraySymbol = []

for ii in s:
    while ii != "*" and ii != "/" and ii != "-" and ii != "+":
        strVariable += str(ii)
        variable = int(strVariable)
        break

    if ii == "*":
        arrayDigit.append(int(variable))
        arrayDigit.append("*")
        strVariable = ""
    
    elif ii == "/":
        arrayDigit.append(int(variable))
        arraySymbol.append("//")
        strVariable = ""
    
    elif ii == "+":
        arrayDigit.append(int(variable))
        arrayDigit.append("+")
        strVariable = ""

    elif ii == "-":
        arrayDigit.append(int(variable))
        arrayDigit.append("-")
        strVariable = ""
        

arrayDigit.append(int(variable))
print(arrayDigit)

specialDigit = 0
for ii in range(len(arrayDigit)- 1):
    if arrayDigit[ii] == "*" and arrayDigit[ii] == "/" and arrayDigit[ii] == "+" and arrayDigit[ii] == "-":
        if ii == "*":
            specialDigit += arrayDigit[ii-1] * arrayDigit[ii+1]
            print(specialDigit)
        elif ii == "/":
            specialDigit += arrayDigit[ii-1] // arrayDigit[ii+1]
            print(specialDigit)
        elif ii == "+":
            specialDigit += arrayDigit[ii-1] + arrayDigit[ii+1]
            print(specialDigit)
        elif ii == "-":
            specialDigit += arrayDigit[ii-1] - arrayDigit[ii+1]
            print(specialDigit)
        print(specialDigit)
    print(specialDigit)

    
print(specialDigit)





