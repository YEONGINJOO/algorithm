import sys
input = sys.stdin.readline
a = input().strip()
n = int(input())
index_lst = []
for i in range(9):
    if a[i] == '*':
        index_lst.append(i)
cnt = 0
ans = []
for _ in range(n):
    s = input().strip()
    temp = ''
    for i in range(9):
        if i in index_lst:
            temp += '*'
        else:
            temp += s[i]
    if temp == a:
        cnt += 1
        ans.append(s)
print(cnt)
for j in range(len(ans)):
    print(ans[j])