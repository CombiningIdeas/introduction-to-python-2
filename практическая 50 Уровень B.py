
#Практическая 50 Уровень В

number = int(input("Введите натуральное число: \n"))


def multipliers(number):
    k = 2
    while k ** 2 <= number:
        if number % k == 0:
            print(k, end = "*")
            multipliers(number // k)           
        k += 1 #чтобы не пропустить простые числа, поэтому увеличеваем.
        
    return ""

        
            

print(number," = ", end="", sep = "")

s = multipliers(number)
print(s)
