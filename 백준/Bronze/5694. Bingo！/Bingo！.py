while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break
    pack = list(map(int, input().split()))
    lst = [0] * (n+1)
    for i in range(b):
        for j in range(b):
            lst[abs(pack[i]-pack[j])] += 1
    if 0 in lst:
        print('N')
    else:
        print('Y')