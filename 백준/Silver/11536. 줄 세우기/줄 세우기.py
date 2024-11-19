import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]
sort_lst = sorted(lst)
rev_sort_lst = sorted(lst, reverse=True)
if lst == sort_lst:
    print('INCREASING')
elif lst == rev_sort_lst:
    print('DECREASING')
else:
    print('NEITHER')