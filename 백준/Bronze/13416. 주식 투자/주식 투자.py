import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if a > 0 or b > 0 or c > 0:
            cnt += max(a, b, c)
    print(cnt)
