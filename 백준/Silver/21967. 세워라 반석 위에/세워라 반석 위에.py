import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

max_len = 0
min_deque = deque()
max_deque = deque()
left = 0

for right in range(n):
    while min_deque and lst[min_deque[-1]] >= lst[right]:
        min_deque.pop()
    min_deque.append(right)
    
    while max_deque and lst[max_deque[-1]] <= lst[right]:
        max_deque.pop()
    max_deque.append(right)
    
    while lst[max_deque[0]] - lst[min_deque[0]] > 2:
        left += 1
        if min_deque[0] < left:
            min_deque.popleft()
        if max_deque[0] < left:
            max_deque.popleft()
    
    max_len = max(max_len, right - left + 1)

print(max_len)