n = int(input())
for _ in range(n):
    a = input().split()
    b = sorted(a[0])
    c = sorted(a[1])
    if b == c:
        print('Possible')
    else:
        print('Impossible')