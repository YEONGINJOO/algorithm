import math

n = int(input())  # 입력값 N
current_log = 0  # 로그 합계
results = []  # 조건을 만족하는 X 값들 저장

for i in range(1, 10**6):  # 적절한 범위 설정 (안전한 대략값으로 10^6까지 탐색)
    current_log += math.log10(i)
    # 현재 로그합의 자릿수가 N과 같으면 X를 저장
    if math.floor(current_log) + 1 == n:
        results.append(i)
    # 로그합의 자릿수가 N을 초과하면 종료
    elif math.floor(current_log) + 1 > n:
        break

# 출력
if results:
    print(len(results))  # 가능한 X의 개수
    print(*results)      # 모든 X를 출력
else:
    print("NO")