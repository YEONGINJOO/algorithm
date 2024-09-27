import sys
input = sys.stdin.readline

def ghost_leg(n, rungs):
    permutation = list(range(1, n + 1))

    for rung in rungs:
        permutation[rung - 1], permutation[rung] = permutation[rung], permutation[rung - 1]
    return permutation


n, m = map(int, input().split())
rungs = [int(input()) for _ in range(m)]
result = ghost_leg(n,rungs)
for element in result:
    print(element)