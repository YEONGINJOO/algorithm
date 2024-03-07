import sys
input = sys.stdin.readline
n = int(input())
s = ''
ans = 0
for i in range(1, n+1):
    s += str(i)
for i in range(len(s)-len(str(n))+1):
    temp = ''
    for j in range(len(str(n))):
        temp += s[i+j]
    if temp == str(n):
        ans = i
        break
print(ans+1)