import sys
input = sys.stdin.readline
ans = 0
n = int(input())
for i in range(n):
    a = n-i
    if '4' in str(a) or '7' in str(a):
        if '1' not in str(a) and '2' not in str(a) and '3' not in str(a) and '5' not in str(a) and '6' not in str(a) and '8' not in str(a) and '9' not in str(a) and '0' not in str(a):
            ans = a
            break
print(ans)