import sys
input = sys.stdin.readline
T = int(input())
for i in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = []
    j = 0
    while len(arr) < N:
        if lst[j] % 4 == 0:
            b = lst[j]
            a = (lst[j] // 4) * 3
            if a in lst:
                arr.append(a)
                lst.remove(a)
                lst.remove(b)
                j = 0
        j += 1
    print(f'Case #{i}:', *arr)