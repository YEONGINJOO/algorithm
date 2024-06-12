import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n != 0:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] += dp[i-1] + dp[i-2]
        print(dp[-2], dp[-1])
    else:
        print(1, 0)