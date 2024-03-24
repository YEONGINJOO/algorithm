t = int(input())
for _ in range(t):
    x1,y1,x2,y2,x3,y3,p1,q1,p2,q2,p3,q3 = map(float, input().split())
    p1score = 0
    p2score = 0
    ans = 'TIE'
    p1_lst = [(x1**2+y1**2)**(1/2), (x2**2+y2**2)**(1/2), (x3**2+y3**2)**(1/2)]
    p2_lst = [(p1**2+q1**2)**(1/2),(p2**2+q2**2)**(1/2),(p3**2+q3**2)**(1/2)]
    for i in range(3):
        if p1_lst[i] > 15:
            pass
        elif p1_lst[i] == 15:
            p1score += 20
        elif p1_lst[i] > 12:
            p1score += 20
        elif p1_lst[i] == 12:
            p1score += 40
        elif p1_lst[i] > 9:
            p1score += 40
        elif p1_lst[i] == 9:
            p1score += 60
        elif p1_lst[i] > 6:
            p1score += 60
        elif p1_lst[i] == 6:
            p1score += 80
        elif p1_lst[i] > 3:
            p1score += 80
        elif p1_lst[i] <= 3:
            p1score += 100

        if p2_lst[i] > 15:
            pass
        elif p2_lst[i] == 15:
            p2score += 20
        elif p2_lst[i] > 12:
            p2score += 20
        elif p2_lst[i] == 12:
            p2score += 40
        elif p2_lst[i] > 9:
            p2score += 40
        elif p2_lst[i] == 9:
            p2score += 60
        elif p2_lst[i] > 6:
            p2score += 60
        elif p2_lst[i] == 6:
            p2score += 80
        elif p2_lst[i] > 3:
            p2score += 80
        elif p2_lst[i] <= 3:
            p2score += 100

    if p1score > p2score:
        ans = 'PLAYER 1 WINS'
    elif p1score < p2score:
        ans = 'PLAYER 2 WINS'

    print(f'SCORE: {p1score} to {p2score}, {ans}.')