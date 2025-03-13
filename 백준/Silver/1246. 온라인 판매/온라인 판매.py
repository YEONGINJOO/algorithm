import sys
input = sys.stdin.readline
N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]
P.sort()
cost = 0
mx = 0
for i in range(M):
    egg = min(N, M-i)
    temp = P[i] * egg
    if temp > mx:
        mx = temp
        cost = P[i]
print(cost, mx)