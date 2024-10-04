'''
Практическая работа № 62.	
Функции для работы со строками
'''


#Уровень C. Напишите программу, которая заменяет во всей строке одну последовательность символов на другую.

s = input("Введите строку: \n")
whatChange = input("Что меняем: : \n")
whatReplace = input("Что меняем: : \n")

s1 = ""
arrayS1 = []


while whatChange in s:
    n = s.find(whatChange)
    s1 += s[:n]
    s1 += whatReplace 
    s = s[n+len(whatChange):]
    
if s1 == "":
    print("Ошибка! Неверно указан символ который нужно заменить.")
else:
    s1 += s
    print(f"Результат: \n{s1}")
