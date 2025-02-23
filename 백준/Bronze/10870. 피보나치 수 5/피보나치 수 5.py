import sys
input = sys.stdin.readline

n = int(input())
fibo = [0] * (n+1)
if n <= 1:
    print(n)
else:
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    print(fibo[n])