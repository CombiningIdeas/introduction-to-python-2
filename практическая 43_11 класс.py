# dictionary = {}
# for s in open('list_in.txt', 'r'):
#     s = s.strip()
#     if s in dictionary:
#         dictionary[s] += 1
#     else:
#         dictionary[s] = 1
    

# print(dictionary)

# sortKeys = sorted(dictionary, key = dictionary.get, reverse = True)
# print(sortKeys)

# f = open('list_out.txt', 'w')
# for i in sortKeys:
#     f.write(i + ' ' +str(dictionary[i]) + '\n')
# f.close()