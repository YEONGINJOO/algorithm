import sys
input = sys.stdin.readline
n = int(input())
a = [input().strip().split(',') for _ in range(n)]
arr = []
for i in range(n):
    temp = []
    for j in range(len(a[i])):
        if '"name"' in a[i][j]:
            tem1 = a[i][j].split(':')
            temp.append(tem1)
        if '"score"' in a[i][j]:
            tem2 = a[i][j].split(':')
            temp.append(tem2)
        if '"isHidden"' in a[i][j]:
            tem3 = a[i][j].split(':')
            temp.append(tem3)
    arr.append(temp)

arr.sort(key=lambda x: (-int(x[1][1]), x[0][1][1:-1]))
i = 0
while i < len(arr):
    arr[i].append(i+1)
    for j in range(i+1, len(arr)):
        if arr[i][1][1] == arr[j][1][1]:
            arr[j].append(i+1)
        else:
            i = j
            break
    else:
        i += 1

for k in range(len(arr)):
    if '0' in arr[k][2][1]:
        print(f'{arr[k][3]} {arr[k][0][1][1:-1]} {arr[k][1][1]}')