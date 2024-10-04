
#Пример работы с матрицами

def printMatrix(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            print("{:4d}".format(A[i][j]), end = "")
        print()
    
A = [[-1, 0, 1],
     [-1, 0, 1],
     [0, 1, -1]]

printMatrix(A)
