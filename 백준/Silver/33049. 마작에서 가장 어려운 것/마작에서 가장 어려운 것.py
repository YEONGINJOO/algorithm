P3, P4, P0 = map(int, input().split())

for i in range(P0 + 1):
    if (P3 + i) % 3 == 0 and (P4 + P0 - i) % 4 == 0:
        print((P3 + i) // 3, (P4 + P0 - i) // 4)
        break
else:
    print(-1)