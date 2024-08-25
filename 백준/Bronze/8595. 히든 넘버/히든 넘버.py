import sys
input = sys.stdin.readline

n = int(input())
a = input().strip()
alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sm = 0
i = 0
while i < n:
    if a[i] not in alp:
        temp = a[i]
        for j in range(i+1, n):
            if a[j] not in alp:
                temp += a[j]
                i += 1
            else:
                i = j
                break
        sm += int(temp)
    i += 1
print(sm)