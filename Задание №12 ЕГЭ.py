# #Задание №12(4)

# for i in range(1, 45):
#     for j in range(1, 45):
#         for k in range(1, 45):
#             s = '0' + '1' * i + '2' * j + '3' * k
            
#             while ('01' in s) or ('02' in s) or ('03' in s):
#                 s = s.replace('01', '2302', 1)
#                 s = s.replace('02', '10', 1)
#                 s = s.replace('03', '201', 1)
                
#             if s.count('1') == 40 and \
#                 s.count('2') == 10 and \
#                 s.count('3') == 8:
#                 print(i)




# #Задание №12 дз №1

# for i in range(1, 50):
#     for j in range(1, 50):
#         for k in range(1, 50):
#             s = '0' + '1' * i + '2' * j + '3' * k + '0'
#             s1 = s
            
#             while not ('00' in s):
#                 s = s.replace('01', '210', 1)
#                 s = s.replace('02', '320', 1)
#                 s = s.replace('03', '3012', 1)
                
#             if s.count('1') == 23 and \
#                 s.count('2') == 48 and \
#                 s.count('3') == 41:
#                 print(s1, len(s1))
#                 s2 = s1

# print(len(s2))#ответ 34


# #Задание №12 дз №2
# tmpMin = 1000000
# for ii in range(201, 550):
#     s = '1' * ii
#     s1 = s
    
#     while ('111' in s) or ('222' in s):
#         s = s.replace('111', '22', 1)
#         s = s.replace('222', '1', 1)
        
#     if not ('2' in s):
#         print(s, s1.count('1'))
#         if s1.count('1') < tmpMin:
#             tmpMin = s1.count('1')
                

# print(tmpMin)#это нужное нам искомое кол во единиц в самом начале
# #ответ получился 205




# #Задание №12 дз №3
# tmpLen = 1000000
# digitOne = 0
# digit_one = 0
# for ii in range(201, 300):
#     s = '1' * ii
#     s1 = s
    
#     while ('1111' in s):
#         s = s.replace('1111', '22', 1)
#         s = s.replace('222', '1', 1)
        
#     tmpLen = len(s1)
#     digitOne = s.count('1')
#     print(tmpLen, digitOne)
#     if (s.count('1') > digit_one):
#         digit_one = s.count('1')
#         print('\n\n\n', tmpLen, digitOne)


# #ответ 201



# #Задание №12 дз №4

# for i in range(1, 75):
#     for j in range(1, 75):
#         for k in range(1, 75):
#             s = '0' + '1' * i + '2' * j + '3' * k + '0'
#             s1 = s
            
#             while not ('00' in s):
#                 s = s.replace('01', '210', 1)
#                 s = s.replace('02', '3101', 1)
#                 s = s.replace('03', '2012', 1)
        
        
#             if s.count('1') == 70 and \
#             s.count('2') == 56 and \
#             s.count('3') == 23:
#                 print(len(s1))
                
# #Ответ 40 - это колво цифр в исходной строке






# #Задание №12 дз №5


# for i in range(1, 50):
#     for j in range(1, 50):
#         s = '0' + '1'*i + '2'*j + '0'
        
#         while not ('00' in s):
#             s = s.replace('02', '20', 1)
#             s = s.replace('03', '30', 1)
#             s = s.replace('011', '1031', 1)
#             s = s.replace('01', '102', 1)
        
        
#         if s.count('1') == 17 and \
#          s.count('2') == 25 and \
#          s.count('3') == 4:
#             print(j)
                

# #ответ 12
                




#Задание №12 дз №6
# from itertools import * 


# for i in range(1, 20):
#    for j in product('12', repeat = 2*i):
#        s = ''.join(j)
#        s = '0' + s + '0'
       
#        if s.count('1') == s.count('2'):
#            while not ('00' in s):
#                s = s.replace('011', '20', 1)
#                s = s.replace('022', '10', 1)
#                s = s.replace('01', '220', 1)
#                s = s.replace('02', '110', 1)
               
#            print(s)
#            if s.count('1') == 40 and s.count('2') > 50:
#                print(s.count('2'))
       
#здесь тоже не получается узнать ответ, опять же я не вижу оишбок в скоей программе
#поэтому не знаю что здесь не так








# from itertools import * 


# for ii in range(4, 10001):
#     s = '1' + ii*'6'
    
    
#     while ('111' in s) or ('66' in s):
#         if ('6666' in s):
#             s = s.replace('6666', '1', 1)
#         else:
#             s = s.replace('111', '3', 1)
#         if ('66' in s):
#             s = s.replace('66', '6', 1)    
    
#     if s.count('3') == 5:
#         print(s, ii)
#         break
               

#ответ: 69




# #Номер 13 ЕГЭ февраль 2024 демо:

# from itertools import *
# a = bin(118)[4::]
# print(a, '\n')

# #print(int('01110110', 2))

# counter = 0
# for jj in product('10', repeat = 5):
#     if (not ('000' in ''.join(jj)) and (not ('111' in ''.join(jj)))):
#         counter += 1
#         print(''.join(jj))
        
# print(counter)
# #так как нам нужно определить по байту то первые три числа не меняются
# #это числа "011" - отсюдого видно, что нельзя брать следующую единицу,
# #так как будет 3 подряд единицы, соотвественно в ответ береме только те
# #варианты, которые начинаются с нуля, таких вариантов 8.


#Номер 13 ЕГЭ март 2024 демо:

#print(bin(160)[2::])

# from itertools import *
# a = bin(160)[6::]
# print(a, '\n')

# #print(int('01110110', 2))


# counter = 0
# for jj in product('10', repeat = 4):
#     num = ''.join(jj)
#     if ((num.count('1')  == 2) and  (int(num, 2) % 2 == 0 )):
#         counter += 1
#         print(''.join(jj))
        
# print(counter)
# #Ответ: 3






#КИМ № 25030012
#Задание №12

# maxLen = 0
# for ii in range(4, 1000):
#     s = '1' + ii * "2"
    
#     while ("12" in s) or ("322" in s) or ("222" in s):
#         if ("12" in s):
#             s = s.replace('12', '2', 1)
#         if ("322" in s):
#             s = s.replace('322', '21', 1)
#         if ("222" in s):
#             s = s.replace('222', '3', 1)
            
#     countLen = len(s)
#     if (countLen > maxLen):
#         maxLen = countLen
        

# print(maxLen)
#Ответ: 9



#Степик прогноз 

#№1
# for n in range(4, 10**7):
#     s = '2' + n * "5"
    

#     while ("25" in s) or ("355" in s) or ("555" in s):
#         if ("25" in s):
#             s = s.replace('25', '5', 1)
#         if ("355" in s):
#             s = s.replace('355', '52', 1)
#         if ("555" in s):
#             s = s.replace('555', '3', 1)
            
#     result = 0
#     for ii in range(len(s)):
#         result += int(s[ii])
        
#     if (result == 17):
#         print(result, n)
#         break


#Ответ: 29


#№2
# for n in range(4, 10**7):
#     s = '2' + n * "5"
    

#     while ("25" in s) or ("355" in s) or ("555" in s):
#         if ("25" in s):
#             s = s.replace('25', '5', 1)
#         if ("355" in s):
#             s = s.replace('355', '52', 1)
#         if ("555" in s):
#             s = s.replace('555', '3', 1)
            
#     result = s.count("3")
        
#     if (result == 2):
#         print(result, n)
#         break
    
#Ответ: 18



#№3
# for n in range(4, 10**7):
#     s = '3' + n * "5"
    

#     while ("25" in s) or ("355" in s) or ("555" in s):
#         if ("25" in s):
#             s = s.replace('25', '5', 1)
#         if ("355" in s):
#             s = s.replace('355', '52', 1)
#         if ("555" in s):
#             s = s.replace('555', '3', 1)
            
#     result = len(s)
        
#     if (result == s.count("5")):
#         print(s, n)
#         break
    
#Ответ: 19


# tmp_max = 0
# for n in range(4, 1000):
#     s = "1" + n * "9"
    

#     while ("19" in s) or ("49" in s) or ("999" in s):
#         if ("19" in s):
#             s = s.replace("19", "9", 1)
#         if ("49" in s):
#             s = s.replace("49", "91", 1)
#         if ("999" in s):
#             s = s.replace("999", "4", 1)

#     summ_num = 0
#     for jj in range(0, len(s)):
#         summ_num += int(s[jj])


#     if (summ_num > tmp_max):
#         tmp_max = summ_num
        
# print(tmp_max)
#Ответ: 23


#print(bin(128))