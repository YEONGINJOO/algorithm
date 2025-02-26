import sys
input = sys.stdin.readline
N, W, H = map(int, input().split())
lst = [int(input()) for _ in range(N)]
a = (W**2 + H ** 2) ** (1/2)
for i in lst:
    if i <= a:
        print('YES')
    else:
        print('NO')