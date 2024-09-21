import sys
input = sys.stdin.readline
dp = [0] * 2000
dp[1] = 1
dp[2] = 2
for i in range(3, 2000):
    dp[i] = dp[i-2] + dp[i-1]
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    cnt = 0

    for i in range(1, len(dp)):
        if dp[i] > b:
            break
        if dp[i] >= a and dp[i] <= b:
            cnt += 1
    print(cnt)