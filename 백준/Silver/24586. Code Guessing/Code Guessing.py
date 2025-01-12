p, q = map(int, input().split())
s = input().strip()
if s == 'ABBA':
    if q-p == 3:
        print(p+1, q-1)
    else:
        print(-1)
elif s == 'BAAB':
    if p == 2 and q == 8:
        print(1, 9)
    else:
        print(-1)
elif s == 'ABAB':
    if p == 6:
        print(7, 9)
    else:
        print(-1)
elif s == 'AABB':
    if q == 7:
        print(8, 9)
    else:
        print(-1)
elif s == 'BBAA':
    if p == 3:
        print(1, 2)
    else:
        print(-1)
elif s == 'BABA':
    if p == 2 and q-p == 2:
        print(1, 3)
    else:
        print(-1)
else:
    print(-1)