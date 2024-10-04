# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     if x == 10: return 0
#     if x == 11: return 0
#     if x < y: return f(x+1, y) + f(x+2, y) + f(x*3, y)


# print(f(1, 8) * f(8, 27))




# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     if x == 14: return 0
#     if x < y: return f(x+1, y) + f(x+2, y) + f(x*3, y)


# print(f(2, 10) * f(10, 13))







# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     if x == 30: return 0
#     if x < y: return f(x+1, y) + f(x*2, y) + f(x*3, y)


# print(f(2, 12) * f(12, 36))




# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     if x == 30: return 0
#     if x < y: return f(x+1, y) + f(x*2, y) + f(x*3, y)


# print(f(2, 12) * f(12, 36))

# counter = 0
# for x in range(0, 10):
#     digit = 1
#     for y in range(0, 10):
#         for ij in range(0, 2):
#             if (ij == 0):
#                 digit = digit * 2
                
#             if (ij == 1):
#                 digit = digit * 2 + 1
                
            
#         print(digit)


# from itertools import *

# counter = 0
# for ii in product('12', repeat = 10):
#     s = ''.join(ii)
#     print(s)
#     counter += 1
    

# print(counter)



#≈√Ё март 2024 демо


# from itertools import *

# counter = 0
# for ii in product('12', repeat = 10):
#     s = ''.join(ii)
#     print(s)
#     counter += 1
    

# print(counter)

# for ii in range(10, 31):
#     number = ii**2
#     if (number % 2 == 0):
#         print(ii, number)
        
#и плюс 10**3 = 1000 и есть еще только 2 складывать, в итоге ответ: 11 + 1 + 1 = 13.



def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0

    if x > y: return f(x-1, y) + f(x-2, y) + f(x//3, y)


print(f(16, 11) * f(11, 6))