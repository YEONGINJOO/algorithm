N = int(input())
for _ in range(N):
    lst = []
    a = int(input())
    for i in range(1, a+1):
        for j in range(1,a+1):
            if i + j == a and i != j and i < j:
                lst.append([i,j])
    print(f'Pairs for {a}:', end=' ')
    for k in range(len(lst)):
        print(*lst[k], end='')
        if k == len(lst) - 1:
            break
        print(', ', end='')
    print()