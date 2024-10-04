#Практическая работа № 69.	
#Файловый ввод и вывод

'''
Уровень B. Напишите программу, которая находит минимальное и максимальное среди чётных положительных чисел, записанных в файле,
и выводит результат в другой файл. Учтите, что таких чисел может вообще не быть.
'''
import sys

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

array = []     
    
while True:
    var = Fin.readline()
    if not var:
        break
    if int(var) > 0 and int(var) % 2 == 0:
        array.append(int(var))
        
if len(array) == 0:
    exit([0])
    
minNum = min(array)
maxNum = max(array)

s = str(minNum) + " " + str(maxNum)

Fout.write(s)
Fin.close()
Fout.close()
