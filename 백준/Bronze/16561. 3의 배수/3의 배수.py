import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        a = n - i * 3 - j * 3
        if a > 0 and a % 3 == 0:
            cnt += 1
print(cnt)