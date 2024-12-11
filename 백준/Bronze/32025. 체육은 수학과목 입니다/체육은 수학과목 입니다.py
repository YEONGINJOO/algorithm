import sys
input = sys.stdin.readline

h = int(input())
w = int(input())
if h > w:
    print(w * 100 // 2)
else:
    print(h * 100 // 2)