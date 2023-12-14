T = int(input())
for _ in range(T):
    n = int(input())
    p1_cnt = 0
    p2_cnt = 0
    for i in range(n):
        p1, p2 = map(str, input().split())
        if p1 == 'R' and p2 == 'S':
            p1_cnt += 1
        elif p1 == 'R' and p2 == 'P':
            p2_cnt += 1
        elif p1 == 'P' and p2 == 'R':
            p1_cnt += 1
        elif p1 == 'P' and p2 == 'S':
            p2_cnt += 1
        elif p1 == 'S' and p2 == 'R':
            p2_cnt += 1
        elif p1 == 'S' and p2 == 'P':
            p1_cnt += 1
    if p1_cnt > p2_cnt:
        print('Player 1')
    elif p1_cnt == p2_cnt:
        print('TIE')
    else:
        print('Player 2')