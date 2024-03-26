lst = list(map(str, input().split('-')))
ans = ''
for i in lst:
    ans += i[0]
print(ans)