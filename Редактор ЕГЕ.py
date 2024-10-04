'''
#Задание ЕГЕ тест полякова №8
number = "5" * 146

while ("333" in number) or ("555" in number):
    if "555" in number:
        number = number.replace("555", "3", 1)
    else:
        number = number.replace("333", "5", 1)
print("Задание ЕГЕ тест полякова №8, ответ:", number)

#Задание ЕГЕ тест полякова №9
digit = "8" * 156

while ("222" in digit) or ("888" in digit):
    if "222" in digit:
        digit = digit.replace("222", "8", 1)
    else:
        digit = digit.replace("888", "2", 1)
print("Задание ЕГЕ тест полякова №9, ответ:", digit)
'''

ans = 0

for i in range(100, 1000):
    a, b, c = str(i)
    if a==b or a==c or b==c:
        ans += 1

print(ans)
