# #номер №14(1)
# n = 343**5-7**9+48
# k = 0

# while n > 0:
#     if n % 7 == 6:
#         k += 1
#     n //= 7
# print(k)





# #номер №14(2)

# for ii in range(0, 1000):
#     x = ii
#     n = 343**5+7**3-1-x
#     k = 0
#     while n > 0:
#         if n % 7 == 6:
#             k += 1
#         n //= 7
        
#     if k == 12:
#         print(x)
        


# #номер №14(3)
# n = 729**7+3**16-18
# k = 0
# while n > 0:
#     if n % 9 == 0:
#         k += 1
#     n //= 9
        
# print(k)


# #ЕГЭ мартовский вариант

# globalString = ''
# for ii in range(200, 0, -1):
#     ii_2 = ii#так как мы в коде будем изменять ii
#     string = ''
#     while ii > 0:
#         string = str(ii % 4) + string
#         ii = ii // 4
        
#     print(string)
#     print(string[:-4:-1])
#     if (string[:-4:-1] == '321'):
#         globalString += str(ii_2)


# print(globalString)

# #Ответ: 1559127



#КИМ № 25030012
#№14

# n = int(input())

# b = ''

# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2

# print(b)

# for ii in range(0, 150):
#     a = 5*150**4 + 1*150**3 + ii*150**2 + 2*150 + 9
#     b = ii*150**3 + 0 + 2*150 + 3
#     if (a + b) % 149 == 0:
#         print((a + b) // 149)
        

#20157588





#Прогноз ЕГЭ 2024(1)

# for x in range(0, 19):
#     #98x79641 + 36x14 + 73x4
#     a = 9*19**9 + 8*19**8 + x*19**7 + 7*19**6 + 9*19**5 + 6*19**4 + 4*19**3 + 1*19**2 + 1*19**1 + 9*19**0
#     b = 3*19**6 + 6*19**5 + x*19**4 + 1*19**3 + 4*19**2 + 1*19**1 + 9*19**0
#     c = 7*19**5 + 3*19**4 + x*19**3 + 4*19**2 + 1*19**1 + 9*19**0
#     res = a + b + c
#     if (res % 18 == 0):
#         print(a, b, c)



#Номер 13:
#Номер 13:
#Номер 13:        
#from itertools import *
# s = "10"

# counter = 0
# for ii in product(s, repeat = 6):
#     a = ''.join(ii)
#     if (a.count("1") % 2 != 0):
#         counter += 1

# print(counter)




#Номер 14




# from itertools import *

# counter = 0
# for ii in product("01", repeat = 19):
#     a = ''.join(ii)
#     if (a.count("1") % 2 != 0):
#         counter += 1
        
# print(counter)
#Ответ: 262144




s = 3*289**2024 + 81*49**121 - 9*16**81 - 6011
sm = 0

while (s > 0):
    digit = s%31
    digit = s % 31
    if digit <= 17:
        sm+= digit
    s //= 31
print(sm)
#Ответ: 16750