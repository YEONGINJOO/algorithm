def min_button_presses(current_time, correct_time):
    # 현재 시간과 목표 시간을 시(hour)와 분(minute)으로 분리합니다.
    current_hour, current_minute = map(int, current_time.split(':'))
    correct_hour, correct_minute = map(int, correct_time.split(':'))

    # 현재 시간과 목표 시간을 총 분 단위로 변환합니다.
    current_total_minutes = current_hour * 60 + current_minute
    correct_total_minutes = correct_hour * 60 + correct_minute

    # 목표 시간이 현재 시간보다 작을 경우, 하루를 더해서 계산합니다.
    if correct_total_minutes < current_total_minutes:
        correct_total_minutes += 24 * 60

    # 총 차이 분을 계산합니다.
    difference = correct_total_minutes - current_total_minutes

    # 버튼 B (1시간 = 60분)와 버튼 A (1분)을 사용하여 최소한의 조작 횟수를 계산합니다.
    button_b_presses = difference // 60
    button_a_presses = difference % 60

    return button_b_presses + button_a_presses

# 입력을 받습니다.
current_time = input().strip()
correct_time = input().strip()

# 최소한의 버튼 조작 횟수를 출력합니다.
print(min_button_presses(current_time, correct_time))