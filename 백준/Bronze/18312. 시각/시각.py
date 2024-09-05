import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cnt = 0
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if len(str(hour)) == 1:
                a = '0' + str(hour)
            else:
                a = str(hour)
            if len(str(minute)) == 1:
                b = '0' + str(minute)
            else:
                b = str(minute)
            if len(str(second)) == 1:
                c = '0' + str(second)
            else:
                c = str(second)
            if str(k) in a + b + c:
                cnt += 1
print(cnt)