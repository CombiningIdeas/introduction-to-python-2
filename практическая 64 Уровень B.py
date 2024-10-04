#Практическая работа № 64.	
#Строки в процедурах и функциях

#Уровень B. Напишите функцию, которая заменяет расширение файла на заданное новое расши-рение. 
def reverse_extension(x, x1):
    if "." in x:
        x = "".join(reversed(x))
        x1 = "".join(reversed(x1))
        x3 = x
        for ii in range(len(x)):
            if x[ii] != ".":
                x3 = x3[1::]
            else:
                break
        x3 = x1 + x3
        x3 = "".join(reversed(x3))
        return x3
    else:
        return x + "." + x1

s = str(input("Введите имя файла: \n"))
s1 = str(input("Введите новое расширение: \n"))
print(reverse_extension(s, s1))
