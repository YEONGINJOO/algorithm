import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_lst = [0] * 10
for i in range(n, m+1):
    for j in str(i):
        num_lst[int(j)] += 1
print(*num_lst)