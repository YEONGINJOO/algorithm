n = int(input())
arr = ['', '']
for j in range(n):
    if j % 2 == 0:
        arr[0]+='*'
    else:
        arr[0]+=' '
for k in range(n):
    if k % 2 == 0:
        arr[1]+=' '
    else:
        arr[1]+='*'
for i in range(n):
    for j in arr:
        if j == '':
            continue
        else:
            print(j)