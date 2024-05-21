a = input()
n = int(input())
cnt = 0
for _ in range(n):
    temp = input()
    for i in range(len(temp)):
        if i <= len(temp)-len(a):
            if temp[i:i+len(a)] == a:
                cnt += 1
                break
        else:
            sol = temp[i:] + temp[:len(a)-(len(temp)-i)]
            if sol == a:
                cnt += 1
                break
print(cnt)