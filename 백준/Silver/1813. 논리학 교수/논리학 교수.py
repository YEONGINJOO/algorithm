import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

ans = -1

for j in range(n+1):
	cnt = lst.count(j)
	if cnt == j:
		ans = max(ans, j)
print(ans)