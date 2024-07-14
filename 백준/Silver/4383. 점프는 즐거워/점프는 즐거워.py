import sys
input = sys.stdin.readline

while True:
    try:
        n, *lst = map(int, input().split())
        if n == 1:
            print('Jolly')
        else:
            arr = [0] * (n - 1)
            for i in range(n-1):
                dif = abs(lst[i]-lst[i+1])
                if 1 <= dif <= len(arr):
                    arr[dif-1] += 1
            if 0 in arr:
                print('Not jolly')
            else:
                print('Jolly')
    except:
        break