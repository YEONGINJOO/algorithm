import sys
input = sys.stdin.readline
N = int(input())
cy_cnt = 100
sd_cnt = 100
for _ in range(N):
    c, s = map(int, input().split())
    if c > s:
        sd_cnt -= c
    elif c < s:
        cy_cnt -= s
    else:
        continue
print(cy_cnt)
print(sd_cnt)