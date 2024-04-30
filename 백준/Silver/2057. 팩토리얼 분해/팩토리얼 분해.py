n = int(input())

fact = [1, 1]
for i in range(2, 21):
    fact.append(fact[i-1]*i)

sm = 0

for i in range(20, -1, -1):
    if sm+fact[i] < n:
        sm += fact[i]
    elif sm+fact[i] == n:
        print("YES")
        exit(0)

print("NO")