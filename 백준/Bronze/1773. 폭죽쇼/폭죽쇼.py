import sys

n, c = map(int, sys.stdin.readline().split())
fireworks = [0] * (c+1)
count = 0

for _ in range(n):
    period = int(sys.stdin.readline())
    if fireworks[period] == 0:
        for j in range(period, c+1, period):
            if fireworks[j] == 0:
                fireworks[j] = 1
                count += 1

print(count)