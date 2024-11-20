import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n+1):
    if '50' in str(i):
        cnt += 1
    cnt += 1
if '50' in str(n):
    cnt -= 1
print(cnt)