import sys
input = sys.stdin.read
data = input().splitlines()  # 입력받은 내용을 줄 단위로 분리

dir = data[0]  # 진행 방향
# 해당 방향에서 바라보는 기준으로 문자열을 저장
name = ["T", "F", "Lz"]
T = ['.', 'O', 'P', '.']
F = ['I', '.', '.', 'P']
Lz = ['O', '.', '.', 'P']
    
check = [False] * 3  # 점프 계열 체크
    
# 2x2 격자 입력받기
u = list(data[1])
d = list(data[2])
    
# 방향에 따라 격자 변환
if dir == "E":  # 동쪽
    j = [d[0], u[0], d[1], u[1]]
elif dir == "W":  # 서쪽
    j = [u[1], d[1], u[0], d[0]]
elif dir == "S":  # 남쪽
    j = [u[0], u[1], d[0], d[1]]
elif dir == "N":  # 북쪽
    j = [d[1], d[0], u[1], u[0]]
    
# 각각의 점프 계열마다 체크
for i in range(4):
    if not check[0] and j[i] != T[i]:
        check[0] = True
            
    if not check[1] and j[i] != F[i]:
        check[1] = True
            
    if not check[2] and j[i] != Lz[i]:
        check[2] = True
    
# 일치하는 점프가 있다면 출력
sb = ""
for i in range(3):
    if not check[i]:
        sb = name[i]
        break
            
# 일치하는 점프가 없다면 ? 출력
if not sb:
    sb = "?"
    
print(sb)