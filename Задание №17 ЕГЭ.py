#Задание №17 ЕГЭ(1)
# fin = open('17.txt')
# variable = fin.read().split()
# arrayA = list(map(int, variable))
# print(arrayA)

# counter = 0
# mx = 0
# length = len(arrayA)
# for ii in range(0, length - 1):
#     pair1 = arrayA[ii]
#     pair2 = arrayA[ii+1]
#     if ((pair1 % 3 == 0) or (pair2 % 3 == 0)) \
#     and ((pair1 + pair2) % 5 == 0):
#         counter += 1
#         mx = max(mx, pair1+pair2)


# print(counter, mx)
# fin.close()




#Задание №17 ЕГЭ(2)
# fin = open('17_2.txt')
# arrayA = list(map(int, fin.readlines()))

# count = 0
# midl = 0
# for ii in range(len(arrayA)):
#     if (arrayA[ii] % 2 == 0):
#         count += 1
#         midl += arrayA[ii]
    
# midl = midl / count
# print(midl)

# counter = 0
# mx = 0
# for ii in range(len(arrayA) - 1):
#     pair1 = arrayA[ii]
#     pair2 = arrayA[ii+1]
#     if ((pair1 % 3 == 0) or (pair2 % 3 == 0)) and \
#         ((midl > pair1) or (midl > pair2)):
#         counter += 1
#         mx = max(mx, pair1+pair2)


# print(counter, mx)
# fin.close()








# #Задание №17 ЕГЭ дз №1
# fin = open('17 №1.txt')
# arrayA = list(map(int, fin.readlines()))

# count = 0
# midl = 0
# for ii in range(len(arrayA)):
#     if (arrayA[ii] % 2 == 0):
#         count += 1
#         midl += arrayA[ii]
    
# midl = midl / count
# print(midl)

# counter = 0
# mx = 0
# for ii in range(len(arrayA) - 1):
#     pair1 = arrayA[ii]
#     pair2 = arrayA[ii+1]
#     if ((pair1 % 3 == 0) or (pair2 % 3 == 0)) and \
#         ((midl > pair1) or (midl > pair2)):
#         counter += 1
#         mx = max(mx, pair1+pair2)


# print(counter, mx)
# fin.close()





#КИМ № 25030012
#Задание №17

#17_10719

# fin = open("17_10719.txt")
# arrayA = list(map(int, fin.readlines()))

# # s = "12345"
# # d = s[-2::]
# # print(d)

# arrayB = []#Нужен массив для записи индексов нужных пар из изначального массива

# generalCount = 0
# count = 0
# for ii in range(len(arrayA) - 1):
#     generalCount += 1
#     if (((str(arrayA[ii])[-2::] != "13") and (str(arrayA[ii+1])[-2::] == "13")) or
#         ((str(arrayA[ii])[-2::] == "13") and (str(arrayA[ii+1])[-2::] != "13"))):
#         count += 1
#         arrayB.append(generalCount)
#         arrayB.append(generalCount+1)

# print("кол-во пар:", count)

# maxSumm = 0
# for ii in range(len(arrayB) - 1):
#     pair1 = arrayA[arrayB[ii]]
#     pair2 = arrayA[arrayB[ii+1]]
#     ii+=2
#     if ((pair1 + pair2) > maxSumm):
#         maxSumm = pair1 + pair2

# print("максимальная сумма:", maxSumm)

#92
#19390
        
        


#17_84132

# fin = open("17_84132.txt")
# array = list(map(int, fin.readlines()))
# print(array)











fin = open('17_2.txt')
arrayA = list(map(int, fin.readlines()))

counter = 0
mx = 0
for ii in range(len(arrayA) - 1):
    pair1 = arrayA[ii]
    pair2 = arrayA[ii+1]
    tmp_min = min(pair1, pair2)
    if (((pair1 % 18) == tmp_min) and ((pair2 % 18) == tmp_min)):
        print(pair1 % 18)
        print(pair2 % 18)
        counter += 1
        mx = max(mx, pair1+pair2)
        print(counter, mx, pair1, pair2, tmp_min)



print(counter, mx)
# pair1 = 100
# pair2 = 50
# tmp_min = min(pair1, pair2)
# print(tmp_min)