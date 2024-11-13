import sys
input = sys.stdin.readline
resu = input().strip()
code = resu[:5]
n = int(input())
cnt = 0
for _ in range(n):
    a = input().strip()
    if code == a[:5]:
        cnt += 1
print(cnt)