import sys
input = sys.stdin.readline
N, k = map(int, input().split())
lst = list(map(int, input().split()))
b = sorted(lst)
cnt = 0
ans = []

for last in range(N - 1, 0, -1):
    max_index = 0
    for i in range(1, last + 1):
        if lst[i] > lst[max_index]:
            max_index = i

    if last != max_index:
        lst[last], lst[max_index] = lst[max_index], lst[last]
        cnt += 1
        if cnt != k and lst == b:
            break
        elif cnt == k:
            ans.append(lst[max_index])
            ans.append(lst[last])
if ans == []:
    print(-1)
else:
    ans.sort()
    print(*ans)