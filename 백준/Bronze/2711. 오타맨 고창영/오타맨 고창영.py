t = int(input())
for _ in range(t):
    a, b = input().split()
    ans = ''
    for i in range(len(b)):
        if i == int(a)-1:
            continue
        else:
            ans += b[i]
    print(ans)