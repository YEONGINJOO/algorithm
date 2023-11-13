'''
1 = 1 + 2
2 = 1 + 2 + 2 + 3 + 4
3 = 1 + 2 + 2 + 3 + 4 + 3 + 4 + 5 + 6 = 30
4 = 18 + 3 + 4 + 5 + 6 
15 * 68 * 2 = 2040 
'''
n = int(input())
cnt = 0
for i in range(1, n+1):
    for j in range(i, 2*i+1):
        cnt += j
print(cnt)