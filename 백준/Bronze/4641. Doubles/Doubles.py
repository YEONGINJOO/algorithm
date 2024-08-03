# bronze 1 double
while True:
    lst = list(map(int, input().split()))
    if len(lst) == 1 and lst[0] == -1:
        break
    cnt = 0
    for i in range(len(lst)-1):
        a = lst[i] * 2
        if a in lst:
            cnt += 1
    print(cnt)