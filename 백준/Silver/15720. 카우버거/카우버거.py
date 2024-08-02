import sys
input = sys.stdin.readline
b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
burger.sort(reverse=True)
side = list(map(int, input().split()))
side.sort(reverse=True)
umryo = list(map(int, input().split()))
umryo.sort(reverse=True)
ans = sum(burger)+sum(side)+sum(umryo)
ans1 = 0
for i in range(min(b, c, d)):
    a = burger[i]+side[i]+umryo[i]
    ans1 += a * 0.9
ans1 += sum(burger[min(b,c,d):]) + sum(side[min(b,c,d):]) + sum(umryo[min(b,c,d):])
print(ans)
print(int(ans1))