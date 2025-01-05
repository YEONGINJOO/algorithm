A = input()
B = input()
num = ''
for i in range(8):
    num += A[i]
    num += B[i]
while len(num) > 2:
    temp = ''
    for i in range(len(num)-1):
        if int(num[i]) + int(num[i+1]) >= 10:
            temp += str(int(num[i]) + int(num[i+1]))[1]
        else:
            temp += str(int(num[i]) + int(num[i+1]))
    num = temp
print(num)