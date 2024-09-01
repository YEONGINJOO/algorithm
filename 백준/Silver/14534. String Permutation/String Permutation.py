import sys
input = sys.stdin.readline
import itertools
t = int(input())
for i in range(1, t+1):
    a = input().strip()
    lst = list((map(''.join, itertools.permutations(a))))
    print(f'Case # {i}:')
    for j in lst:
        print(j)