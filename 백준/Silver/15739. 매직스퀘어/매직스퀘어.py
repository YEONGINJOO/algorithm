import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

t_sm = n * (n**2 + 1) // 2

d_sm1 = 0
d_sm2 = 0
lst = []
b = set()
for i in range(n):
    d_sm1 += arr[i][i]
    d_sm2 += arr[i][n-1-i]
    rsm = sum(arr[i][:])
    csm = 0
    for j in range(n):
        csm += arr[j][i]
        b.add(arr[i][j])
    lst.append(csm)
    lst.append(rsm)
lst.append(d_sm2)
lst.append(d_sm1)
a = set(lst)
if len(a) != 1 or t_sm not in a or len(b) != n**2:
    print('FALSE')
else:
    print('TRUE')