N = int(input())
for i in range(N):
    lst = list(map(int, input().split()))
    h_cnt = 0
    j_cnt = 0
    for i in lst[1:]:
        if i % 2 == 0:
            j_cnt += i
        else:
            h_cnt += i
    if j_cnt > h_cnt:
        print('EVEN')
    elif j_cnt < h_cnt:
        print('ODD')
    else:
        print('TIE')