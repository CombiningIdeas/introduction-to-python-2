'''
Практическая работа № 52.	
Перебор элементов массива
'''
#Уровень B. Заполните массив случайными числами в интервале [0,100] и
#подсчитайте отдельно среднее значение всех элементов, которые <50, и среднее значение всех элементов, кото-рые ≥50.
import random

print("Массив: ")

N = random.randint(1, 10)
array = [0] * N

for index in range(N):
    array[index] = random.randint(0, 100)



count1 = 0
count2 = 0
summ1 = 0
summ2 = 0


for jj in array:
    if 0 <= jj < 50:
        count1 += 1
        summ1 += jj
    elif 100 > jj >= 50:
        count2 += 1
        summ2 += jj


print(array)
print(f"Средне арифметическое элементов [0, 50): {summ1/count1}")
print(f"Средне арифметическое элементов [50, 100): {summ2/count2}")


#Я не очень понял должно ли 100 входить в диапозон потому что при выводе на экран там круглые скобки а в условии квадратные,
#я решил не брать 100 во втором случае
