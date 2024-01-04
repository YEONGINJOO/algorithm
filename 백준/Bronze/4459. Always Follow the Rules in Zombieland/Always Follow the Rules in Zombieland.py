q = int(input())
lst = []
for i in range(1,q+1):
    a = input()
    lst.append([i,a])
r = int(input())
for _ in range(r):
    s = int(input())
    for j in range(q):
        if lst[j][0] == s:
            ans = lst[j][1]
            break
        else:
            ans = 'No such rule'
    print(f'Rule {s}: {ans}')