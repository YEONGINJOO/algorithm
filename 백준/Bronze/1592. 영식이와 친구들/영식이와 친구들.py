n, m, l = map(int, input().split())
lst = [0] * n
cnt = 0
lst[0] = 1
i = 0
while m not in lst:
    if lst[i] % 2 == 1:
        i = (i + l) % n
    else:  
        i = (i - l) % n  
    lst[i] += 1
    cnt += 1
print(cnt)