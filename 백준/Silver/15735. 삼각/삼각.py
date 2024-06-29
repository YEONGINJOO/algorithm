import sys
input = sys.stdin.readline

def count_triangles(n):
    total_triangles = n* (n+2) *(2*n+1)//8
    return total_triangles

N = int(input())

print(count_triangles(N))