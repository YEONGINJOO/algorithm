A, B, C = map(int, input().split())
if C % 2 == 1:
    ans = A ^ B
else:
    ans = A
print(ans)