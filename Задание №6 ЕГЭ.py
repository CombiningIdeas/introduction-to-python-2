# #������ �6 ��� � 25030012

# from turtle import *

# screensize(10**4, 10**4)#���������� ������� �������� ����
# tracer(0)#��������� ����������

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
  
# up()#��������� ����� � ��������, ����� ����� ������ �����
# #����� ���� ����� �����:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#����� ������ ���������� �����
# exitonclick()#���� �� ����������� ���� � ���������

#forward - ������
#up() - ������� �����
#down() - �������� �����



#��� � 25032504
#������� �6

# from turtle import *

# screensize(10**4, 10**4)#���������� ������� �������� ����
# tracer(0)#��������� ����������

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
    

# up()#��������� ����� � ��������, ����� ����� ������ �����
# #����� ���� ����� �����:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#����� ������ ���������� �����
# exitonclick()#���� �� ����������� ���� � ���������






#������� 2024
#������� �6(1)


# from turtle import *

# screensize(10**4, 10**4)#���������� ������� �������� ����
# tracer(0)#��������� ����������

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
    

# up()#��������� ����� � ��������, ����� ����� ������ �����
# #����� ���� ����� �����:
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k, y*k)
#         dot(5, 'green')

# update()#����� ������ ���������� �����
# exitonclick()#���� �� ����������� ���� � ���������


#36

#print(294912/1024)


#print(210*8/120)




# ��̹ 25048321

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


#�����: 30


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
#�����: 68004

k