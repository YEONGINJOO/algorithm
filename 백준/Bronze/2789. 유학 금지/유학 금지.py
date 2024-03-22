q = 'CAMBRIDGE'
a = input()
ans = ''
for i in a:
    if i not in q:
        ans += i
print(ans)