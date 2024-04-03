def answer(lst):
    temp =[]
    for i in range(len(lst)-1):
        temp.append(lst[i+1]-lst[i])
    return temp

n, k = map(int, input().split())
lst = list(map(int, input().split(',')))
for i in range(k):
    lst = answer(lst)
print(*lst, sep=',')