
#Тест полякова по пайтону №43

'''
def F(n):
    print('*')
    if n > 0:
        F(n - 2)
        F(n // 2)


F(7)
'''

'''
def F( n ):
    print( '*' )
    if n > 0:
        F( n-2 )
        F( n // 2 )
        F( n // 2 )

F(5)
'''

'''
def F( n ):
    print( '*' )
    if n > 0:
        print( '*' )
        G(n - 1);

def G( n ):
    print( '*' )
    if n > 1:
        F( n - 2 )

F(12)
'''

k = 0

def F(n):
    if n > 2:
        return F(n - 1) + G(n - 2)
    else:
        return k = k + 1
def G(n):
    if n > 2:
        return G(n - 1) + F(n - 2)
    else:
        return k += 1


F(7)
print(k)
