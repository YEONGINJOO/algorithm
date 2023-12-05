T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    arr = []
    for i in range(7):
        if lst[i] % 2 == 0:
            arr.append(lst[i])
    print(sum(arr), min(arr))