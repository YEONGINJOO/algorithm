import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
	n = 4
else:
	n = n * 2
print(n)