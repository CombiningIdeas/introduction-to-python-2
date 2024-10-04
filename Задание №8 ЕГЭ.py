#КИМ № 25030012
#Задание №8

# from itertools import *

# counter = 0
# for ii in product(sorted("КОМПЬЮТЕР"), repeat = 5):
#     a = ''.join(ii)
#     counter += 1
#     if (2 == a.count('К')) and (a[0] != "Ь") and (counter % 2 != 0):
#         print('\n',counter)
#         print(a)
        
#Ответ: 58979



#Прогноз 2024
#Задание №8(2)

# from itertools import *

# counter = 0
# for ii in product(sorted("КЛРТ"), repeat = 4):
#     a = ''.join(ii)
#     counter += 1
#     print('\n',counter)
#     print(a)
#     if (counter == 100):
#         break
    
#ЛККР


# general_counter = 0
# for ii in range(100000, 1000000):
#     if (ii % 5 == 0):
#         s_ii = str(ii)
#         if ((s_ii.count(s_ii[0]) + s_ii.count(s_ii[1]) + s_ii.count(s_ii[2]) + s_ii.count(s_ii[3]) \
#              + s_ii.count(s_ii[4]) + s_ii.count(s_ii[5])) == 6):
#             counter = 0
#             for jj in range(0, 6 - 1):
#                 tmp1 = int(s_ii[jj])
#                 tmp2 = int(s_ii[jj + 1])
#                 if (tmp1 % 2 == 0) and (tmp2 % 2 == 0):
#                     counter += 1
#                 elif (tmp1 % 2 != 0) and (tmp2 % 2 != 0):
#                     counter += 1
                
#             if (counter == 0):
#                 general_counter += 1
            

# print(general_counter)
#Ответ: 1296



№print((1024*768*8)/65536)