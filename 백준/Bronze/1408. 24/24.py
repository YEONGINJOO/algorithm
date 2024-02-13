a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
lst = [0] * 3
for j in range(3):
    lst[j] = b[j] - a[j]
if lst[2] < 0:
    lst[1] -= 1
    lst[2] += 60
if lst[1] < 0:
    lst[0] -= 1
    lst[1] += 60
if lst[0] < 0:
    lst[0] += 24
ans = ''
for i in range(3):
    if lst[i] < 10:
        ans += '0'+str(lst[i])+':'
    else:
        ans += str(lst[i])+':'
print(ans[:-1])