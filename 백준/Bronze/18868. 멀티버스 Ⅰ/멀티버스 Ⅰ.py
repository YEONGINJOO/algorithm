import sys
input = sys.stdin.readline

m, n = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for i in range(m):
    univ_sort = sorted(universes[i])
    temp = []
    for j in universes[i]:
        temp.append(univ_sort.index(j)+1)
    universes[i] = temp

for i in range(m-1):
    for j in range(i+1, m):
        if universes[i] == universes[j]:
            cnt += 1
print(cnt)