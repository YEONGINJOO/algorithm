import sys
input = sys.stdin.readline

def calculate_min_angle(h, m, s):
    # 시침, 분침, 초침 각도 계산
    hour_angle = (h % 12) * 30 + (m / 60) * 30 + (s / 3600) * 30
    minute_angle = (m % 60) * 6 + (s / 60) * 6
    second_angle = (s % 60) * 6

    # 세 각도 리스트
    angles = [hour_angle, minute_angle, second_angle]

    # 두 각도 간의 최소 각도 계산
    min_angle = float('inf')
    for i in range(3):
        for j in range(i + 1, 3):
            angle_diff = abs(angles[i] - angles[j])
            min_angle = min(min_angle, angle_diff, 360 - angle_diff)

    return min_angle

T = int(input())
for _ in range(T):
    h, m, s = map(int, input().split())
    min_angle = calculate_min_angle(h, m, s)
    print(f"{min_angle:.6f}")