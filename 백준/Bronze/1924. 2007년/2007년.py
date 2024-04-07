import sys
input = sys.stdin.readline
x, y = map(int, input().split())
mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
sm = y
ans = ''
for i in range(x):
    sm += mon[i]
if sm % 7 == 1:
    ans = 'MON'
elif sm % 7 == 2:
    ans = 'TUE'
elif sm % 7 == 3:
    ans = 'WED'
elif sm % 7 == 4:
    ans = 'THU'
elif sm % 7 == 5:
    ans = 'FRI'
elif sm % 7 == 6:
    ans = 'SAT'
elif sm % 7 == 0:
    ans = 'SUN'
print(ans)