from bintree import * 

s = input("Введите арифметическое выражение: ")

T = makeTree(s)

print("Результат:", calcTree(T))