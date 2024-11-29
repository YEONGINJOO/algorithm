def min_button_presses(h, w, keyboard, target_string):
    # 키보드의 각 문자 위치를 기록
    position = {}
    for i in range(h):
        for j in range(w):
            char = keyboard[i][j]
            if char != '_':
                position[char] = (i, j)

    # 초기 위치
    current_position = (0, 0)
    total_presses = 0

    for char in target_string:
        target_position = position[char]
        # 이동 거리 계산
        distance = abs(current_position[0] - target_position[0]) + abs(current_position[1] - target_position[1])
        # 이동 거리 + OK 버튼 클릭 1회
        total_presses += distance + 1
        # 현재 위치 업데이트
        current_position = target_position

    return total_presses

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    keyboard = [input().strip() for _ in range(h)]
    target_string = input().strip()
    
    result = min_button_presses(h, w, keyboard, target_string)
    print(result)
