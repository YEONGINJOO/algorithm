import sys
input = sys.stdin.readline
lst = []
while True:
    if lst and len(lst) == int(lst[0])+1:
        break
    a = input().strip().split()
    lst.extend(a)
del lst[0]
arr = []
for i in lst:
    k = i[::-1]
    arr.append(int(k))
arr.sort()
for j in arr:
    print(j)