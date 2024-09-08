import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(2**i)

n = int(input())
suyeol = [i for i in range(8)]
lst = list(map(int, input().split()))
K = int(input())
for i in range(n):
    flag = 0
    for j in range(9):
        for k in range(9):
            if arr[j] + arr[k] == lst[i]:
                suyeol[j], suyeol[k] = suyeol[k],suyeol[j]
                flag = 1
                break
        if flag == 1:
            flag = 0
            break
print(suyeol[K])