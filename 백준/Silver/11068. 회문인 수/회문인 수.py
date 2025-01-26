import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a = int(input())
    ans = []
    for i in range(2, 65):
        li = []
        temp = a
        while temp != 0:
            li.append(temp%i)
            temp //= i
        for j in range(len(li)//2):
            if (li[j] != li[-1-j]):
                ans.append('X')
                break
    if len(ans) == 63:
        print(0)
    else:
        print(1)