import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i+1,9):
        if sum(arr)-arr[i]-arr[j]==100:
            x,y=i,j
            break
arr.pop(x)
arr.pop(y-1)
for i in arr:
    print(i)