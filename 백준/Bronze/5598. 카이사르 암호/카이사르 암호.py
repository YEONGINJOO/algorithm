a = {}
for i in range(65, 91):
    if i < 68:
        a[chr(i)] = chr(i+23)
    else:
        a[chr(i)] = chr(i - 3)
s = input().strip()
ans = ''
for i in s:
    ans += a[i]
print(ans)