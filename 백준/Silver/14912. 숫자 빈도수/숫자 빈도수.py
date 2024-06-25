import sys
input = sys.stdin.readline

n, d = map(str, input().split())
cnt = 0
for i in range(1, int(n)+1):
    for j in str(i):
        if j == d:
            cnt += 1
print(cnt)