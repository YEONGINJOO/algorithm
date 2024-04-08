k = int(input())
a = input()
lst = []
for i in range(0, len(a), k):
    lst.append(a[i:i+k])
ans = ''
for i in range(k):
    for j in range(len(lst)):
        if j % 2 != 0:
            ans += lst[j][::-1][i]
        else:
            ans += lst[j][i]
print(ans)