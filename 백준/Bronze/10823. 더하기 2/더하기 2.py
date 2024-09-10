import sys
input = sys.stdin.readline
S = ''
while True:
    s = input().strip()
    if s == '':
        break
    S += s
a = S.split(',')
ans = 0
for i in a:
    ans += int(i)
print(ans)
