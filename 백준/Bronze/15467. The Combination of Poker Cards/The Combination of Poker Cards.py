import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    lst = list(map(int, input().split()))
    set_lst = set(lst)
    arr = []
    for i in set_lst:
        arr.append([i,0])
    for j in range(6):
        for k in range(len(arr)):
            if lst[j] == arr[k][0]:
                arr[k][1] += 1
    arr.sort(key=lambda x:x[1])
    if len(arr) == 6:
        print('single')
    elif len(arr) == 5:
        print('one pair')
    elif len(arr) == 4:
        if arr[-1][1] == 2:
            print('two pairs')
        else:
            print('one triple')
    elif len(arr) == 3:
        if arr[-1][1] == 2:
            print('three pairs')
        elif arr[-1][1] == 4:
            print('tiki')
        else:
            print('full house')
    elif len(arr) == 2:
        if arr[-1][1] == 4:
            print('tiki pair')
        else:
            print('two triples')