A, B = map(str,  input().split())
mn = int(A.replace('6', '5')) + int(B.replace('6','5'))
mx = int(A.replace('5', '6')) + int(B.replace('5','6'))
print(mn, mx)