N, K, A, B = map(int, input().split())
lst = [K] * N
cnt = 0
node = 0
while 0 not in lst:
    for i in range(A):
        lst[node + i] += B
    if node + A > N - 1:
        node = 0
    else:
        node += A
    for j in range(N):
        lst[j] -= 1
    cnt += 1
print(cnt)