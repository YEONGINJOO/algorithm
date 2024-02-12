import sys
input = sys.stdin.readline

n, q = map(int, input().split())
tlst = [int(input()) for _ in range(n)]
qlst = [int(input()) for _ in range(q)]

# 악보의 총 길이로 lst의 크기를 설정
lst = [0] * (sum(tlst) + 1)
k = 0
for i in range(n):
    if i != 0:
        k += tlst[i-1]
    for j in range(k, k + tlst[i]):
        # lst[j]는 j초에 부르는 악보 번호
        lst[j] = i+1

for n in range(q):
    print(lst[qlst[n]])