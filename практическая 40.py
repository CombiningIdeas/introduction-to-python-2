#Практическая 40
'''
#Уровень А
print("Введите три целых числа: ")
a, b, c = map(int, input().split())

print(a, "+", b,"+", c, "=", a + b + c, sep = "")
print(a, "*", b,"*", c, "=", a * b * c, sep = "")
print("({:d}+{:d}+{:d})/3={:5.3f} ".format(a, b, c, (a + b + c) / 3))

#Уровень В

import math

print("Введите координаты точки A:")
coordinateA_X, coordinateA_Y = map(float, input().split())
print("Введите координаты точки B:")
coordinateB_X, coordinateB_Y = map(float, input().split())

long_coordinateA = coordinateA_X - coordinateB_X
long_coordinateB = coordinateA_Y - coordinateB_Y

long_vector = math.sqrt(long_coordinateA**2 + long_coordinateB**2)

print("Длина отрезка AB =", long_vector)

#Уровень С

#Первый способ

import random
random_number = random.randint(100, 999)

hundreds = random_number // 100
dozens = random_number // 10 % 10
units = random_number % 10 


print(f"Получено число {random_number}.")
print(f"Его цифры {hundreds}, {dozens}, {units}.")

'''
#второй способ, что то пошло не поплану и я не смогу в конце вместо запятой после последнего числа придумать как написать точку.
#Это я так, просто делал для себя, хотел через цикл и прохождению по числу отделить автоматически
#Чтобы в дальнейшем можно было не только трех значные числа писать, а любые и все работало.


from random import randint
random_number = str(randint(100, 999))
print("Получено число ", random_number, ".", sep = "")
print("Его цифры", end = " ")
g = ","
for i in range(len(random_number)):
    if i == len(random_number)-1:
        print(str(i) +',',  end = "")
    else:
        print(str(i) +'.',  end = "")

    




