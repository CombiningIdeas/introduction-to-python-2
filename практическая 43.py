'''
Практическая работа № 43.	
Сложные условия
'''
#Уровень А
'''
print("Введите три числа:")
index1, index2, index3 = map(int, input().split())

if index1 == index2 and index1 == index3 and index2 == index3:
    print("Все числа одинаковые.")

elif index1 == index2 or index1 == index3 or index2 == index3:
    print("Два числа одинаковые.")

else:
    print("Нет одинаковых чисел.")

#Уровеь В

import sys

print("Введите номер месяца:")

season = int(input())

if season < 1 or season > 12:
    print("Неверный номер месяца.")
    sys.exit()

if season == 1 or season == 2 or season == 12:
    print("Зима.")

elif season == 3 or season == 4 or season == 5:
    print("Весна.")

elif season == 6 or season == 7 or season == 8:
    print("Лето.")

elif season == 9 or season == 10 or season == 11:
    print("Осень.")

#Можно было в конце просто else написать(ведь другие исходы событий уже известны), но мой перфекционизм не позволил мне это сделать.
'''
#Уровень С
import sys#Я коментировал программу B, чтобы быстрее проверить, поэтому опять импортировал эту библиотеку.
age = int(input("Введите возраст: "))

if age > 120 or age < 0:
    print("Неверный возраст")
    sys.exit()

remains = age % 10

if remains == 0 or remains == 5 or remains == 6 or remains == 7 or remains == 8 or remains == 9:
    print(f"Вам {age} лет.")

#Это исключени, их я написал отдельно:  
elif age == 11 or age == 12 or age == 13 or age == 14 \
   or age == 111 or age == 112 or age == 113 or age == 114:
    print(f"Вам {age} лет.")

elif remains == 1:
    print(f"Вам {age} год.")

elif remains == 2 or remains == 3 or remains == 4:
    print(f"Вам {age} года.")
