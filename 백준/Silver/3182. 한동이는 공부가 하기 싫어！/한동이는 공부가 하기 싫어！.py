import sys
input = sys.stdin.readline
n = int(input())
lst = [[0,0]]
for k in range(n):
    a = int(input())
    lst.append([a, k+1])
arr = []
mx = 0
ans = -1
for i in range(1, n+1):
    temp = [lst[i]]
    j = lst[i][0]
    p = 0
    while p < n:
        if lst[j] not in temp:
            temp.append(lst[j])
        j = lst[j][0]
        p += 1
    arr.append(temp)
for i in range(n):
    if len(arr[i]) > mx:
        mx = len(arr[i])
        ans = i + 1
print(ans)