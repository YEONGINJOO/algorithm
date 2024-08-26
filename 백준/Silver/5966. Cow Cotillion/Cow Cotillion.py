import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().strip().split()
    stack = []
    for i in range(int(a)):
        if b[i] == '>':
            stack.append(b[i])
        elif b[i] == '<':
            if stack == []:
                stack.append(b[i])
            elif stack[-1] == '>':
                stack.pop()
            else:
                stack.append(b[i])
    if stack == []:
        print('legal')
    else:
        print('illegal')
