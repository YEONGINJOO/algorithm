n = input().strip()
a = int(n)
n = sorted(n, reverse=True)
ans = ''
for i in range(len(n)):
    ans += n[i]
if int(ans) % 30 != 0:
    print(-1)
else:
    print(int(ans))