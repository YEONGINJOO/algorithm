def min_cost_to_travel(N, distances, prices):
    total_cost = 0
    current_price = prices[0]
    
    for i in range(N - 1):
        # 현재 도시에서 다음 도시로 가기 위한 거리
        distance = distances[i]
        
        # 현재 도시의 기름 가격이 현재 가격보다 저렴한 경우
        if prices[i] < current_price:
            current_price = prices[i]
        
        # 이동 비용 계산
        total_cost += current_price * distance
    
    return total_cost

# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0].strip())
distances = list(map(int, data[1].strip().split()))
prices = list(map(int, data[2].strip().split()))

# 최소 비용 계산
result = min_cost_to_travel(N, distances, prices)

# 결과 출력
print(result)