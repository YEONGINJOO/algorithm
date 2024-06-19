import sys
input = sys.stdin.readline

a = input().strip()
cnt = 0
for i in range(len(a)-3):
    if a[i:+i+4] == 'DKSH':
        cnt += 1
print(cnt)