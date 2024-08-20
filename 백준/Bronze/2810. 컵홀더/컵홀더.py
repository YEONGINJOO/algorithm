import sys
input = sys.stdin.readline
n = int(input())
a = input().strip()
if 'L' not in a:
    print(n)
else:
    temp = '*'
    i = 0
    while i < n:
        if a[i] == 'S':
            temp += a[i]
            temp += '*'
            i += 1
        else:
            if a[i+1] == 'L':
                temp += a[i] + a[i]
                temp += '*'
                i += 2
    print(temp.count('*'))