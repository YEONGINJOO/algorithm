import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sm = sum(lst)
ans = 0
for i in range(n):
    sm -= lst[i]
    ans += lst[i] * sm
print(ans)