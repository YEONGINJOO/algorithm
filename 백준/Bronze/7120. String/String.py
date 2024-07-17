import sys
input = sys.stdin.readline

a = input().strip()
ans = ''
i = 0
while i < len(a):
    if ans == '':
        ans += a[i]
    else:
        if ans[-1] != a[i]:
            ans += a[i]
    i += 1
print(ans)