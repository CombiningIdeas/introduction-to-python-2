
import random

#Уровень A. Игральный кубик бросается три раза (выпадает три случайных значения). Сколько очков в среднем выпало?

one_digit = random.randint(1, 6)
two_digit = random.randint(1, 6)
three_digit = random.randint(1, 6)

print("Выпало очков:")
print(one_digit, two_digit, three_digit)

print("({:d}+{:d}+{:d})/3={:5.3f}".format(one_digit,  two_digit, three_digit, (one_digit + two_digit + three_digit) / 3))
'''
#Уровень B. Игральный кубик бросается три раза (выпадает три случайных значения).
#Из этих чисел составляется целое число, программа должна найти его квадрат.

one_digit = random.randint(1, 6)
two_digit = random.randint(1, 6)
three_digit = random.randint(1, 6)
#Неясно почему нельзя использовать строки, ведь для этого они и нужны, при работе в компании, могут сказать на счет невклалифицированости разработчика
#если он все пишет сам не используя готовые библиотеки, методы и функции, которые понятны все, ниже пример как сдлелать легче со строками:
'''
'''
string_one_digit = str(one_digit)
string_two_digit = str(two_digit)
string_three_digit = str(three_digit)
#Затем просто сложить их в строчку также как и в 34 и 39 строке. А потом перед 41 строкой преобразовать это в int и возвести в квадрат
#без всех этих выеслений.
'''
'''
hundred_digit = one_digit * 100
ten_digit = two_digit * 10
units_digit = three_digit

number_digit = hundred_digit + ten_digit + units_digit

print("Выпало очков:")
print(one_digit, two_digit, three_digit)

print("Число", number_digit)

print("Его квадрат",number_digit**2)
'''
#Уровень C. Получить случайное трёхзначное число и вывести через запятую его отдельные цифры.
'''
digit = random.randint(100, 999)

hundred_digit = digit // 100
ten_digit = digit // 10 % 10
units_digit = digit % 10

print("Получено число", digit)

print("Сотни:", hundred_digit)
print("Десятки:", ten_digit)
print("Единицы:", units_digit)
'''
