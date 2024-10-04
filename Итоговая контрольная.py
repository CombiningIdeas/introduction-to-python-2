'''
sumNumbers = 8**1023 + 2**1024 - 3

digit = 0
while sumNumbers > 0:
    digit += sumNumbers % 2
    sumNumbers = sumNumbers // 2

print(digit)
'''

'''
8)Рассматривается множество целых чисел, принадлежащих отрезку [3542; 15876],
которые делятся на 2 или на 9 и не делятся на 11, 13, 17 и 23.
Напишите программу, которая находит количество таких чисел и максимальное из них
и в ответе выводит два числа через пробел: сначала количество, затем максимальное число.
'''

numArray = []
for ii in range(3542, 15876 + 1):
    if ((ii % 2 == 0 or ii % 9 == 0) and (ii % 11 != 0) \
        and (ii % 13 != 0) and (ii % 17 != 0) \
        and (ii % 23 != 0)):
        numArray.append(ii)
        
lenght = len(numArray)
maxNum = max(numArray)

print(lenght, maxNum)

    
