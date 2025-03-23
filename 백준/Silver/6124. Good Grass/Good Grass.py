import sys
input = sys.stdin.readline
Nr, Nc = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Nr)]
mx = 0
ar, ac = 0, 0
for i in range(Nr-2):
    for j in range(Nc-2):
        sm = 0
        for k in range(3):
            sm += sum(arr[i+k][j:j+3])
        if sm > mx:
            mx = sm
            ar, ac = i+1, j+1
print(mx)
print(ar, ac)