#Классная работа

s = list(map(float, input("Ввод: ").split()))
s2 = list(map(int, s))
#print(s2)

s3 = ""
for i in s2:
    s3 += str(i)
    s3 += "-"

s3 = s3[:-1:]
print(s3)
