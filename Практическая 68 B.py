#Практическая 68
#Алгоритмы обработки матриц

'''
Уровень B. Пиксели рисунка закодированы числами (обозначающими цвет) в виде матрицы,
со-держащей N строк и M столбцов. Выполните отражение рисунка сверху вниз:
'''

import random

N = 3
M = 3
A= []

for i in range(N):
    A.append([0]*M)
    
for ii in range(N):
    for jj in range(M):
        A[ii][jj] = random.randint(20, 80)
        print("{:4d}".format(A[ii][jj]), end = "")
    print()
print()

copyA = []
for i in range(N-1, -1, -1):
    copyA.append(A[i])


for ii in range(N):
    for jj in range(M):
        print("{:4d}".format(copyA[ii][jj]), end = "")
    print()
print()
