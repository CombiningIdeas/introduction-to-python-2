# #Задание №15 ЕГЭ(1)

# for a in range(1, 100):
#     f = 1
#     for x in range(1, 500):
#         if ((90 % a == 0) and ((x % a != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))) == 0:
#             f = 0
#             break
#     if f == 1:
#         print(a)


# #Задание №15 ЕГЭ(2)

# for a in range(1, 100):
#     f = 1
#     for x in range(1, 500):
#         if ((70 % a == 0) and ((x % 28 == 0) <= ((x % a != 0) <= (x % 21 != 0)))) == 0:
#             f = 0
#             break
#     if f == 1:
#         print(a)



# #Задание №15 ЕГЭ(3)

# for a in range(1, 1000):
#     f = 1
#     for x in range(1, 1000):
#         if ((a % 45 == 0) and ((750 % x == 0) <= ((a % x != 0) <= (120 % x != 0)))) == 0:
#             f = 0
#             break
#     if f == 1:
#         print(a)

#ответ 90


# #Задание №15 ЕГЭ дз №1

# def f(x, y, a):
#     return (x + 2*y > 48) or (y > x) or (x + 3*y < a)

# for a in range(200, 1, -1):
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if f(x, y, a) == False:
#                 print(a)
#                 exit()

# #ответ: 64




# #Задание №15 ЕГЭ дз №2

# def f(x):
#     global a
#     return (((x&57>0) or (x&99>0)) <= (x&a>0)) == True

# for a in range(1, 1000):
#      if all(f(x) for x in range(1000)):
#          print(a)
#          break

# #ответ: почему то в ответ попадают все числа.





# #ЕГЭ вариант мартовский 2024 задание 15

# def f(x, y, a):
#     return (x + 2*y > 48) or (y > x) or (x + 3*y < a)

# for a in range(200, 1, -1):
#     for x in range(0, 100):
#         for y in range(0, 100):
#             if f(x, y, a) == False:
#                 print(a)
#                 exit()

# #ответ: 64



