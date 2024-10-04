#Практическая работа № 71.	
#Обработка смешанных данных из файла

'''
Уровень A. В файле записаны данные о результатах сдачи экзамена. Каждая строка содержит фамилию, имя и количество баллов, разделенные пробелами:
<Фамилия> <Имя> <Количество баллов>
Вывести в другой файл фамилии и имена тех учеников, которые получили больше 80 баллов.
'''

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\Результаты экзамена.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output Экзамен.txt", "w")

outputArray = []

while True:
    var = Fin.readline()
    if not var:
        break
    points = int(var.split()[2])
    if points > 80:
        surName = var.split()[0]
        Fout.write(str(surName) + " ")
        name = var.split()[1]
        Fout.write(str(name) + "\n")
        '''
        surName = var.split()[0]
        name = var.split()[1]
        outputArray.append(surName)
        outputArray.append(name)
        outputArray.append("\n")
        


s = " ".join(map(str, outputArray))
Fout.write(s)
'''
Fin.close()
Fout.close()
