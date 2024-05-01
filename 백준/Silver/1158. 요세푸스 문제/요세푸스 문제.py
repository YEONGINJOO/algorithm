n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
arr = []
idx = 0
for i in range(1, n+1):
    idx += k-1
    if idx >= len(lst):
        idx %= len(lst)
    arr.append(lst.pop(idx))
print('<',end='')
for i in range(n):
    if i < n-1:
        print(arr[i], end=', ')
    else:
        print(arr[i], end='')
print('>', end='')