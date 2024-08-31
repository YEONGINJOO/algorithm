import sys
input = sys.stdin.readline
try:
    while True:
        n = int(input())
        ans = '1'
        while True:
            if int(ans) % n == 0:
                print(len(ans))
                break
            else:
                ans += '1'
except:
    exit()