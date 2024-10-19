N = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(N)]
tmp = []
if N % 2 == 0:
    for i in range(N):
        tmp.append(arr[i][N//2-1])
    tmp.sort()
    print(tmp[N//2-1])
else:
    for i in range(N):
        tmp.append(arr[i][N//2])
    tmp.sort()
    print(tmp[N//2])