import sys
input = sys.stdin.readline
n, k = map(int, input().split())
t = 0
m = 0
s = 0
cnt = 0
while True:
    if t == n and m == 59 and s == 59:
        if len(str(n)) == 1:
            d = '0' + str(n)
        else:
            d = str(n)
        if str(k) in d or str(k) in str(m) or str(k) in str(s):
            cnt += 1
        break
    if len(str(s)) == 1:
        a = '0' + str(s)
    else:
        a = str(s)
    if len(str(m)) == 1:
        b = '0' + str(m)
    else:
        b = str(m)
    if len(str(t)) == 1:
        c = '0' + str(t)
    else:
        c = str(t)
    if str(k) in a or str(k) in b or str(k) in c:
        cnt += 1
    s += 1
    if s > 59:
        s = 0
        m += 1
        if m > 59:
            m = 0
            t += 1
print(cnt)