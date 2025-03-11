import sys
input = sys.stdin.readline
n = int(input())
a = {}
lst = []
for _ in range(n):
    s = input().strip()
    sorted_word = ''.join(sorted(s))
    a[(s[0],s[-1],sorted_word)] = s

m = int(input())
arr = input().strip().split()
for i in range(m):
    if (arr[i][0], arr[i][-1], ''.join(sorted(arr[i]))) in a:
        arr[i] = a[(arr[i][0], arr[i][-1], ''.join(sorted(arr[i])))]
print(*arr)