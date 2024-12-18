import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    p = int(input())
    mx = 0
    ans = ''
    for i in range(p):
        a = input().strip().split()
        if int(a[0]) > mx:
            mx = int(a[0])
            ans = a[1]
    print(ans)