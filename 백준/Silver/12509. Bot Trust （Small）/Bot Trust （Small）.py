def main():
    t = int(input())
    for case_num in range(1, t + 1):
        parts = input().split()
        n = int(parts[0])
        commands = parts[1:]
        
        bat = oat = 1  # B, O 현재 위치
        btime = otime = 0  # B, O 완료 시간

        for i in range(n):
            c = commands[i * 2]
            next_pos = int(commands[i * 2 + 1])

            if c == 'B':
                btime = max(btime + abs(bat - next_pos), otime) + 1
                bat = next_pos
            else:  # 'O'
                otime = max(otime + abs(oat - next_pos), btime) + 1
                oat = next_pos

        print(f"Case #{case_num}: {max(btime, otime)}")

if __name__ == "__main__":
    main()
