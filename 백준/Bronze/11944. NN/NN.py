import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n < m:
    for i in range(n):
        print(n, end='')
else:
    ans = ''
    for i in range(n):
        ans += str(n)
        if len(ans) >= m:
            break
    if len(ans) > m:
        print(ans[:m])
    else:
        print(ans)