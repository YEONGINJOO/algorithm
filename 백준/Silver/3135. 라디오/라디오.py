A, B = map(int, input().split())
N = int(input())
lst = [int(input()) for _ in range(N)]
arr = []
for i in range(len(lst)):
    if lst[i] == B:
        arr.append(1)
        break
    if abs(B - lst[i]) < abs(A-B):
        arr.append(abs(B - lst[i])+1)
    else:
        arr.append(abs(A-B))
print(min(arr))