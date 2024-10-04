class TNode: pass

def node(d, L = None, R = None):
    newNode = TNode()#создаем новый узел
    newNode.data = d
    newNode.left = L
    newNode.right = R
    return newNode


#Обход дерева в глубину (обход КЛП) в виде рекурсивной процедуры:
def DFS(T):
    if not T:
        return
    print(T.data, end = " ")
    DFS(T.left)
    DFS(T.left)
    

#Такой же обход без рекусии использующий стек:
def DFS_stack(T):
    stack = [T]
    while stack:
        V = stack.pop()
        print(V.data, end = " ")
        if V.right:
            stack.append(V.right)
        if V.left:
            stack.append(V.left)


#Процедура обхода в ширину использующая очередб вместо стека:
def BTS(T):
    queue = [T]
    while queue:
        V = queue.pop(0)#берем первый элемент из очереди
        print(V.data, end=" ")
        if V.left:
            queue.append(V.left) 
        if V.right:
            queue.append(V.right)
        

def oper(op, n1, n2):
    if op == '+': return n1 + n2
    elif op == '-': return n1 - n2
    elif op == '*': return n1 * n2
    elif op == '/': return n1 // n2

#функция возвращаемая приоретет операции(для переданного ей символа):
def priority(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 100

def lastOp(s):
    minPrt = 50  #любое между 2 и 100
    k = -1
    for i in range(len(s)):
        if priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            k = i
    return k




def makeTree(s):
    k = lastOp(s)
    if k < 0:#создать лист
        Tree = node(s)
    else:#создать узел-операцию
        Tree = node(s[k])
        Tree.left = makeTree(s[:k:])
        Tree.right = makeTree(s[k+1::])
    return Tree


#Функция calcTree(вычисление арифметического выражения по дереву)
#тоже будет рекурсивной:
def calcTree(Tree):
    if not Tree.left:
        return int(Tree.data)
    else:
        n1 = calcTree(Tree.left)
        n2 = calcTree(Tree.right)
        return oper(Tree.data, n1, n2)
    


