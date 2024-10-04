
#практическая 50

#Уровень А

print("Введите два натуральных числа: ")
digitA, digitB = map(int, input().split())

def NOD(num1, num2):
    
    if  num1 == 0 or num2 == 0:
        return num1 + num2
    elif num1 > num2:
        return NOD(num2, num1 % num2)
    else:
        return NOD(num1, num2 % num1)

s = NOD(digitA, digitB)

print(f"НОД({digitA},{digitB}) = {s}.")

