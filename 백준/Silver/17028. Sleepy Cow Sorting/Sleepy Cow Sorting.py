import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(n-1, 0, -1):
    if lst[i-1] > lst[i]:
        ans = i
        break
print(ans)