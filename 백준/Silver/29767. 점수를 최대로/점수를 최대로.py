import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0] * n
dp[0] = lst[0]
for i in range(1,n):
	dp[i] = dp[i-1] + lst[i]
dp.sort(reverse=True)
print(sum(dp[:k]))