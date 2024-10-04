
#Практическая 42

#Уровень A. Ввести три целых числа, найти максимальное из них.

print("Введите три целых числа:")
a, b, c = map(int, input().split(" "))
maximum = max(a, b, c)
print("Максимальное число", maximum)

#Уровень B. Ввести пять целых чисел, найти максимальное из них.

print("Введите пять целых чисел:")
a, b, c, d, e = map(int, input().split(" "))

numberMax = a

if b > a:
    numberMax = b
if c > b:
    numberMax = c
if d > c:
    numberMax = d
if e > d:
    numberMax = e

print("Максимальное число", numberMax)

#Уровень C. Ввести последовательно возраст Антона, Бориса и Виктора. Определить, кто из них.

'''
Возраст Антона: 15 
Возраст Бориса: 17 
Возраст Виктора: 16 
Ответ: Борис старше всех.
Пример:
Возраст Антона: 17 
Возраст Бориса: 17 
Возраст Виктора: 16 
Ответ: Антон и Борис старше Виктора.
'''


anton = int(input("Возраст Антона: "))
boris = int(input("Возраст Бориса: "))
victor = int(input("Возраст Виктора: "))


if anton > boris:
    if anton > victor:
        print("Ответ: Антон старше всех.")
    elif anton == victor:
        print("Ответ: Антон и Bиктор старше Бориса.")
    else:
        print("Ответ: Bиктор старше всех.")

elif boris > anton:
    if boris > victor:
        print("Ответ: Борис старше всех.")
    elif boris == victor:
        print("Ответ: Борис и Виктор старше Антона.")
    else:
         print("Ответ: Виктор старше всех.")

elif victor > boris:
    if victor > anton:
        print("Ответ: Виктор старше всех.")
    elif victor == anton:
        print("Ответ: Виктор и Антон старше Бориса.")
    else:
        print("Ответ: Антон старше всех.")

elif anton > victor:
    if anton > boris:
        print("Ответ: Антон старше всех.")
    elif anton == boris:
        print("Ответ: Антон и Борис старше Виктора.")
    else:
        print("Ответ: Борис старше всех.")

elif boris > victor:
    if boris > anton:
        print("Ответ: Борис старше всех.")
    elif boris == anton:
        print("Ответ: Борис и Антон старше Виктора.")
    else:
        print("Ответ: Антон старше всех.")
        
elif victor > anton:
    if victor > boris:
        print("Ответ: Виктор старше всех.")
    elif victor == boris:
        print("Ответ: Виктор и Антон старше Бориса.")
    else:
        print("Ответ: Борис старше всех.")

#Дополнение к программе, если у них у всех одинаковый возраст:

elif anton == boris:
    if anton == victor:
        print("У всех одинаковый возраст")

    
