from itertools import permutations
time = list(permutations(map(int,input().split(":"))))
count = 0
for h, m ,s in time :
    if 1<=h<=12 and 0<=m<=59 and 0<=s<=59 :
        count += 1
print(count)