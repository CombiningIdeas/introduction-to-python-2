#Практическая работа № 69.	
#Файловый ввод и вывод

'''
Уровень C. В файле в столбик записаны целые числа, сколько их – неизвестно.
Напишите про-грамму, которая определяет длину самой длинной цепочки
идущих подряд одинаковых чисел и выводит результат в другой файл. 
'''

Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

variable = Fin.read().split()
array = list(map(int, variable))

# set - преобразет список в множество, в котором нельзя оюращаться к элементам по индексам,
# но зато все элементы уникальны, поэтому с пмощью разницы длинны множества и списка можно найти количество повторяющихся элементов.
# count - считает число повторенийц кокретного элемента списка
setArray = set(array)
repeatElemArray = []

for ii in setArray:
    countElement = array.count(ii)
    if countElement > 1:
        repeatElemArray.append(countElement)

maxNum = max(repeatElemArray)

Fout.write(str(maxNum))
Fin.close()
Fout.close()
