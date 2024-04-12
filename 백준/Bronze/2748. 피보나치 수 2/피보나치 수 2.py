def fi_bo(n):
    if n <= 1:
        return n
    fibo_cache = [0, 1] + [0] * (n - 1)
    for i in range(2, n+1):
        fibo_cache[i] = fibo_cache[i-1] + fibo_cache[i-2]
    return fibo_cache[n]

n = int(input())
print(fi_bo(n))