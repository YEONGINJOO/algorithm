import sys
input = sys.stdin.readline


n, m = map(int, input().split())
pass_dic = {}
for _ in range(n):
    a, b = map(str, input().strip().split())
    pass_dic[a] = b
for i in range(m):
    c = input().strip()
    print(pass_dic[c])