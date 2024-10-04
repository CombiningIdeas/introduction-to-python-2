class TNode : pass
def node(d, L =None, R=None) :
    newNode = TNode()
    newNode.data = d
    newNode.left = L
    newNode.right = R
    return newNode


def DFS(T) :
    if not T :
        return
    print(T.data, end = " ")
    DFS(T.left)
    DFS(T.right)


def DFS_stack(T) :
    stack = [T]
    while stack :
        V = stack.pop()
        print(V.data, end=" ")
        if V.right :
            stack.append(V.right)
        if V.left :
            stack.append(V.left)


def BFS(T) :
    queue = [T]
    while queue :
        V = queue.pop(0)
        print(V.data, end=" ")
        if V.right :
            queue.append(V.right)
        if V.left :
            queue.append(V.left)




