import sys
input = sys.stdin.readline

n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())
tcnt = 0
pcnt = 0
if s % t == 0:
    tcnt += s // t
else:
    tcnt += s // t + 1
if m % t == 0:
    tcnt += m // t
else:
    tcnt += m // t + 1
if l % t == 0:
    tcnt += l // t
else:
    tcnt += l // t + 1
if xl % t == 0:
    tcnt += xl // t
else:
    tcnt += xl // t + 1
if xxl % t == 0:
    tcnt += xxl // t
else:
    tcnt += xxl // t + 1
if xxxl % t == 0:
    tcnt += xxxl // t
else:
    tcnt += xxxl // t + 1
pcnt = n // p
pcnt_mod = n % p
print(tcnt)
print(pcnt, pcnt_mod)