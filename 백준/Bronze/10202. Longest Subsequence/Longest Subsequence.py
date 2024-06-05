import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, *b = map(str, input().split())
    cnt = 0
    mx = 0
    for i in range(int(a)):
        if b[i-1] == 'X' and b[i] == 'X':
            cnt += 1
            if cnt > mx:
                mx = cnt
        elif b[i] == 'X':
            cnt += 1
            if cnt > mx:
                mx = cnt
        else:
            cnt = 0
    print(f"The longest contiguous subsequence of X's is of length {mx}")