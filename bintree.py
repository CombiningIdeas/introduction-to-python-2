class TNode: pass

def node(d, L = None, R = None):
    newNode = TNode()#������� ����� ����
    newNode.data = d
    newNode.left = L
    newNode.right = R
    return newNode


#����� ������ � ������� (����� ���) � ���� ����������� ���������:
def DFS(T):
    if not T:
        return
    print(T.data, end = " ")
    DFS(T.left)
    DFS(T.left)
    

#����� �� ����� ��� ������� ������������ ����:
def DFS_stack(T):
    stack = [T]
    while stack:
        V = stack.pop()
        print(V.data, end = " ")
        if V.right:
            stack.append(V.right)
        if V.left:
            stack.append(V.left)


#��������� ������ � ������ ������������ ������� ������ �����:
def BTS(T):
    queue = [T]
    while queue:
        V = queue.pop(0)#����� ������ ������� �� �������
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

#������� ������������ ��������� ��������(��� ����������� �� �������):
def priority(op):
    if op in "+-": return 1
    if op in "*/": return 2
    return 100

def lastOp(s):
    minPrt = 50  #����� ����� 2 � 100
    k = -1
    for i in range(len(s)):
        if priority(s[i]) <= minPrt:
            minPrt = priority(s[i])
            k = i
    return k




def makeTree(s):
    k = lastOp(s)
    if k < 0:#������� ����
        Tree = node(s)
    else:#������� ����-��������
        Tree = node(s[k])
        Tree.left = makeTree(s[:k:])
        Tree.right = makeTree(s[k+1::])
    return Tree


#������� calcTree(���������� ��������������� ��������� �� ������)
#���� ����� �����������:
def calcTree(Tree):
    if not Tree.left:
        return int(Tree.data)
    else:
        n1 = calcTree(Tree.left)
        n2 = calcTree(Tree.right)
        return oper(Tree.data, n1, n2)
    


