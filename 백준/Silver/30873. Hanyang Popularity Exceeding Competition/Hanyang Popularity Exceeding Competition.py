import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
    p, c = map(int, input().split())
    if abs(p-cnt) <= c:
        cnt += 1
print(cnt)