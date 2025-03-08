import sys
input = sys.stdin.readline
N, T = map(int, input().split())
a = list(map(int,  input().split()))
cnt = 0
for i in range(N):
    if T % a[i] == 0:
        continue
    else:
        ah = a[i]
        cnth = 0
        al = a[i]
        cntl = 0
        while True:
            ah += 1
            al -= 1
            cnth += 1
            cntl += 1
            if T % ah == 0:
                cnt += cnth
                break
            elif T % al == 0:
                cnt += cntl
                break
print(cnt)