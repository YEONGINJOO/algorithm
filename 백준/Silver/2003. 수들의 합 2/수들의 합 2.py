import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

sm = a[0]
left = 0
right = 1
cnt = 0

while True:
    if sm < m:
        if right < n:
            sm += a[right]
            right += 1
        else:
            break
    elif sm == m:
        cnt += 1
        sm -= a[left]
        left += 1
    else:
        sm -= a[left]
        left += 1

print(cnt)