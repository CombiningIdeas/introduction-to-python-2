
#from random import random
#from random import *
import random

N = 100000
M = 0

#random.rabdom() - ������� ��������� ����� � ��������� �� [0;1), ������
#������� 0 �� �� ������� 1. �� ������ ����� ������� ������������ ���������� 
#� ������� �������������� ��������

for i in range(N):
    x = random.random()
    y = random.random()
    if x*x+y*y <= 1:
        M += 1
print("PI =", 4*M/N)


#from random import random, randint
import random

L = 480#��� � ������� ������� ����, � ����� 8 �����
Pmax = 4#������������ ����� �������� �� 1 ������
Tmin = 1#����������� ����� ������������
Tmax = 1#����������� ����� ������������
M = 15#���������� ����� ��������
T = 0#������� � ����� ������ ���
count = 0#������� ������ �����
# ����� ��� ������ ����� �������� K

for i in range(L):
    P = random.randint(0, Pmax)
    T = Tmin + random.random() * (Tmax-Tmin)
    R = round(K/T)
    #round() - ���������� �����, ���� ������� ����� ����� ������ 0.5 �� ����������� ����
    N += P - R
    if N < 0:
        N = 0
        dT = N / K * T
    if dT > M:
        count += 1

