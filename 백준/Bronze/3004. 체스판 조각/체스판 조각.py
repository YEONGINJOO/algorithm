N = int(input())
a = 1
ans = 1
for i in range(N):
    if i % 2 != 0:
        a += 1
    ans += a
print(ans)