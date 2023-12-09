N = int(input())
cnt = 0
for i in range(1, 100):
    for j in range(1, 100):
        if N - i - j == 0:
            cnt += 1
print(cnt)