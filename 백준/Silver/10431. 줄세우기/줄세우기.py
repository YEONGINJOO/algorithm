import sys
input = sys.stdin.readline
def solve(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                cnt += 1
    return cnt


p = int(input())
for _ in range(p):
    a, *lst = map(int, input().split())
    print(a, solve(lst))