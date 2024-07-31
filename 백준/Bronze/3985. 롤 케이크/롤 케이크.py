import sys
input = sys.stdin.readline

l = int(input())
n = int(input())
arr = []
ans1 = 0
mx = 0
for i in range(n):
    p, k = map(int, input().split())
    if k-p+1 > mx:
        mx = k-p+1
        ans1 = i+1
    lst = []
    for j in range(p, k+1):
        lst.append(j)
    arr.append(lst)
cnt = [0] * n
for i in range(n):
    for e in range(len(arr[i])):
        for j in range(i+1, n):
            if arr[i][e] in arr[j]:
                arr[j].remove(arr[i][e])
mx2 = 0
ans2 = 0
for i in range(n):
    if len(arr[i]) > mx2:
        mx2 = len(arr[i])
        ans2 = i+1

print(ans1)
print(ans2)