#Практическая работа № 67. Матрицы

'''
Уровень B. Пиксели рисунка закодированы числами от 0 до 255 (обозначающими яркость пиксе-лей) в виде матрицы,
содержащей N строк и M столбцов. Нужно преобразовать рисунок в черно-белый по следующему алгоритму:
вычислить среднюю яркость пикселей по всему рисунку
все пиксели, яркость которых меньше средней, сделать черными (записать код 0), а остальные – белыми (код 255)
'''


import random

N = 4
M = 4
A = []

for kk in range(N):
    A.append([0]*M)

sumLightPin = 0
longPin = 0


print("Матрица А: ")

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(0, 255)
        sumLightPin += A[i][j]
        longPin += 1
        print("{:4d}".format(A[i][j]), end = "")
        
    print()    


averageNumber = sumLightPin / longPin
print(f"Средняя яркость : {averageNumber}")
print("Результат: ")

for i in range(N):
    for j in range(M):
        if A[i][j] <= averageNumber:
            A[i][j] = 0
        elif A[i][j] > averageNumber:
            A[i][j] = 255

        print("{:4d}".format(A[i][j]), end = "")
        
    print()

