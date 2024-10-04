#Практическая работа № 66.
'''
Уровень B. Вводится несколько строк (не более 20), в которых сначала записан порядковый номер строки с точкой, а затем – слово.
Ввод заканчивается пустой строкой. Вывести введённые слова в алфавитном порядке.
'''

print("Введите слова: ")
array = []

while len(array) < 9:
    s = input()
    if s == "":
        break;
    array.append(s[3::])

while 9 <= len(array) <= 20:
    s = input()
    if s == "":
        break;
    array.append(s[4::])


array.sort()
s1 = ""

for i in range(len(array)):
    s1 += str(array[i]) + ", "

s1 = s1[:-2:]

print("Список слов в алфавитной порядке: \n", s1, sep = "")
'''
1. quweg
2. uuwe
3. poqeow
4. iuweq
5. weiu
6. wejkwep
7. uweuweww
8. aaaaewhjk
9. quwiuweuiw
10. uweuiwqeu
11. uyuerwyuhw
12. ywequiyzahj
13. weyurteyr
14. iiiioqw
15. hjsdfsf
16. pppdedrfe
17. weuywguey
18. wueiweu
19. lllsllre
20. bbbywqeurywe
'''
