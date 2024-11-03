import sys
input = sys.stdin.readline
import math

a, b = map(int, input().split(':'))
gcd_ab = math.gcd(a, b)
a = a // gcd_ab
b = b // gcd_ab
print(f'{a}:{b}')