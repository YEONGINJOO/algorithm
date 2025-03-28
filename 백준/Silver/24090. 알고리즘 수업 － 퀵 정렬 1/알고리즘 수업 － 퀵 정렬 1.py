import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e4))

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    global sw_cnt, k
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            sw_cnt += 1
            if sw_cnt == k:
                print(*sorted([A[i], A[j]]))
                sys.exit(0)
    if i + 1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        sw_cnt += 1
        if sw_cnt == k:
            print(*sorted([A[i+1], A[r]]))
            sys.exit(0)
    return i+1

n, k = map(int, input().split())
A = list(map(int, input().split()))

sw_cnt = 0
quick_sort(A, 0, n - 1)
print(-1)