import sys
input = sys.stdin.readline
def cowsort(lst):
    n = len(lst)
    if n <= 1:
        return lst, 0

    mid = n // 2
    left, left_distance = cowsort(lst[:mid])
    right, right_distance = cowsort(lst[mid:])

    total_distance = left_distance + right_distance

    if left > right:
        total_distance += (n ** 2) // 2
        return right + left, total_distance
    else:
        return left + right, total_distance


N = int(input())
arr = [int(input()) for _ in range(2 ** N)]

lst, total_distance = cowsort(arr)
print(total_distance)
for cow in lst:
    print(cow)