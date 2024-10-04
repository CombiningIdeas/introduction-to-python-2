'''
Практическая работа № 61.	
Посимвольная обработка строк
'''

#Уровень C. Ввести с клавиатуры символьную строку и найдите самое длинное слово и его длину.
#Словом считается последовательности непробельных символов, отделенная с двух сторон пробелами (или стоящая с краю строки).
#Слова могут быть разделены несколькими пробела-ми, в начале и в конце строки тоже могут быть пробелы.

s = input("Введите строку: \n")

s1 = ""
arrayS1 = []

for c in s:
    if c != " ":
        s1 += c
    elif c == " " and s1 != "":
        arrayS1.append(s1)
        s1 = ""

arrayS1.append(s1)

print(arrayS1)

maxDigit = 0
array = []
for ii in range(len(arrayS1)):
    digit = len(arrayS1[ii])
    array.append(digit)
    if maxDigit < digit:
        maxDigit = len(arrayS1[ii])
        maximumDigit = arrayS1[ii]
        
print(f"Самое длинное слово: {maximumDigit}, длинна {maxDigit}")

