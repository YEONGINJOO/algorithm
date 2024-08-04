import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
lst = [[i, 0, 0] for i in range(r)]
for i in range(r):
    mxidx = 0
    for j in range(c):
        if arr[i][j] != '.' and arr[i][j] != 'F':
            if j > mxidx:
                mxidx = j
                lst[int(arr[i][j])][1] = mxidx
lst.sort(key=lambda x:x[1], reverse=True)

lst[0][2] = 1
for i in range(1, r-1):
    if lst[i][1] == lst[i-1][1]:
        lst[i][2] = lst[i-1][2]
    else:
        lst[i][2] = lst[i-1][2] + 1

lst.sort(key=lambda x:x[0])
for i in range(1, 10):
    print(lst[i][2])