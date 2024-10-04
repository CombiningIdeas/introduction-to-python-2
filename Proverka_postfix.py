data = input().split()
stack = []
for x in data:
    if x in "+-*/":
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        if x == '+': result = op1 + op2
        elif x == '-': result = op1 - op2
        elif x == '*': result = op1 * op2
        elif x == '/': result = op1 // op2
        stack.append(result)
    else:
        stack.append(x)
        
print(stack[0])