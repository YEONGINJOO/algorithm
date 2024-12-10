import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    jjak = []
    hol = []
    for j in lst:
        if j % 2 == 0:
            jjak.append(j)
        else:
            hol.append(j)
    hol.sort()
    jjak.sort(reverse=True)
    ans = ''
    for k in range(n):
        if lst[k] % 2 == 0:
            a = jjak.pop(0)
            ans += str(a)
        else:
            b = hol.pop(0)
            ans += str(b)
        ans += ' '
    print(f'Case #{i}: {ans[:-1]}')