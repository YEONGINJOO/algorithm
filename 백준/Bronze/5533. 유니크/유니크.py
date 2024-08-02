# bronze 1 유니크
n = int(input())
arr = [[], [], []]
for _ in range(n):
    a, b, c = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
lst = [0] * n
for i in range(3):
    for j in range(n):
        flag = 0
        for l in range(n):
            if l != j:
                if arr[i][j] == arr[i][l]:
                    flag = 1
        if flag == 0:
            lst[j] += arr[i][j]
for k in range(n):
    print(lst[k])