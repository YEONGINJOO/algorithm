a = input()
ans = ''
i = 0
while i < len(a):
    ans += a[i]
    if a[i] in 'aeiou':
        i += 2
    i += 1
print(ans)