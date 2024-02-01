import sys
input = sys.stdin.readline
n = int(input())
score = 0
while n > 1:
    if n % 2 == 1:
        n = n * 3 + 1
        score += 1
    else:
        n = n // 2
        score += 1
print(score)