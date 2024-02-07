import sys
input = sys.stdin.readline
N, m, M, T, R = map(int, input().split())
X = m
i = 0
t = 0
if X + T > M:
    t = -1
else:
    while i < N:
        t += 1
        if X + T <= M:
            X += T
            i += 1
        else:
            X -= R
            if X < m:
                X = m
print(t)