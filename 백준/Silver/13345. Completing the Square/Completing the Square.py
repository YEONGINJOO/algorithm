import sys
input = sys.stdin.readline
lst = []
for i in range(3):
    x, y = map(int, input().split())
    lst.append([x, y])

line_1_2 = (lst[0][0] - lst[1][0]) ** 2  + (lst[0][1] - lst[1][1]) ** 2
line_2_3 = (lst[1][0] - lst[2][0]) ** 2  + (lst[1][1] - lst[2][1]) ** 2
line_3_1 = (lst[2][0] - lst[0][0]) ** 2  + (lst[2][1] - lst[0][1]) ** 2

min_point = []
center_point = []

if line_1_2 == line_2_3 :
    min_point = lst[1]
    center_point = [(lst[0][0] + lst[2][0])/2,(lst[0][1] + lst[2][1])/2]
elif line_2_3 == line_3_1 :
    min_point = lst[2]
    center_point = [(lst[0][0] + lst[1][0])/2,(lst[0][1] + lst[1][1])/2]
elif line_3_1 == line_1_2 :
    min_point = lst[0]
    center_point = [(lst[2][0] + lst[1][0]) / 2, (lst[2][1] + lst[1][1]) / 2]

target_point = [int(2*center_point[0]-min_point[0]) , int(2*center_point[1]-min_point[1])]

print(*target_point)