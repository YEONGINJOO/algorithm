import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
guest = []
cnt = 0
for i in range(n):
    if lst[i] in guest:
        continue
    else:
        guest.append(lst[i])
    if len(guest) != 0:
        for j in range(i, n):
            if i == j:
                continue
            else:
                if lst[i] == lst[j]:
                    cnt += 1
print(cnt)