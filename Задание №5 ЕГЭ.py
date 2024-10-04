
##ЕГЭ №5(2)
#for n in range(10, 100):
#    s = bin(n)[2::]
#    #print(s)
#    s += s[-2]
#    s += s[1]
#    ds = int(s, 2)
#    if ds > 150:
#        print(n)
#        break



##ЕГЭ №5(3)
#for n in range(10, 100):
#    s = bin(n)[2::]
#    s1 = s[:-1:] + s[1] + s[1]
#    R = int(s1, 2)
#    if R > 92:
#        print(n)
#        break




##ЕГЭ №5(4.1)
#for n in range(100, 1000):
#    s = bin(n)[2::]
#    count = 0
#    while (count < 3):
#        num1 = 0
#        num0 = 0
#        for ii in range(len(s)):
#            if s[ii] == '1':
#                num1 += 1
#            else:
#                num0 += 1
#        if (num1 == num0):
#            s += s[-1]
#        elif (num1 > num0):
#            s += '0'
#    elif (num1 < num0):
#        s += '1'
#    count += 1

#R = int(s, 2)
#if (R % 4 == 0):
#    print(n)
#    break





##ЕГЭ №5(4.2)
#for n in range(100, 1000):
#    s = bin(n)[2::]
#    for ii in range(3):
#        if s.count('0') > s.count('1'):
#            s += '1'
#        elif s.count('0') < s.count('1'):
#            s += '0'
#        elif s.count('0') == s.count('1'):
#         s += s[-1]

#    R = int(s, 2)
#    if (R % 4 == 0):
#        print(n)
#        break








##ЕГЭ №5 дз №1
#count = 0
#for n in range(1, 1000):
#    if ((n % 2) == 0):
#        n = n / 2
#    else:
#        n = n - 1

#    if ((n % 3) == 0):
#        n = n / 3
#    else:
#        n = n - 1

#    if ((n % 5) == 0):
#        n = n / 5
#    else:
#        n = n - 1

#    if n == 1:
#        count += 1

#print(count)







##ЕГЭ №5 дз №2

#for n in range(1, 100000):
#    count_even = 0
#    even = 0
#    for ii in range(0, len(str(n))):
#        if int(str(n)[ii]) % 2 == 0:
#            even += int(str(n)[ii])
#        if (ii+1) % 2 == 0:
#            count_even += int(str(n)[ii])

#    result = abs(even - count_even)
#    if (result == 13):
#        print(n)
#        break





##ЕГЭ №5 дз №3

#for n in range(1, 100000):
#    count_even = 0
#    even = 0
#    for ii in range(0, len(str(n))):
#        if int(str(n)[ii]) % 2 == 0:
#            even += int(str(n)[ii])
#        if (ii+1) % 2 == 0:
#            count_even += int(str(n)[ii])

#    result = abs(even - count_even)
#    if (result == 9):
#        print(n)
#        break




##ЕГЭ №5 дз №4

#for n in range(1, 100000):
#    s = bin(n)[2::]
#    count_1 = 0
#    count_0 = 0
#    for ii in range(len(str(s))):
#        if ((ii+1) % 2 == 0) and int(str(s)[ii]) == 1:
#            count_1 += 1
#        if ((ii+1) % 2 != 0) and int(str(s)[ii]) == 0:
#            count_0 += 1

#    R = abs(count_1 - count_0)
#    if R == 5:
#        print(n)# - это ответ
#        print(s)# - это проверка
#        break









##ЕГЭ №5 дз №5

#for n in range(10, 10000):
    
#    min_num = int( str(n)[0] + str(n)[1])
#    max_num = int( str(n)[0] + str(n)[1])
#    for ii in range(0, len(str(n)) - 1):
#        tmp = int( str(n)[ii] + str(n)[ii+1])
#        if tmp < min_num:
#            min_num = tmp
#        if tmp > max_num:
#            max_num = tmp

#    #print(min_num) - проверка

#    R = max_num + min_num
#    if R == 137:
#        print(n)
#        break






##ЕГЭ №5 дз №6

#for n in range(10, 10000):
#    min_num = int(str(n)[0] + str(n)[1])
#    max_num = int(str(n)[0] + str(n)[1])
#    for ii in range(0, len(str(n)) - 1):
#        tmp = int(str(n)[ii] + str(n)[ii+1])
#        if tmp < min_num:
#            min_num = tmp
#        if tmp > max_num:
#            max_num = tmp

#    R = max_num - min_num
#    if R == 44:
#        print(n)
#        break



#x = 23455
#r=str(x)[:3:]
#print(r)


##ЕГЭ №5 дз №7.1

#for n in range(1000, 10000):
#    s = bin(n)[2::]
#    for ii in range(0, len(str(s))):
#        if (str(s)[ii] == '0'):
#            s = str(s)[:ii:] + str(1) + str(s)[ii+1::]
#        elif (str(s)[ii] == '1'):
#            s = str(s)[:ii:] + str(0) + str(s)[ii+1::]


    
#    R = int(s, 2)
#    res = n - R
#    if res == 999:
#        print(n)
#        break

##ЕГЭ №5 дз №7.2

#for n in range(1000, 10000):
#    s = bin(n)[2::]
#    s1 = s.replace('1', '-')
#    s1 = s1.replace('0', '1')
#    s1 = s1.replace('-', '0')
#    s = int(s1, 2)
#    R = n - s
#    if R == 999:
#        print(n)
#        #print(s)
#        #print(R)
#        break




##ЕГЭ №5 дз №8.1

#for n in range(1, 10000):
#    s = bin(n)[2::]
#    n1 = n

#    for jj in range(3):
#        count = 0
#        for ii in range(len(str(n))):
#            count += int(str(n)[ii])

#        if count % 2 == 0:
#            s = str(s) + '0'
#        elif count % 2 != 0:
#            s = str(s) + '1'

#        n = int(s, 2)

#    R = int(s, 2)
#    if R > 1028:
#        print(R)
#        break



##ЕГЭ №5 дз №8.2

#for n in range(1, 10000):
#    s = bin(n)[2::]
#    x = sum(int(i) for i in str(n))
#    s += '1' if x % 2 != 0 else '0'
#    for j in range(2):
#         x = sum(int(i) for i in str(int(s, 2)))
#         s += '1' if x % 2 != 0 else '0'

#    R = int(s, 2)
#    if R > 1028:
#        print(R)
#        break





##ЕГЭ №5 дз №9

##(15432098, 248456790):
#for n in range(15432096, 248456790):
#    s = bin(n)[2::]
#    n1 = n

#    for jj in range(3):
#        count = 0
#        for ii in range(len(str(n))):
#            count += int(str(n)[ii])

#        if count % 2 == 0:
#            s = s + '0'
#        elif count % 2 != 0:
#            s = s + '1'

#        n = int(s, 2)

#    R = int(s, 2)
#    print(R)
#    print(n1)
    
#    if (123456789 <= R):
#        print(R)# R - 123456796
#        print(n1)#n1 - 15432099 - это как раз начиная с этого числа
#        break

#    #if (1987654321 < R):
#    #    print(R)# R - 1987654325
#    #    print(n1)#n1 - 248456790 это уже больше на 1, но в цикле права граница не n, а n-1
#    #    break

#print(248456789 - 15432098)#233024691 - это ответ








##ЕГЭ №5 дз №10
#counter = 0

#for n in range(15432, 123456791):
#    s = bin(n)[2::]
#    for ij in range(3):
#        count_even = 0
#        count_uneven = 0
#        for ii in range(0, len(str(n))):
#            if (int(str(n)[ii]) % 2) == 0:
#                count_even += 1
#            if (int(str(n)[ii]) % 2) != 0:
#                count_uneven += 1

#        if (count_even > count_uneven):
#            s = s + '1'
#        elif (count_even < count_uneven):
#            s = s + '0'
#        else:
#            if (n % 2 == 0):
#                s = s + '0'
#            elif (n % 2 != 0):
#                s = s + '1'

#    R = int(s, 2)
#    print(R)
#    if (R > 123455):
#        print(R)
#        print(n)#15432 - то откуда начинается
#        break
#    #if (123455 < R) and (R < 987654321):
#    #    counter += 1
#    if (R > 987654321):
#        print(R)
#        print(n)# 123456791 - это уже выход за пределы, но в цикле правая граница берется в круглые скобки
#        break

#print(counter)# по итогу нет смысла так считать легче найти границы R - с двух сторон 
##и сколько при этом получается n - тогда будет известно, что столько же и R
##ведь из одного n получается одно R
##тогда получаем:

#print(123456790 - 15432)# 123441358 - ответом будет это число






##ЕГЭ №5 дз №11
#tmp_n = 0
#tmp_R = 0
#for n in range(1, 1000000):
#    s = bin(n)[2::]

#    if (n % 5) == 0:
#        s = s + bin(5)[2::]
#    else:
#        s = s + '1'

#    if (int(s, 2) % 7) == 0:
#        s = s + bin(7)[2::]
#    else:
#        s = s + '1'


#    R = int(s, 2)
#    if (R < 1728404):
#        if (n > tmp_n):
#            tmp_n = n
#            tmp_R = R



#print(tmp_n)#432098
#print(tmp_R)#1728395
##Ответ: 432099 - это наибольшее число


# for ii in range(100, 999):
#     num1 = int(str(ii)[0])
#     num2 = int(str(ii)[1])
#     num3 = int(str(ii)[2])
#     summ_num = num1 + num2 + num3
#     if (ii / summ_num == 87):
#         print(ii, summ_num)
       




# for ii in range(1000, 10000):
#     #max_digit = max(int(str(ii)[0]), int(str(ii)[1]), int(str(ii)[2]),int(str(ii)[3]))
#     #min_digit = min(int(str(ii)[0]), int(str(ii)[1]), int(str(ii)[2]),int(str(ii)[3]))
#     #max_digit = max(int(str(ii)[jj]) for jj in range(0, 4))
#     #min_digit = min(int(str(ii)[jj]) for jj in range(0, 4))
    
#     if ((int(str(ii)[0])) == (int((str(ii)[1]))) or \
#         (int(str(ii)[0])) == (int((str(ii)[2]))) or \
#         (int(str(ii)[0])) == (int((str(ii)[3]))) or \
#         (int(str(ii)[1])) == (int((str(ii)[2]))) or \
#         (int(str(ii)[1])) == (int((str(ii)[3]))) or \
#         (int(str(ii)[2])) == (int((str(ii)[3])))):
#         continue
    
        
#     tmp1 = -1
#     tmp2 = -1
#     max_digit = -1
#     min_digit = 11
#     counter1 = -3; counter2 = -3

#     for jj in range(0, 4):
#         if max_digit < int(str(ii)[jj]):
#             max_digit = int(str(ii)[jj])
#             counter1 = jj
#         if min_digit > int(str(ii)[jj]):
#             min_digit = int(str(ii)[jj])
#             counter2 = jj
            
#     tmpCounter = -5
#     for gg in range(0, 4):
#         if (gg != counter1) and (gg != counter2):
#             if tmp1 == -1:
#                 tmp1 = int(str(ii)[gg])
#                 tmpCounter = gg
#         if (gg != counter2) and (gg != counter1) and (gg != tmpCounter):
#             if tmp2 == -1:
#                 tmp2 = int(str(ii)[gg])
            

#     summ1 = max_digit + min_digit
#     summ2 = tmp1 * tmp2
    
#     newMaxDigit = max(summ1, summ2)
#     newMinDigit = min(summ1, summ2)
    
#     R = int(str(newMinDigit) + str(newMaxDigit))
    
#     if R > 85:
#         print(ii)
#         print(max_digit, min_digit, ii)
#         break



# from itertools import *

# k = 0
# sg = 'ГПРБЛ'
# gl = 'ИЕОА'
# for ii in product('ГИПЕРБОЛА', repeat = 6):
#     s = ''.join(ii)
#     if (s[0] in sg and s[-1] in sg):
#         if s[1] in gl and s[2] in gl:
#             k+=1
#         if s[2] in gl and s[3] in gl:
#             k+=1
#         if s[3] in gl and s[4] in gl:
#             k+=1


#         if s[1] in gl and s[2] in gl and s[3] in gl:
#             k+=1
#         if s[2] in gl and s[3] in gl and s[4] in gl:
#             k+=1

#         if s[2] in gl and s[3] in gl and s[4] in gl and s[5] in gl:
#             k+=1



#         #if all( for kk in range(1, len(s)):
#                #k+=1
# print(k)





# class Pet:
#   def __init__(self):
#     self.name = "Джек"
#     print(self.name)
#   def say(self):
#     print("Вау!")

# class Dog(Pet):
#   def say(self, name):
#     print(self.name)

# p = Dog()
# p.say("Миша")
# p.say("Гоша")




#ЕГЭ мартовский вариант



# for n in range(1, 1000):
#     digit = bin(n)[2::]

#     countForZero = 0
#     if (n % 2 == 0):
#         countForZero = digit.count('0')

#     digitStr = str(digit) + countForZero * '0'


#     countForOne = 0
#     if (n % 2 != 0):
#         countForOne = digit.count('1')

#     digitStr = countForOne * '1' + str(digit) 
    
#     digit = int(digitStr, 2)

#     if (digit > 2000):
#         print(n)
#         break
    
# #Ответ: 47





#КИМ № 25030012
#№5

# def convert(x):
#     s = ''
#     while x > 0:
#         s = str(x % 6) + s
#         x = x // 6

#     return s

# a = []

# for ii in range(1, 10**3):
#     copy_ii = convert(ii)


#     if (ii % 3 == 0):
#         copy_ii += copy_ii[:2:]
#     else:
#         copy_ii += convert((ii % 3) * 10) 
    
#     result = int(copy_ii, 6)
#     if (result > 680):
#         a.append(result)
        
# print(min(a))




#КИМ № 25032504
#Задание №5

# def convert(x):
#     s = ''
#     while x > 0:
#         s = str(x % 3) + s
#         x = x // 3

#     return s

# def f(y):
#     sumNum = 0
#     for ii in range(len(y)):
#         sumNum += int(y[ii])
        
#     return sumNum

# for n in range(1, 1000):
#     copy_ii = convert(n)
    
#     if (n % 2 == 0):
#         copy_ii = "1" + copy_ii + "00"
#     else:
#         tmpNum = f(copy_ii)
#         resultTmp = convert(tmpNum)
#         copy_ii = copy_ii + resultTmp
     
#     copy_ii = int(copy_ii, 3)
    
#     if (168 < copy_ii):
#         print(n, copy_ii)
        
#Ответ: 10


#Прогноз ЕГЭ 2024 
#Задание №5(1)

#print(str(12345)[-2::])


# tmp_min = 10000
# def convert(x):
#     s = ''
#     while x > 0:
#         s = str(x % 3) + s
#         x = x // 3

#     return s

# for n in range(1, 1000):
#     R = convert(n)
    
#     if (n % 3 == 0):
#         R = R + R[-2::]
#     else:
#         tmp = (n % 3) * 5
#         R = R + convert(tmp)
        

#     R = int(R, 3)
#     if (R > 133):
#         if (tmp_min > R):
#             tmp_min = R
            
# print(tmp_min)
# #141




#Прогноз ЕГЭ 2024
#Задание №5(2)

# new_number = ""
# for ii in range(100, 1000):
#     digit1 = int(str(ii)[0]) * int(str(ii)[1])
#     digit2 = int(str(ii)[1]) * int(str(ii)[2])

#     if (digit1 > digit2):
#         new_number = str(digit2) + str(digit1)
#     else:
#         new_number = str(digit1) + str(digit2)
        

#     if (new_number == "621"):
#         print(ii)
        
#Ответ: 732




# КИМ№ 25048321

# def convert(x):
#     notation = 3
#     s = ""
#     while x > 0:
#         s = str(x % notation) + s
#         x = x // notation
#     return s

# # z = "123345"
# # print(z[-2::])


# sc = set()
# for ii in range(1, 10**5):
#     R = convert(ii)
    
#     if (ii % 3 == 0):
#         R += R[-2::]
#     else:
#         R += convert((ii % 3)*5)

#     R = int(R, 3)
#     if (R > 133):
#         sc.add(R)
        
# print(min(sc))


#Ответ: 141