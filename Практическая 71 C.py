#Практическая работа № 71.	
#Обработка смешанных данных из файла

'''
Уровень C. В файле записаны данные о результатах сдачи экзамена. Каждая строка содержит фамилию, имя и количество баллов, разделенные пробелами:
<Фамилия> <Имя> <Количество баллов>
Вывести в другой файл данные учеников, которые получили больше 80 баллов. Список дол-жен быть отсортирован по убыванию балла. Формат выходных данных: 
1)	П. Иванов	 98
2)	И. Петров 96
3)	...
'''

def sortArray(sortArray):
    #return int(sortArray.split()[3]) - поскольку так нельзя написать,
    #то можно через чикл получить полседний элемент в это списке который будет являться числом
    for ii in sortArray.split():
        temp = ii
    return int(temp)
    

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\Результаты экзамена.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output Экзамен.txt", "w")

outputArray = []
listOfResults = []
array = []

while True:
    var = Fin.readline()
    if not var:
        break
    points = int(var.split()[2])
    if points > 80:
        #long = len(var.split())
        listOfResults.append(var)

#N = long
M = len(listOfResults)

#print(N, M)

for i in range(1):
    outputArray.append([0]*M)


listOfResults = sorted(listOfResults, key = sortArray, reverse = True)
counter = 1
for ii in range(1):
    count = 0
    for jj in range(M):
        outputArray[ii][jj] = listOfResults[count].split()
        count += 1
        tmp = outputArray[ii][jj]
        tmp0 = str(tmp[0])
        tmp1 = str(tmp[1])
        tmp2 = str(tmp[2])
        print(tmp[0], end = " ") # - нужно для проверки как сортируется матрица
        print(tmp[1], end = " ")
        print(tmp[2])
        #Fout.write(str( str(counter) + ") " + str(*outputArray[ii][jj]) + "\n")) - со звездочкой
        #и присваванием сразу к строке нельзя писать поэтому разобьем на части вывод в файл как написано выше
        Fout.write(str( str(counter) + ") "))
        Fout.write(str(tmp0 + " " + tmp1 + " " + tmp2 + "\n"))
    print()


Fin.close()
Fout.close()

