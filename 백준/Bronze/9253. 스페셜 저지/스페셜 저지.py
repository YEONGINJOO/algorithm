import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
ans = 'NO'
if c in a and c in b:
    ans = 'YES'
print(ans)