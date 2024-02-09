n = int(input())
lst = list(map(int, input().split()))
c = int(input())
cnt = 0
for i in range(n):
    if lst[i] == 0:
        continue
    elif 1 > lst[i] / c > 0:
        cnt += 1
    else:
        if lst[i] % c == 0:
            cnt += lst[i] // c
        else:
            cnt += 1 + lst[i] // c
print(cnt * c)