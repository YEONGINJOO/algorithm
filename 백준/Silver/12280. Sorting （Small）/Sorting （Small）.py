import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    hol = []
    jjak = []
    for j in range(n):
        if lst[j] % 2 == 0:
            jjak.append(lst[j])
        else:
            hol.append(lst[j])
    hol.sort()
    jjak.sort(reverse=True)
    ans = ''
    for k in range(n):
        if lst[k] % 2 == 0:
            ans += str(jjak[0])
            ans += ' '
            jjak.pop(0)
        else:
            ans += str(hol[0])
            ans += ' '
            hol.pop(0)
    print(f'Case #{i}: {ans[:-1]}')