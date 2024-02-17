n = int(input())
k = 1
cnt = 0
while n > 0:
    n -= k
    k += 1
    cnt += 1
    if k > n:
        k = 1
print(cnt)