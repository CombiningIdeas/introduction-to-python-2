#Классная работа

#Задача 1
#Напиши функцию neg_to_zero(x), которая заменяет в переданной строке все отрицательные числа на ноль.
'''
def neg_to_zero(x):
    x1 = ""
    for ii in range(len(x)):
        if x[ii] < 0:
            x1 += str(0) + " "
        else:
            x1 += str(s[ii]) + " "

    x1 = x1[:-1]#В конце убираем последний элемент потому что это будет пробел в любом случае
    return x1

s = list(map(int, input("Введите строку: \n").split()))
print(neg_to_zero(s))
'''


#Задача 2
#Напиши функцию make_positive(x), которая в строке меняет знак у отрицательных чисел и возвращает их количество.
'''
counter = 0
def make_positive(x):
    global counter
    x1 = ""
    for ii in range(len(x)):
        if x[ii] < 0:
            x1 += str(abs(x[ii])) + " "
            counter += 1
        else:
            x1 += str(s[ii]) + " "

    x1 = x1[:-1]#В конце убираем последний элемент потому что это будет пробел в любом случае
    return x1

s = list(map(int, input("Введите строку: \n").split()))
print(make_positive(s))
print("Количество замен отрицательных чисел:", counter)
'''


#Задача 3
#Напиши функцию reverse_all(x), которая в переданной строке разворачивает все слова задом наперёд.

def reverse_all(x):
    x1 = ""
    for ii in x:
        #x1 += "".join(reversed(ii)) + " "
        # Или можно вот так:
        x1 += ii[::-1] + " "
        
    x1 = x1[:-1]
    return x1
s = list(map(str, input("Введите строку: \n").split(" ")))
print(reverse_all(s))



