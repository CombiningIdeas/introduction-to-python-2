#Практическая работа № 66.	

'''
Уровень C. Вводится несколько строк (не более 20), в которых сначала записаны инициалы и фа-милии работников фирмы.
Ввод заканчивается пустой строкой. Отсортировать  строки в алфа-витном порядке по фамилии.
'''

def surnameSort(x):
    return x[5::]

    
print("Введите слова: ")
array1 = []

while True and len(array1) <= 20:
    s = input()
    if s == "":
        break;
    array1.append(s)


array3 = sorted(array1, key = surnameSort)
s1 = ""

for i in range(len(array3)):
    s1 += str(array3[i]) + "\n"

s1 = s1[:-1:]

print("Список слов в алфавитной порядке: \n", s1, sep = "")


