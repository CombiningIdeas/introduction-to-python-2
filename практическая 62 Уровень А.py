'''
Практическая работа № 62.	
Функции для работы со строками
'''

#Уровень A. Ввести с клавиатуры в одну строку фамилию, имя и отчество, разделив их пробелом. Вывести фамилию и инициалы.

#Первый способ с использованием split().
'''
print("Введите имя, отчество и фамилию: ")
s = input()
fio = s.split()
s = fio[2] + " " + fio[0][0] + "." + fio[1][0] + "."
print(s)
'''
#Второй способ без использования split().

print("Введите имя, отчество и фамилию: ")
s = input()
n = s.find(" ")
name = s[:n] #Вырезать имя
s = s[n+1:]
n = s.find(" ")
name2 = s[:n] # Вырезать отчество
s = s[n+1:] #Осталась фамилия
s = s + " " + name[0] + "." + name2[0] + "."
print(s)


