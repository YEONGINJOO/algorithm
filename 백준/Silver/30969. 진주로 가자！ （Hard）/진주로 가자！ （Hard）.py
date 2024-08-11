import sys
input = sys.stdin.readline

n = int(input())
jinju_cost = 0
cnt = 0
lst = [0] * 1001
for _ in range(n):
    d, c = input().strip().split()
    c = int(c)
    if d == 'jinju':
        jinju_cost = c
    elif c > 1000:
        cnt += 1
    else:
        lst[c] += 1
for i in range(jinju_cost+1, 1001):
    cnt += lst[i]

print(jinju_cost)
print(cnt)