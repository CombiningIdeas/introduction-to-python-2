#Практическая работа № 71.	
#Обработка смешанных данных из файла

'''
Уровень B. В предыдущей задаче добавить к полученному списку нумерацию, сократить имя до одной буквы и поставить перед фамилией:
1)	П. Иванов
2)	И. Петров
3)	...
'''

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\Результаты экзамена.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output Экзамен.txt", "w")

outputArray = []
counter = 0
while True:
    var = Fin.readline()
    if not var:
        break
    points = int(var.split()[2])
    if points > 80:
        counter += 1
        Fout.write(str(counter) + ")" + " ")
        name = var.split()[1][0] + "."
        Fout.write(str(name) + " ")
        surName = var.split()[0]
        Fout.write(str(surName) + "\n")

        

Fin.close()
Fout.close()
