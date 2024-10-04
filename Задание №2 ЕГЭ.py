##Домашняя работа ЕГЭ №2 (1)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((((x == (not y)) <= (y and (not z))) or (z and (not w))) == 0):
#                    print(x, y, z, w)


##Домашняя работа ЕГЭ №2 (2)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (not((x or y) <= (z and w))) and (x <= w):
#                    print(x, y, z, w)





##Домашняя работа ЕГЭ №2 (3)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (((x and (not y)) == (z or (not w))) <= (x and z)) == 0:
#                    print(x, y, z, w)




##Домашняя работа ЕГЭ №2 (4)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( (x == (not y)) <= ( (x and w) == (z and (not w)) ) ) == 0:
#                    print(x, y, z, w)



##Домашняя работа ЕГЭ №2 (5)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( ((x <= y) and (z or w)) <= ((x == w) or (y and (not z))) ) == 0:
#                    print(x, y, z, w)





##Домашняя работа ЕГЭ №2 (6)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( ((not y) <= (z == w)) and ((z <= x) == w) ) == 1:
#                    print(x, y, z, w)





##Домашняя работа ЕГЭ №2 (7)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( ((x <= y) == (z and w)) and (x <= z) ) == 1:
#                    print(x, y, z, w)






##Домашняя работа ЕГЭ №2 (8)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( (x == (y or z)) <= (y == (x and w)) ) == 0:
#                    print(x, y, z, w)






##Домашняя работа ЕГЭ №2 (9)

#print("x y z w")
#for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( (x == (not y)) <= ( (z <= (not w)) and (w <= y) ) ) == 1:
#                    print(x, y, z, w)





##Домашняя работа ЕГЭ №2 (10)

# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( ((x <= y) or (z <= w)) and ((z == y) <= (w == x)) ) == 0:
#                    print(x, y, z, w)



##Домашняя работа ЕГЭ №2 (11)
#from itertools import *

#def f1(x, y, z, w):
#    return ((x <= y) == (w or (not z)))

#def f2(x, y, z, w):
#    return ((x <= y) and ((not w) == z))


#for x1, x2, x3, x4, x5 in product([0, 1], repeat = 5):
#    a = [
#           (x1, 1, 0, 1) + (x4, 0),
#           (x2, 0, 0, 0) + (0, x5),
#           (0, x3, 0, 0) + (0, 1)
#        ]

#    if len(a) == len(set(a)):
#        for ii in permutations('xyzw'):
#            if all(f1(**dict(zip(ii, s))) == s[-2] and 
#                   f2(**dict(zip(ii, s))) == s[-1] for s in a):
#                print(*ii, sep = "")

#print("Result: xzyw")


##Домашняя работа ЕГЭ №2 (12)
#from itertools import *

#def f1(x, y, z, w):
#    return ((x or (not y)) <= (w == z))

#def f2(x, y, z, w):
#    return ((x or (not y)) == (z <= w))


#for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat = 6):
#    a = [
#           (0, x1, 0, 0) + (0, 0),
#           (x2, 1, 1, x3) + (0, x5),
#           (x4, 0, 0, 0) + (x6, 0)
#        ]

#    if len(a) == len(set(a)):
#        for ii in permutations('xyzw'):
#            if all(f1(**dict(zip(ii, s))) == s[-2] and 
#                   f2(**dict(zip(ii, s))) == s[-1] for s in a):
#                print(*ii, sep = "")


#print("Result: yzxw")



# print("a b c d")
# for a in range(0, 2):
#    for b in range(0, 2):
#        for c in range(0, 2):
#            for d in range(0, 2):
#                if (((a and b) <= c) and ((b and c) <= d)) == 0:
#                    print(a, b, c, d)
                   

#Ответ: dbac





# #ЕГЭ мартовский вариант

# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( ((1 == w) == (not ((w and x) or y))) <= z ) == 1:
#                    print(x, y, z, w)





# #КИМ № 25030012
# #номер 2
# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ( (x or (not y)) and (not(x == z)) and w) == 1:
#                    print(x, y, z, w)
                   

#Ответ: zyxw




#КИМ № 25032504
#Задание №2
# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((x and (not y)) or (x == z) or w) == 0:
#                    print(x, y, z, w)
                   
#Ответ: zyxw







#Прогноз ЕГЭ задание №2(1)
#(¬x /\ ¬y) \/ (y ≡ z) \/  w,         

# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if (((not x) and (not y)) or (y == z) or w) == 0:
#                    print(x, y, z, w)
          
#zwyx





#КИМ 25048321

# print("x y z w")
# for x in range(0, 2):
#    for y in range(0, 2):
#        for z in range(0, 2):
#            for w in range(0, 2):
#                if ((x or (not y)) and (not(y == z)) and (not w)) == 1:
#                    print(x, y, z, w)

#Ответ: xzyw