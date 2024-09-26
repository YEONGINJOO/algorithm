import sys
input = sys.stdin.readline

while True:
    a = input().strip()
    if a == '#':
        break
    A_cnt = 0
    B_cnt = 0
    A_score = 0
    B_score = 0
    for i in range(len(a)):
        if a[i] == 'A':
            A_cnt += 1
        else:
            B_cnt += 1
        if A_cnt - B_cnt >= 2 and A_cnt >= 4:
            A_score += 1
            A_cnt = 0
            B_cnt =0
        elif B_cnt - A_cnt >= 2 and B_cnt >=4:
            B_score += 1
            A_cnt = 0
            B_cnt = 0
    print(f'A {A_score} B {B_score}')