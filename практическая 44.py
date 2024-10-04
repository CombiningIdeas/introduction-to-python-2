#Практическая 44
'''
#Уровень A. Напишите программу, которая получает два целых числа A и B (0 < A < B) и выводит квадраты всех натуральных чисел в интервале от A до B.
print("Введите два целых числа:")

count = 0
indexA, indexB = map(int, input().split())
while (indexB - count) != (indexA - 1):
    print(f"{indexB}*{indexB}={(indexA + count)*(indexA + count)}")
    count += 1
'''
#Уровень B. Напишите программу, которая получает два целых числа и находит их произведение,
#не используя операцию умножения. Учтите, что числа могут быть отрицательными.
'''
print("Введите два числа:")
indexA1, indexB1 = map(int, input().split())

degree = 0
more = indexA1
less = indexB1
count = 0

if abs(indexB1) >= abs(indexA1):
    more = indexB1
    less = indexA1

while (abs(more) - count) > 0:
    degree += less
    count += 1

degree2 = degree
if more < 0:
    degree2 = -degree

if indexA1 < 0 and indexB1 < 0:
    print(f"({indexA1})*({indexB1})={degree2}")
elif indexA1 > 0 and indexB1 > 0:
    print(f"{indexA1}*{indexB1}={degree2}")
elif indexA1 < 0 and indexB1 > 0:
    print(f"({indexA1})*{indexB1}={degree2}")
elif indexA1 > 0 and indexB1 < 0:
    print(f"{indexA1}*({indexB1})={degree2}")
'''
#Уровень C. Ввести натуральное число N и вычислить сумму всех чисел Фибоначчи, меньших N. Предусмотрите защиту от ввода отрицательного числа N.
import sys

print("Введите число N:")
N = int(input())

if N < 0:
    print("Ошибка! Нельзя вводить отрицательные числа.")
    sys.exit()
    
fibonacciN1 = 1
fibonacciN2 = 1
fibSum = fibonacciN1 + fibonacciN2
counter = 0

while N - 2 > counter:
    fibSequence = fibonacciN1 + fibonacciN2
    fibonacciN1 = fibonacciN2
    fibonacciN2 = fibSequence
    fibSum += fibonacciN2
    counter += fibonacciN1
    
print(f"Сумма {fibSum}")
