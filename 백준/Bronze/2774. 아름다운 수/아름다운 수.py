t = int(input())
for i in range(t):
    a = list(input())
    a.sort()
    cnt = 1
    if len(a) > 1:
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                cnt += 1
    print(cnt)