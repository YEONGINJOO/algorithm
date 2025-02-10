import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()

pages = 0
i = 0

while i < N:
    pages += 1
    price_limit = lst[i] * 2  # 현재 책 가격의 두 배
    while i < N and lst[i] < price_limit:
        i += 1  # 조건에 맞는 책들을 모두 포함

print(pages)