time = list(map(int,input().split(":")))

def check(num):
    if num[0] >= 1 and num[0] <= 12:
        if num[1] >= 0 and num[1] <= 59:
            if num[2] >= 0 and num[2] <= 59:
                return True
    return False

count = 0
for i in range(3):
    for j in range(3):
        if j != i:
            for k in range(3):
                if k != i and k != j:
                    if check([time[i], time[j], time[k]]):
                        count += 1
print(count)