
#Практическая 42

#Уровень A. Ввести три целых числа, найти максимальное из них.
'''
print("Введите три целых числа:")
a, b, c = map(int, input().split(" "))
maximum = max(a, b, c)
print("Максимальное число", maximum)
'''
#Уровень B. Ввести пять целых чисел, найти максимальное из них.
'''
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
'''

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

