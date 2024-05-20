import sys
from fractions import Fraction

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
temp = 0
for i in range(n):
    temp += Fraction(1, lst[i])
mo = temp.numerator
ja = temp.denominator
print(f'{ja}/{mo}')