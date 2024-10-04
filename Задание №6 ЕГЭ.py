# #Здание №6 КИМ № 25030012

# from turtle import *

# screensize(10**4, 10**4)#увелечение размера рабочего поля
# tracer(0)#ускорение выполнения

# left(90)
# k = 30

# for ii in range(3):
#     right(45)
#     forward(10*k)
#     right(45)
    
# right(315)
# forward(10*k)

# for ii in range(2):
#     right(90)
#     forward(10*k)
  
# up()#поднимаем хвост у черепахи, чтобы лучше видеть точки
# #чтобы было видно точки:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#чтобы быстро рисовались точки
# exitonclick()#чтоб не закрывалось окно с черепахой

#forward - вперед
#up() - поднять хвост
#down() - опустить хвост



#КИМ № 25032504
#Задание №6

# from turtle import *

# screensize(10**4, 10**4)#увелечение размера рабочего поля
# tracer(0)#ускорение выполнения

# k = 30

# for ii in range(0, 2):
#     back(-8*k)
#     right(90)
#     forward(10*k)
#     right(90)

# up()

# forward(3*k)
# right(90)
# forward(7*k)
# left(90)

# down()

# for ii in range(0, 2):
#     forward(-12*k)
#     right(90)
#     back(-13*k)
#     right(90)
    

# up()#поднимаем хвост у черепахи, чтобы лучше видеть точки
# #чтобы было видно точки:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#чтобы быстро рисовались точки
# exitonclick()#чтоб не закрывалось окно с черепахой






#Прогноз 2024
#Задание №6(1)


# from turtle import *

# screensize(10**4, 10**4)#увелечение размера рабочего поля
# tracer(0)#ускорение выполнения

# k = 30

# for ii in range(0, 2):
#     forward(7*k)
#     right(90)
#     forward(18*k)
#     right(90)

# up()

# back(-2*k)
# right(90)
# forward(9*k)
# left(90)

# down()

# for ii in range(0, 2):
#     forward(8*k)
#     right(90)
#     forward(5*k)
#     right(90)
    

# up()#поднимаем хвост у черепахи, чтобы лучше видеть точки
# #чтобы было видно точки:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#чтобы быстро рисовались точки
# exitonclick()#чтоб не закрывалось окно с черепахой


#36

#print(294912/1024)


#print(210*8/120)




# КИМ№ 25048321

# from turtle import *

# screensize(10**4, 10**4)
# tracer(0)

# left(90)
# k = 30

# for ii in range(0, 2):
#     forward(10*k)
#     right(90)
#     forward(18*k)
#     right(90)
    
# up()

# forward(5*k)
# right(90)
# forward(14*k)
# left(90)

# down()

# for ii in range(0, 2):
#     forward(17*k)
#     right(90)
#     forward(7*k)
#     right(90)
    

# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, "green")
        

# exitonclick()


#Ответ: 30


# count = 0
# for ii in range(100000, 1000000):
#     if (ii % 2 == 0):
#         continue
#     else:
#         ii_str = str(ii)
#         if (ii_str[len(ii_str) - 1::] == 2) or (ii_str[len(ii_str) - 1::] == 3):
#             continue
#         else:
#             if (ii_str.count("1") < 2):
#                 continue
#             else:
#                 count += 1
# print(count)
#Ответ: 68004

k