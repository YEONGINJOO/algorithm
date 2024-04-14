def fibo(n):
    if n <= 1:
        return n
    fibo_temp =  [0, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        fibo_temp[i] = fibo_temp[i-1] + fibo_temp[i-2]
    return fibo_temp[n]

n = int(input())
print(fibo(n))