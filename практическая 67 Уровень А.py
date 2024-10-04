#Практическая работа № 67. Матрицы
'''
Уровень A. Напишите программу, которая заполняет квадратную матрицу случайными числами в интервале [10,99],
и находит максимальный и минимальный элементы в матрице и их индексы.
'''
import random

N = 4
M = 4
A = []

for kk in range(N):
    A.append([0]*M)

indexMaxI = 0
indexMaxJ = 0
maxNumber = A[0][0]

indexMinI = 0
indexMinJ = 0
minNumber = 100

print("Матрица А: ")

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(10, 99)
        
        if A[i][j] > maxNumber:
            maxNumber = A[i][j]
            indexMaxI = i
            indexMaxJ = j
            
        if minNumber > A[i][j]:
            minNumber = A[i][j]
            indexMinI = i
            indexMinJ = j
            
        print("{:4d}".format(A[i][j]), end = "")
        
    print()    



print(f"Максимальный элемент A[{indexMaxI}, {indexMaxJ}] = {maxNumber}")
print(f"Минимальный элемент A[{indexMinI}, {indexMinJ}] = {minNumber}")
