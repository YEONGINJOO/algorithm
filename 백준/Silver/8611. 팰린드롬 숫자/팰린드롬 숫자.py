import sys
input = sys.stdin.readline

def jin(n, i):
    ans = ''
    while n > 0:
        n, mod = divmod(n, i)
        ans += str(mod)
    return ans[::-1]

n = int(input())
cnt = 0
for i in range(2, 11):
    a = jin(n, i)
    if a == a[::-1]:
        print(i, a)
        cnt += 1
if cnt == 0:
    print('NIE')