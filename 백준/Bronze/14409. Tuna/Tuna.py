import sys
input = sys.stdin.readline

n = int(input())
x = int(input())
ans = 0
for i in range(n):
    p1, p2 = map(int, input().split())
    if abs(p1-p2) > x:
        p3 = int(input())
        ans += p3
    elif p1 > p2:
        ans += p1
    else:
        ans += p2
print(ans)