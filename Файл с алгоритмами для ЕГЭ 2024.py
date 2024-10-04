
#Задание №13 ЕГЭ 2024
from ipaddress import *

net = ip_network("192.128.32.160/255.255.255.240", 0)# 0 - означает точность до 0.
#или для более старой версии питона:
bin(int(ip))[2::].zfill(32)

k = 0
for i in net:
    print(i)
    if bin(int(i))[2::].count("1") > 8:
        k += 1
        print(i, bin(int(i))[2::])
print(k)

print(bin(224)[2::], bin(192)[2::])

#быстрое создание списка:
array = list(range(0, 5))
print(*array, type(array))

#Определить тип:
a = 5.0
print(type(a))


#перевод в любую систему исчесления:
def convert(x):
    notation = 2
    s = ''
    while x > 0:
        s = str(x % notation) + s
        x = x // notation

    return s

number = 555
print(convert(number))