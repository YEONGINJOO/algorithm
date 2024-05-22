t = int(input())
for _ in range(t):
    n = int(input())
    lst = [input() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        temp = lst[i]
        for j in range(i+1, n):
            sol = temp + lst[j]
            sol1 = lst[j] + temp
            if sol[::-1] == sol:
                ans = sol
                break
            if sol1[::-1] == sol1:
                ans = sol1
                break
    print(ans)