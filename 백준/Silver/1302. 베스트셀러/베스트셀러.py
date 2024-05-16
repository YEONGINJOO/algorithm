n = int(input())
lst = []
for _ in range(n):
    a = input()
    lst.append(a)
lst.sort()
mx = 0
ans = ''
for i in range(n):
    if lst.count(lst[i]) > mx:
        mx = lst.count(lst[i])
        ans = lst[i]
print(ans)