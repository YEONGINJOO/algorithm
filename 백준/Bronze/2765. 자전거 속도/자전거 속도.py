i = 1
while True:
    a, b, c = map(float, input().split())
    if b == 0:
        break
    # 원주율
    pie = 3.1415927
    # 총 이동거리 인치 -> 마일로 5280, 12를 나눠준다.
    distance = a * pie * b / 5280 / 12

    MPH = round(distance / c * 3600, 2)


    print(f'Trip #{i}: {round(distance, 2):.2f} {MPH:.2f}')
    i += 1