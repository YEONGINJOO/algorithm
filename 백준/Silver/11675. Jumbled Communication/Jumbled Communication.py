import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    for j in range(256):  # 가능한 바이트 값 (0~255)
        if j ^ ((j << 1) & 255) == lst[i]:  # (j << 1) & 255: 8비트 유지
            print(j, end=" ")
            break