a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

A = a
if T > 30:
    A += x*(T-30)*21
B = b
if T > 45:
     B += y*(T-45)*21
print(A, B)