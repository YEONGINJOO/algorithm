import math
import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
	n = int(input())
	lst = list(map(int, input().split()))
	ans = ''
	while n > 2:
		arr = []
		for j in range(math.ceil(n / 2)):
			if j < n - 1 - j:
				arr.append(lst[j]+lst[n-1-j])
			else:
				arr.append(lst[j]+lst[j])
		lst = arr
		n = len(lst)
		
	if lst[0] > lst[1]:
		ans = 'Alice'
	else:
		ans = 'Bob'
	print(f'Case #{i}: {ans}')