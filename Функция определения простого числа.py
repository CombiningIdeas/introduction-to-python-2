#Логическая формула для определения простого числа

def isPrime(n):
    k = 2
    while k*k <= n and n % k != 0:
        k += 1
    return (k*k > n)
