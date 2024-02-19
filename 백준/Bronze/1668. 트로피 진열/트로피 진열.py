import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
left_lst = lst
right_lst = lst[::-1]
left = 1
right = 1
for i in range(n-1):
    if left_lst[i] < left_lst[i+1]:
        left += 1
    else:
        left_lst[i+1] = left_lst[i]
    if right_lst[i] < right_lst[i+1]:
        right += 1
    else:
        right_lst[i+1] = right_lst[i]
print(left)
print(right)