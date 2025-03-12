import sys
input = sys.stdin.readline
def train_boarding(N, L, P, passengers):
    # 각 차의 문 위치 계산
    door_positions = [(i * L + L // 2) for i in range(N)]
    
    max_distance = 0
    car_passenger_count = [0] * N

    for passenger in passengers:
        # 각 승객이 어느 차의 문으로 가는지 계산
        closest_car = -1
        closest_distance = float('inf')

        for i in range(N):
            # 현재 차의 문까지의 거리 계산
            door_position = door_positions[i]
            distance = abs(passenger - door_position)

            # 더 가까운 차를 찾거나, 거리가 같으면 높은 번호의 차 선택
            if distance < closest_distance or (distance == closest_distance and i > closest_car):
                closest_distance = distance
                closest_car = i

        # 최대 거리 갱신
        max_distance = max(max_distance, closest_distance)

        # 해당 차의 승객 수 증가
        car_passenger_count[closest_car] += 1

    # 최대 승객 수 계산
    max_passengers_in_car = max(car_passenger_count)

    return max_distance, max_passengers_in_car

# 입력 받기
N, L, P = map(int, input().split())
passengers = [int(input().strip()) for _ in range(P)]

# 함수 호출 및 결과 출력
max_distance, max_passengers_in_car = train_boarding(N, L, P, passengers)
print(max_distance)
print(max_passengers_in_car)