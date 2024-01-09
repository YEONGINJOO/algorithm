while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    doll_cnt = a - b
    if doll_cnt > 3:
        print(doll_cnt // 2 - doll_cnt % 2, doll_cnt % 2)
    elif doll_cnt == 3:
        print(0, 1)
    elif doll_cnt == 2:
        print(1, 0)
    else:
        print(0, 0)