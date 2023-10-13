import sys
input = sys.stdin.readline
N = int(input())
cute_cnt = 0
nocute_cnt = 0
for _ in range(N):
    x = int(input())
    if x == 1:
        cute_cnt +=1
    else:
        nocute_cnt += 1
if cute_cnt > nocute_cnt:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')