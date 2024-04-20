n = int(input())
lst = [input().split() for _ in range(n)]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(n):
    lst[i][1] = int(lst[i][1])
    lst[i][2] = int(lst[i][2])
    lst[i][3] = int(lst[i][3])
arr= []
for j in range(n):
     arr.append(lst[j][1] + sum(month[:lst[j][2]]) + (lst[j][3]-1990) * 365 )
print(lst[arr.index(max(arr))][0])
print(lst[arr.index(min(arr))][0])