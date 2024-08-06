import sys
input = sys.stdin.readline

n = int(input())
ans_cnt = 0
wrong_cnt = 0
ans = {}
for _ in range(n):
    a = input().strip().split()
    if a[1] not in ans and a[1] != 'megalusion':
        ans[a[1]] = []
        ans[a[1]].append(a[2])
    elif a[1] in ans:
        ans[a[1]].append(a[2])
for i in ans:
    for j in ans[i]:
        if '4' not in ans[i]:
            continue
        else:
            if j != '4':
                wrong_cnt += 1
            else:
                ans_cnt += 1
                break
try:
    print(ans_cnt/(ans_cnt+wrong_cnt) * 100)
except:
    print(0)