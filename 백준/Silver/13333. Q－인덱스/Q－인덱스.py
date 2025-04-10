import sys
input = sys.stdin.readline

n = int(input())
citations = list(map(int, input().split()))

def solve():
    q_index = 0
    for q in range(1, n + 1):
        count = 0
        for citation in citations:
            if citation >= q:
                count += 1
        if count >= q:
            q_index = q
    print(q_index)

solve()
