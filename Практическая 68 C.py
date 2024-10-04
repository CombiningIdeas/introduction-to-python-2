#Практическая работа № 68.	
#Алгоритмы обработки матриц

'''
Уровень C. Пиксели рисунка закодированы числами (обозначающими цвет) в виде матрицы, со-держащей N строк и M столбцов.
Выполните поворот рисунка вправо на 90 градусов:
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


count1 = 0
count2 = 0
for ii in range(N):
    for jj in range(M):
        print("{:4d}".format(copyA[count1][count2]), end = "")
        count1 += 1

    print()
    count1 = 0
    count2 += 1
