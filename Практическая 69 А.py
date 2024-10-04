#Практическая работа № 69.	
#Файловый ввод и вывод

'''
Уровень A. Напишите программу, которая находит среднее арифметическое всех чисел,
записанных в файле в столбик, и выводит результат в другой файл.
'''

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

#Этот метод плох тем что полностью память компьюетра забивается.
'''
variable = Fin.read().split()
array = list(map(int, variable))

summNumbers = 0
counter = 0
long = len(array)

for ii in range(long):
    summNumbers += array[ii]
    counter += 1

mean = summNumbers / counter
print(mean)
'''

#Еще можно использовать readlines() читает так же как read весь файл и еще преобразовывает сразу в массив(список)
'''
array = Fin.readlines()# Но тут получиться массив содержащий строки, это нужно учитывать в дальнейшей работе со списком
summNumbers = 0
counter = 0
long = len(array)

for ii in range(long):
    summNumbers += int(array[ii])
    counter += 1

mean = summNumbers / counter
print(mean)
'''

#Этот метод лучше тем что тут компьютер не хранит все значения а переберает их по одному. Более быстрая версия работы с большими файлами.
'''
summNumbers = 0
counter = 0
while True:
    var = Fin.readline()
    if not var:
        break
    summNumbers += int(var)
    counter += 1

mean = summNumbers / counter
print(mean)
'''

Fout.write(str(mean))
Fin.close()
Fout.close()
