while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    ans = 0
    for i in range(n):
        s, t = map(int, input().split())
        lst.append([s,t])
    for i in range(len(lst)):
        if i > 0:
            ans += lst[i][0] * (lst[i][1] - lst[i-1][1])
        else:
            ans += lst[i][0] * lst[i][1]
    print(ans, 'miles')