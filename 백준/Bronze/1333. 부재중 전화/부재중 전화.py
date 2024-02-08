N, L, D = map(int, input().split())

ring = D
while ring < N * (L + 5) - 5:  # 노래가 끝나는 시간 전까지
    if ring % (L + 5) < L:  # 노래가 재생되는 동안
        ring += D  # 다음 전화벨이 울리는 시간
    else:
        break

print(ring)
