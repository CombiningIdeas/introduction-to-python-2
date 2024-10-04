#Практическая 68
#Алгоритмы обработки матриц

'''
Уровень A. Напишите программу, которая заполняет квадратную матрицу случайными числами в интервале [10,99],
а затем записывает нули во все элементы выше главной диагонали. Алгоритм не должен изменяться при изменении размеров матрицы.
'''

import random

N = 4
M = 4
A= []

for i in range(N):
    A.append([0]*M)
    
for ii in range(N):
    for jj in range(M):
        A[ii][jj] = random.randint(20, 80)
        print("{:4d}".format(A[ii][jj]), end = "")
    print()
print()

long = 0
for i in range(N):
    long += 1
    for j in range(long, N):
        A[i][j] = 0
        
for ii in range(N):
    for jj in range(M):
        print("{:4d}".format(A[ii][jj]), end = "")
    print()
