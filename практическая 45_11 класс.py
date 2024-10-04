# Практическая работа № 45.	
# Скобочные выражения
# Уровень A.
# 1. Напишите программу, которая проверяет правильность скобочного выражения 
# с четырьмя видами скобок: (), [], {} и <>. 


# s = str(input())


# pairs = { '(' : ')', '[' : ']', '{' : '}'}

# def pair(c):
#     if c == '(': return ')'
#     elif c == '[': return ']'
#     elif c == '{': return '}'
#     else:
#         return '?'


# stack = []

# err = False

# for c in s:
#     if c in pairs:#проверка на открывающуюся скобку
#         #print(c)#открывающаяся скобках
#         #print(pairs[c])#закрывабщаяся скобках
#         #print(pairs.values())
#         stack.append(pairs[c])
#     elif c in pairs.values():#ищем символ среди закрывающихсяч скобок
#          if len(stack) == 0 or c != stack.pop():
#             err = True
#             break
        

# #доп проверка на закрытые и не закртые скобки
# if stack:
#     err = True
    
# if not err:
#     print("Выражение правильное.")
# else:
#     print("Выражение неправильное.")
    







# Уровень B.
# 2.Доработайте программу так, чтобы в случае ошибки она выводила номер первого 
# ошибочного символа

s = str(input())

pairs = { '(' : ')', '[' : ']', '{' : '}'}

def pair(c):
    if c == '(': return ')'
    elif c == '[': return ']'
    elif c == '{': return '}'
    else:
        return '?'

stack = []

err = False
error_simbol = -5#для проверки в конце ставим минус 5, а не 0, чтобы был верный приоритет
#ведь ошибка может стоять и на нулевом элементе а вот на минус 5, не может
counter = -1#отсчет идет с нуля, а не с 1
counter_stack_element = []

for c in s:
    counter += 1
    if c in pairs:#проверка на открывающуюся скобку
        #print(c)#открывающаяся скобках
        #print(pairs[c])#закрывабщаяся скобках
        #print(pairs.values())
        stack.append(pairs[c])
        counter_stack_element.append(counter)#чтобы можно было потом в строке s найти
    elif c in pairs.values():#ищем символ среди закрывающихсяч скобок
         if len(stack) == 0 or c != stack.pop():
            err = True
            #print(len(stack))
            #print(c)#проверяем символы, которые являются ошибочными
            error_simbol = counter
            break
         else:
             counter_stack_element.pop()
             

# этот случай должен быть в приоритете - ()[[[[{{]]]]]{} - неправильный порядок скобок
# этот случай после неправильного порядка уже рассматривается ([]({}( - отсуствие скобки

#доп проверка на закрытые и не закрытые скобки(тоесть отсуствие скобок)
if stack:
    err = True
    #эта проверка означает что проблем с порядком скобок нету, есть отсуствующие скобки
    if error_simbol == -5:
        error_simbol = counter_stack_element[0]#записываем первый ошибочный элемент 
    #стека, где и лежат эти значения, а это 0
    
if err == True:
    print("Номер первого ошибочного символа: ", error_simbol)
    
if not err:
    print("Выражение правильное.")
else:
    print("Выражение неправильное.")