N = int(input())
A = [0] * (N + 1)
values_set = set()
values_set.add(0)

for i in range(1, N + 1):
    next_value = A[i - 1] - i
    if next_value < 0 or next_value in values_set:
        A[i] = A[i - 1] + i
    else:
        A[i] = next_value
    values_set.add(A[i])

print(A[N])