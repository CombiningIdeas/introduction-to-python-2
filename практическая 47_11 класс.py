
column = 5
line = 5
A = [[0] * column] * line

(x0, y0) = (1, 0)
color = A[x0][y0]

Q = [(x0, y0)]


while Q:
    x, y = Q.pop(0)
    if A[x][y] == color:
        A[x][y] = color
        if x > 0:
            Q.append((x-1, y))
        if x < column - 1:
            Q.append((x+1, y))
        if y > 0:
            Q.append((x, y-1))
        if y < line - 1:
            Q.append((x, y+1))