import sys
input = sys.stdin.readline

while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == 0 and s1 == 0 and r0 == 0 and r1 == 0:
        break
    score_s = str(s0) + str(s1)
    status_s = 0
    score_r = str(r0) + str(r1)
    status_r = 0
    if score_s == '12' or score_s == '21':
        status_s = 2
    if score_r == '12' or score_r == '21':
        status_r = 2
    if int(score_s) % 11 == 0:
        status_s = 1
    if int(score_r) % 11 == 0:
        status_r = 1

    if status_s > status_r:
        ans = 'Player 1 wins.'
    elif status_s < status_r:
        ans = 'Player 2 wins.'
    else:
        if status_s == 2 and status_r == 2:
            ans = 'Tie.'
        elif max(int(score_s), int(score_s[::-1])) > max(int(score_r), int(score_r[::-1])):
            ans = 'Player 1 wins.'
        elif max(int(score_s), int(score_s[::-1])) < max(int(score_r), int(score_r[::-1])):
            ans = 'Player 2 wins.'
        else:
            ans = 'Tie.'
    print(ans)