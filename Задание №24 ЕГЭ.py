# #ЕГЭ 2024 мартовский вариант

# f = open('24.txt')
# s = f.read()
# counter = 0
# consecutive_counter = 0
# tmp = 0#понадобится для опредления максимальное последовательсности
# maxDigit = 0

# for ii in range(0, len(s) - 2):
#     tmp = 0
#     string = str(s[ii]) + str(s[ii+1]) + str(s[ii+2])
#     if ( string == 'ABA') or (string == 'BAB'):
#         counter += 1
#         ii += 2#пишем плюс два так как нам нельзя захватывать больше 
#         #если подряд идти будут
#         tmp = 1#меняем флаг показывая что предыдущая последовательность 
#         #была нужной а не какой то другой
        
#     if (tmp == 1):
#         consecutive_counter += 1
#         maxDigit = max(maxDigit, consecutive_counter)
#     else:
#         consecutive_counter = 0

# print(maxDigit)





#ЕГЭ №24 (1.1)

# f = open('24 (1).txt')
# s = f.read()
# array = []
# array2 = []

# for ii in range(0 , len(s) - 1):
#     if (s[ii] == 'A'):
#         tmp = s[ii+1]
#         array.append(tmp)
#         if (not (tmp in array2)):
#             array2.append(tmp)
        
# #print(array2)
# maxNum = 0
# for ii in range(0, 26):
#     tmp2 = array.count(array2[ii])
#     maxNum = max(tmp2, maxNum)
            
# print(maxNum)

# for ii in range(0, len(array)):
#     tmp = array.count(array[ii])
#     if (tmp == maxNum):
#         print(array[ii])
#         break

# # lenght = len(array)
# # print(lenght)

# # maxNum = 0
# # for ii in range(0, lenght):
# #     tmp = array.count(array[ii])
# #     maxNum = max(tmp, maxNum)
    
# # print(maxNum)

# # for ii in range(0, lenght):
# #     tmp = array.count(array[ii])
# #     if (tmp == 1555):
# #         print(array[ii])
# #         break
    




#ЕГЭ №24 (1.2)

# f = open('24 (1).txt')

# array = [0] * 26

# for i in f:
#     for j in range(len(i) - 1):
#         if (i[j] == 'A') :
#             array[ord(i[j+1]) - ord('A')] += 1
            
# # ord - преобразовывает букву в число. по таблица анси
# print(max(array))


# mxL = 0
# mxN = 0

# for i in range(26):
#     if array[i] > mxL:
#         mxL = array[i]
#         mxN = i
        
# print(chr(mxN + ord('A')))
# # chr - преобразовывает число в букву. по таблица анси

# print(chr(ord('A') + array.index(max(array))))










# #ЕГЭ №24 (1.2)

# f = open('24№111.txt')

# array = [0] * 26

# for i in f:
#     for j in range(len(i) - 1):
#         if (i[j] == 'A') :
#             array[ord(i[j+1]) - ord('A')] += 1
            
# # ord - преобразовывает букву в число. по таблица анси
# print(max(array))


# mxL = 0
# mxN = 0

# for i in range(26):
#     if array[i] > mxL:
#         mxL = array[i]
#         mxN = i
        
# print(chr(mxN + ord('A')))
# # chr - преобразовывает число в букву. по таблица анси

# print(chr(ord('A') + array.index(max(array))))




# #ЕГЭ №24 (2)

# f = open('24№111.txt')

# array = [0] * 26

# for i in f:
#     for j in range(1, len(i) - 1):
#         if (i[j-1] == i[j+1]):
#             array[ord(i[j]) - ord('A')] += 1
            
# # ord - преобразовывает букву в число. по таблица анси
# print(max(array))


# mxL = 0
# mxN = 0

# for i in range(26):
#     if array[i] > mxL:
#         mxL = array[i]
#         mxN = i
        
# print(chr(mxN + ord('A')))
# # chr - преобразовывает число в букву. по таблица анси

# print(chr(ord('A') + array.index(max(array))))





# #ЕГЭ №24 (3)
# f = open('24№33.txt')

# array = [0] * 26

# minG = 10000000
# tmp_location_str = -1
# location_str = 0

# for i in f:
#     counterG = 0
#     tmp_location_str += 1
#     for j in range(len(i)):
#         if (i[j] == 'G'):
#             counterG += 1
            
#     if (counterG < minG):
#         minG = counterG
#         location_str = tmp_location_str
        
# print(minG, location_str)
     

# p = open('24№33.txt')
# arr = p.readlines()

# print(len(arr))
# print(arr[332])

# a = arr[332]
# mx = 0
# count = 0

# print(len(a))
# print(a[0], a[5])


# for i in range(0, len(a) - 1):   
#    array[ord(a[i]) - ord('A')] += 1
#    print(a[i])
   
# print('\n\n')

# for j in range(0, 26):
#     if (array[j] >= mx):
#         print(chr(ord('A') + j))
#         print(array[j])
#         mx = array[j]
#         print('\n\n')

# print(mx)

# #Ответ: T
# #Получается буквы D и T встречалисб по 50 раз но буква Т стоит дальше в алфавите


# are = [0, 1, 3 ,5]
# for ii in range(len(are)):
#     print(are[ii])








# #ЕГЭ №24 (4)
# f = open('24#44.txt')

# array = [0] * 26

# additional_array = []


# for i in f:
#     counterA = 0
#     for j in range(len(i)):
#         if (i[j] == 'A'):
#             counterA += 1
            
#     if (counterA < 25):
#         additional_array.append(i)
        

# print(len(additional_array))#значит всего 6 элементов
# #print(additional_array)
# print(len(additional_array[0]))
# print(len(additional_array[1]))
# print(len(additional_array[2]))#всего 1012 элементов значит 1011 элеимеент послеждний так как начало с 0
# print(len(additional_array[3]))


# tmp_val_1 = 0
# tmp_val_2 = 0
# max_letter_spacing = 0


# for ii in range(0, len(additional_array)):   
#    #array[ord(a[ii]) - ord('A')] += 1
#    #print(additional_array[ii])
#    print(additional_array[ii])
#    for jj in range(0, len(additional_array[ii])):
#        tmp_val_1 = (additional_array[ii])[jj]
#        for kk in range(jj, len((additional_array[ii]))):
#            tmp_val_2 = (additional_array[ii])[kk]
#            if (tmp_val_1 == tmp_val_2):
#                if (kk - jj > max_letter_spacing):
#                    max_letter_spacing = kk - jj
#                    if max_letter_spacing == 1004:
#                        print(ii)
#                        print(tmp_val_1)
#                        print(jj)
#                        print(kk)
#                        print('\n\n\n\n')
               

# #мы видми что последний элемент 1011 а буква С пеоследняя находитсмя на 1099 месте но копм считает
# #почему то считает посленюю позицию буквы С за 1008, но нам это не мешает понять
# #что правильно будет как в примере 7-2 = 5. Так и тут 1009 - 4 = 1005.                       

# print(max_letter_spacing)

# #Ответ: 1005 










# #ЕГЭ №24 (5)
# f = open('24#55.txt')
# s = f.readline()

# #print(len(s))
# additional_array = []

# count = 1
# max_count = 0

# count_A = 0
# max_count_A = 2

# tmp_str = ''
# str_max = ''

# for ii in range(0, len(s)):
#     additional_array.append(s[ii])
    

# for ii in range(0, len(additional_array)-1):
#     if (additional_array[ii] == additional_array[ii+1] or \
#         additional_array[ii+1] == 'A'):
#         if (max_count_A > count_A):
#             if (additional_array[ii+1] == 'A'):
#                 count_A += 1
#                 count -= 1
#             count += 1
#             tmp_str += str(additional_array[ii])
#         else:
#             count_A = 0
#     elif (additional_array[ii] != additional_array[ii+1]):
#         tmp_str += str(additional_array[ii])
        
#         if (len(str_max) < len(tmp_str)):
#             str_max = tmp_str
            
#         max_count = max(max_count, count)
        
#         count_A = 0
#         count = 1
#         tmp_str = ''
        


# print(max_count, str_max)

# #Ответ: 5 символов








# f = open("24#66.txt")
# s = f.readline().split('A')

# mx = 0

# for i in range(len(s)-1):
#     count = 0
#     count_E = 0
#     for j in range(len(s[i])-1):
#         if ( (s[i])[j] == (s[i])[j+1] or (s[i])[j+1] == 'E'):
#             count += 1
#             if (count_E >= 3):
#                 mx = max(mx, count)
#         elif ((s[i])[j] == 'E'):
#             if ((s[i])[j-1] == (s[i])[j+1] or (s[i])[j+1] == 'E'):
#                 count += 1
#                 count_E += 1 
#                 if (count_E >= 3):
#                     mx = max(mx, count)
        
# print(mx)



# f = open('24.txt')
# s = f.readline().split('A')
# a = []
# for i in range(len(s)):
#     if s[i].count('E') >=3:
#         a.append(len(s[i]))
# print(max(a))
# print(s)


# f = open("24#66.txt")
# s = f.readline().split('A')

# mx = 0

# for i in range(len(s)-1):
#     count = 0
#     count_E = 0
#     for j in range(len(s[i])-1):
#         if ( (s[i])[j] == (s[i])[j+1] or (s[i])[j+1] == 'E'):
#             count += 1
#             if (count_E >= 3):
#                 mx = max(mx, count)
#         elif ((s[i])[j] == 'E'):
#             if ((s[i])[j-1] == (s[i])[j+1] or (s[i])[j+1] == 'E'):
#                 count += 1
#                 count_E += 1 
#                 if (count_E >= 3):
#                     mx = max(mx, count)
        
# print(mx)




#Ким 25030012
#Номер файла: 24_10724

# f = open("24_10724.txt")
# s = f.readline()

# max_count = 0
# tmp_count = 0

# for ii in range(0, len(s) - 1):
#     if (s[ii] == "0" or s[ii] == "1" or s[ii] == "2" or s[ii] == "3" or s[ii] == "4" or s[ii] == "5" or s[ii] == "6" or s[ii] == "7" or
#         s[ii] == "8" or s[ii] == "9" or s[ii] == "A" or s[ii] == "B" or s[ii] == "C" or s[ii] == "D" or s[ii] == "E" or s[ii] == "F"):
#         if (s[ii] == "0"):
#             if (s[ii-1] != "0"):
#                 tmp_count += 1
#         else:
#             tmp_count += 1
#     else:
#         tmp_count = 0
            
#     if (tmp_count > max_count):
#         max_count = tmp_count
        
# print(max_count)
# #21