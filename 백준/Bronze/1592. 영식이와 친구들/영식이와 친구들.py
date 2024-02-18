N, M, L = map(int, input().split())
cnt = 0
lst = [0] * N
lst[0] = 1
i = 0
while M not in lst:
    if lst[i] % 2 == 0:
        i = (i + L) % N
    else:
        i = (i - L) % N
    lst[i] += 1
    cnt += 1
print(cnt)