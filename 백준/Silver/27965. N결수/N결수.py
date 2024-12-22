import sys
input = sys.stdin.readline
n, k = map(int,input().split())
temp = ''
for i in range(1, n+1):
    temp += str(i)
    a = int(temp) % k
    temp = str(a)
print(int(temp) % k)