import sys
input = sys.stdin.readline

a, b = map(int, input().split())
str_a = str(a)
str_b = str(b)
ans = 0
for i in str_a:
    for j in str_b:
        ans += int(i)*int(j)
print(ans)