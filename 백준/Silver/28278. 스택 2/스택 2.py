import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    a = input().strip().split()
    if a[0] == '1':
        stack.append(int(a[1]))
    elif a[0] == '2':
        if stack != []:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == '3':
        print(len(stack))
    elif a[0] == '4':
        if stack == []:
            print(1)
        else:
            print(0)
    elif a[0] == '5':
        if stack != []:
            print(stack[-1])
        else:
            print(-1)