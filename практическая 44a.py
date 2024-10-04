'''
i = 1
print ( "9", end="" )
while i < 3:
    print ( i, end="" )
    i += 1
'''
'''
x = int(input())
L = 0
M = 0
while x > 0:
    L = L + 1
    if x % 2 == 1:
        M = M + x % 10
    x = x // 10
print(L, M)
'''
#Ответ: 107
'''
x = int(input())
a = 0
b = 1
while x > 0:
    a = a + 1
    b = b * (x % 8)
    x = x // 8
    print(a, b)


#Ответ: 417
'''

#Уровень A. Ввести натуральное число и найти сумму его цифр.
'''
print("Введите натуральное число:")
digit = int(input())
counter = 0

while digit > 0:
    counter += digit % 10
    digit = digit // 10


print(counter)
'''
#Уровень B. Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры, стоящие рядом. 
'''
print("Введите натуральное число:")
number = int(input())
counter1 = 0
counter2 = 0
x = 0


while number > 0:
    counter1 = number % 10
    counter2 = number // 10 % 10    

    if counter1 == counter2:
        x = 1

    number = number // 10

if x == 1:
    print("Да.")
else:
    print("Нет.")

'''
#Уровень C. Ввести натуральное число и определить, верно ли, что в его записи есть две одинаковые цифры (не обязательно стоящие рядом). 

print("Введите натуральное число:")
num = int(input())

count1 = 0
digit = 0
count2 = 0
x = 0


while num > 0:
    count1 = num % 10
    num = num // 10
    digit = num // 10
    
    while digit > 0:
        count2 = digit % 10

        if count1 == count2:
            x = 1
        digit = digit // 10

if x == 1:
    print("Да.")
else:
    print("Нет.")

    
