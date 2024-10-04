#Классная работа 17.04.2023

#Выведи количество членов семьи, в которой живет Яша.

s = list(input().split())
s1 = []

for ii in s:
    if not(ii in  s1):
        s1.append(ii)

long = len(s1)

print(long)
