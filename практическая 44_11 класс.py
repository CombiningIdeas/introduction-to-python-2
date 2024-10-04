#Практическая работа № 44.	
#Использование стека
#Уровень А.
#1.	Напишите программу, которая вычисляет с помощью стека значение 
#арифметического вы-ражения, записанного в постфиксной форме. 
#Выражение вводится с клавиатуры в виде символьной строки.


# data = input().split()
# stack = []
# for x in data:
#     if x in "+-*/":
#         op2 = float(stack.pop())
#         op1 = float(stack.pop())
#         if x == '+': result = op1 + op2
#         elif x == '-': result = op1 - op2
#         elif x == '*': result = op1 * op2
#         elif x == '/': result = op1 // op2
#         stack.append(result)
#     else:
#         stack.append(x)
# print(stack[0])




# # #Уровень B.
# # #2.	Напишите программу, которая вычисляет значение арифметического выражения, 
# # #записанного в префиксной форме. Выражение вводится с клавиатуры в виде 
# # #символьной строки.

# data = input().split()
# stack = []

# for x in reversed(data):
#     if x in "+-*/":
#         op2 = float(stack.pop())
#         op1 = float(stack.pop())
#         if x == "+":
#               result = op1 + op2
#         elif x == "-":
#               result = op1 - op2
#         elif x == "*":
#               result = op1 * op2
#         elif x == "/":
#               result = op1 / op2
#         stack.append(result)
#     else:
#          stack.append(x)


# print("Вывод:", stack[0])


