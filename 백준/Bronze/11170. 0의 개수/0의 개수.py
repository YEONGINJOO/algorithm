import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m+1):
        if '0' in str(i):
            cnt += str(i).count('0')
    print(cnt)
