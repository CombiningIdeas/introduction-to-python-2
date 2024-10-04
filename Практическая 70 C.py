#Практическая работа № 70.	
#Обработка массивов из файла

'''
Уровень C. В двух файлах записаны отсортированные по возрастанию массивы неизвестной дли-ны. Объединить их и записать результат в третий файл.
Полученный массив также должен быть отсортирован по возрастанию.
'''

Fin1 = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fin2 = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input2.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

variable1 = Fin1.read().split()
arrayA1 = list(map(int, variable1))
variable2 = Fin2.read().split()
arrayA2 = list(map(int, variable2))

arrayA3 = arrayA1 + arrayA2

for ii in range(len(arrayA3) - 1):
    for jj in range(len(arrayA3) - 1 - ii):
        if arrayA3[jj] > arrayA3[jj+1]:
            arrayA3[jj], arrayA3[jj+1] = arrayA3[jj+1], arrayA3[jj]
    
s = " ".join(map(str, arrayA3))
print(arrayA3)
Fout.write(s)
Fin1.close()
Fin2.close()
Fout.close()
