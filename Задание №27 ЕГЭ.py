
#Номер 27(А) КИМ № 25032504
from functools import *
from sys import *

setrecursionlimit(99999999)
@lru_cache(maxsize = 100000)
def f():
    fin1 = open("27-A_11468.txt")
    fin2 = open("27-B_11468.txt")

    arrayA = fin1.read().split()
    arrayB = fin2.read().split()

    tmp_min = 10**20
    tmpA = 0
    tmpB = 0
    #print(*arrayA)
    for ii in range(0, len(arrayB) - 1):
        for jj in range(0, len(arrayA) - 1):
            if (abs((int(arrayB[ii]) - int(arrayA[jj]))) < tmp_min):
                tmp_min = abs(int(arrayB[ii]) - int(arrayA[jj]))
                tmpA = int(arrayA[jj])
                tmpB = int(arrayB[jj])
            
    print(tmp_min, tmpA, tmpB)
    
print(f())