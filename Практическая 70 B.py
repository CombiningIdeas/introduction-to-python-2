#Практическая работа № 70.	
#Обработка массивов из файла

'''
Уровень B. В файле записано не более 100 чисел. Отсортировать их по возрастанию суммы цифр и записать в другой файл.
Используйте функцию, которая вычисляет сумму цифр числа.
'''

def summDigit(number):
    summDigit = 0
    for ii in str(number):
        summDigit += int(ii)

    return summDigit


Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

variable = Fin.read().split()
arrayA = list(map(int, variable))

arrayB = sorted(arrayA, key = summDigit)
s = " ".join(map(str, arrayB))

Fout.write(s)
Fin.close()
Fout.close()
