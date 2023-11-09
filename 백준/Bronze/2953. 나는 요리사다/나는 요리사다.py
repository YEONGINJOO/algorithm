mx = 0
mx_idx = 0
for i in range(1, 6):
    a, b, c, d = map(int, input().split())
    sum_a = a + b + c + d
    if sum_a > mx:
        mx = sum_a
        mx_idx = i
print(mx_idx, mx)