#Первый способ:
# fin = open("number9.txt")
# arrayA = fin.read().split()
# print(*arrayA)

# counter = 0
# for ii in range(0, len(arrayA) - (1 + 5), 6):
#     counter += 1

#     arr = []
#     for jj in range(0, 6):
#         arr.append(arrayA[jj+ii])
        
#     print(*arr)

#     if (arr.count(arr[0]) + arr.count(arr[1]) + arr.count(arr[2]) + arr.count(arr[3]) \
#         + arr.count(arr[4]) + arr.count(arr[5])) != 8:
#         continue
#     else:
#         tmp_summ = 0
#         novtor = 0
#         tmp = 0
#         for ii in range(0, 6):
#             if (arr.count(arr[jj]) == 1):
#                 tmp_summ += int(arr[jj])
#             else:
#                 tmp = int(arr[jj])
                
#         tmp_summ = tmp_summ / 4.0
#         novtor += tmp
        
#         if (novtor > tmp_summ):
#             print(counter)
#             break
        


#Второй способ:
# with open("Текстовый документ.txt", "r") as file:
#     counterStr = 0

#     for line in file:
#         counterStr += 1
#         line = [int(x) for x in line.split()]

#         rep = [i for i in line if line.count(i) == 2]
#         un = [i for i in line if line.count(i) == 1]

#         if (len(rep) == 2) and (len(un) == 4) and (rep[0] >= sum(un)/4):
#             print(counterStr)
#             break


fin = open("number901.txt")
array = list(map(int, (fin.read().split())))
print(*array)

count = 0
for ii in range(0, (len(array) - 1) - 5, 5):
    
    tmp_array = []
    for jj in range(0, 5):
        tmp_array.append(array[ii + jj])


    if (tmp_array.count(tmp_array[0]) + tmp_array.count(tmp_array[1]) + tmp_array.count(tmp_array[2]) + 
        tmp_array.count(tmp_array[3]) + tmp_array.count(tmp_array[4])) != 5:
        continue
    else:
        if (((min(tmp_array) + max(tmp_array)) * 2) <= (sum(tmp_array) - min(tmp_array) - max(tmp_array))):
            count += 1


print(count)
#Ответ: 607

