import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    m = int(input())
    lst = [input().strip() for _ in range(m)]
    n = int(input())
    arr = []
    for _ in range(n):
        a, *arr1 = map(int, input().split())
        arr.append(arr1)
    ans = []
    for j in range(n):
        temp = ''
        for k in range(len(arr[j])):
            temp += lst[arr[j][k]]
        ans.append(temp)


    print(f'Scenario #{i+1}:')
    for l in ans:
        print(l)
    print()