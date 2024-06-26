import sys
input = sys.stdin.readline

w, h = map(int, input().split())
width = w * h * (1/2)
print(f'{width:.1f}')