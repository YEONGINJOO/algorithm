import sys
input = sys.stdin.readline


from collections import deque

n = int(input())
de = deque()
for _ in range(n):
    a = input().strip()
    if a[0] == '1':
        de.appendleft(a[2:])
    elif a[0] == '2':
        de.append(a[2:])
    elif a[0] == '3':
        if len(de) == 0:
            print(-1)
        else:
            b = de.popleft()
            print(b)
    elif a[0] == '4':
        if len(de) == 0:
            print(-1)
        else:
            c = de.pop()
            print(c)
    elif a[0] == '5':
        print(len(de))
    elif a[0] == '6':
        if len(de) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == '7':
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])
    elif a[0] == '8':
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])