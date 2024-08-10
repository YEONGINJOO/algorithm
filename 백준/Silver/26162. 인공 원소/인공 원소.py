lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

n = int(input())
for _ in range(n):
    a = int(input())
    ans = 'No'
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i]+lst[j] == a:
                ans = 'Yes'
                break
        if ans == 'Yes':
            break
    print(ans)