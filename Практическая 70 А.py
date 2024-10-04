#Практическая работа № 70.	
#Обработка массивов из файла

'''
Уровень A. В файле записано не более 100 чисел. Отсортировать их по возрастанию последней цифры и записать в другой файл.
'''

def summDigit(number):
    lastDigit = 0
    for ii in str(number):
        lastDigit = int(ii)

    return lastDigit


Fin = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\input.txt", "r")
Fout = open("F:\учеба\Информатика\школа пайтон\Папка для работы с файлами Python\output.txt", "w")

variable = Fin.read().split()
arrayA = list(map(int, variable))

arrayB = sorted(arrayA, key = summDigit)
s = " ".join(map(str, arrayB))
# или s = " ".join(arrayB) только если имеет тип str но не int, как тут, либо можно еще через цикл к строке прибовлять по элоементу
#прибовлять по одному элементу списка преобразовывая его к str

Fout.write(s)
Fin.close()
Fout.close()
