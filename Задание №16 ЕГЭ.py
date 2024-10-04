# #Задание №16 ЕГЭ(1)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 0:
#         return (n + f(n - 3))
#     if n % 3 > 0:
#         return (n + f(n - (n % 3)))

# print(f(22))



# #Задание №16 ЕГЭ(2)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n//2)
#     if n % 2 != 0:
#         return (1 + f(n - 1))

# for ii in range(1, 10000):
#     if f(ii) == 12:
#         print(ii)
        

# #ответ 4095


# #Задание №16 ЕГЭ(3)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 0:
#         return f(n//3)
#     if n % 3 > 0:
#         return (n % 3 + f(n - (n % 3)))

# for ii in range(1, 1000):
#     if f(ii) == 11:
#         print(ii)
        

# #ответ 485




# #Задание №16 ЕГЭ(4)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n//2)
#     if n % 2 != 0:
#         return (1 + f(n - 1))

# count = 0
# for ii in range(1, 501):
#     if f(ii) == 3:
#         count += 1
        
# print(count)
# #ответ 84





# def f(n):
#     if n <= 1:
#         return 0.5
#     else:
#         return (n+1) * f(n-1)


# print(f(139)/f(137))#разница 278 = 19460-19182
# #200-139 = 61
# #посчитали разницу между f(139)/f(137) - f(138)/f(136)
# # - эта послежовательность всегда на 2 увеличивается и складывается
# # и так будет еще 61 раз. На данный момент это 278, затем будет 280.

# x = 19460
# tmp = 278
# for ii in range(0, 61):
#     tmp += 2
#     x += tmp
    

# print(tmp, x)

# #Ответ: 40200






# def f(n):
#     if n >= 2024:
#         return 1
#     else:
#         return (f(n+2) + f(n+4))


# counter = 0
# for ii in range(2012, 2026):
#     f(ii)
#     counter += 1

# print(1)

# #Ответ: 1013




#КИМ № 25030012
# from functools import *
# from sys import *

# @lru_cache(None)
##или можно вот так:
#setrecursionlimit(99999999)#и пишем очень большое число

# def f(n):
#     if n < 3:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return (2 * f(n-2) - f(n-1) + 2)
#     elif n > 2 and n % 2 != 0:
#         return (2 * f(n-1) + f(n-2) - 2)
    

#print(f(170))
#3596910688800


#перевод числе из десятичной в любую дугую систему исчесления( менять двойку для этого)
# n = int(input())

# b = ''

# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2

# print(b)







#КИМ № 25030012
#номер 13
# from itertools import product

# counter = 0
# for i in product('01', repeat = 4):
#     a = ''.join(i)
#     if 2 <= a.count('0'):
#         counter += 1
#         print(''.join(i))

# print(counter)


# from ipaddress import *

# net = ip_network('192.168.32.160/255.255.255.240', 0)
# count = 0
# for ii in net:
#     if bin(int(ii))[2:].count('0') > 21:
#         count+=1
# print(count)






#это через рекурсию:
# from functools import *
# from sys import *

# setrecursionlimit(99999999)
# @lru_cache
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n - 2 + f(n - 1))
#     if n < 1:
#         return 0
    

# print(f(2024) - f(2022))
#Ответ: 4043

#это способ без рекурсии:

array = [0]*3000
for n in range(0, 3000):
    if n == 1:
        array[n] = 1
    if n > 1:
        array[n]=  (n - 2 + array[n - 1])
        

print(array[2024] - array[2022])

#Ответ: 4043