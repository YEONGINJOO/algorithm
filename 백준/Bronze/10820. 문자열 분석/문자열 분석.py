import sys
input = sys.stdin.readline
num = '0123456789'
lowalpha = 'abcdefghijklmnopqrstuvwxyz'
upalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    try:
        a = input()
        if a == '':
            break
        a = a[:-1]
        d_cnt = u_cnt = num_cnt = spa_cnt = 0
        for i in a:
            if i == ' ':
                spa_cnt += 1
            elif i in lowalpha:
                d_cnt += 1
            elif i in upalpha:
                u_cnt += 1
            else:
                num_cnt += 1
        print(d_cnt, u_cnt, num_cnt, spa_cnt)
    except EOFError:
        break