n = int(input())
lst = list(map(str, input().split()))
ans = lst[0][0]
for i in range(1, n):
    if len(lst[i-1]) > len(lst[i]):
        ans += ' '
    else:
        ans += lst[i][len(lst[i-1])-1]
print(ans)