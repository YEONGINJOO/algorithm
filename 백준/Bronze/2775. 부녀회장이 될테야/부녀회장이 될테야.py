import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    ans = [i for i in range(1, n+1)] #0층의 1호부터 n호까지의 수
    for i in range(k):
        for j in range(1,n):
            ans[j] += ans[j-1]
    print(ans[-1])