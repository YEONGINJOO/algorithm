import sys
input = sys.stdin.readline
while True:
    a = input().strip().split()
    if a == ['#']:
        break
    b = set()
    for i in range(3):
        if a[1][i] == a[1][i+1]:
            b.add(a[1][i])
    b = sorted(b)
    if len(b) > 1:
        print(f'{b[0]} {b[0]} glued and {b[1]} {b[1]} glued')
    elif len(b) == 1:
        print(f'{b[0]} {b[0]} glued')
    else:
        continue