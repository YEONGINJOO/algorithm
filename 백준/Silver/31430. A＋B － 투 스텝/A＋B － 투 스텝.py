def main():
    T = int(input())  # 입력의 종류 (1: 갑, 2: 을)

    if T == 1:
        # Step 1: 갑의 입력 처리
        A, B = map(int, input().split())
        k = A + B

        # 13자리 문자열 초기화
        s = ['a'] * 13
        for i in range(13):
            if k > 0:
                s[i] = chr((k % 26) + ord('a'))  # 26진법에 따라 문자로 변환
                k //= 26
            else:
                break
        
        print(''.join(s))  # 리스트를 문자열로 변환하여 출력

    else:
        # Step 2: 을의 입력 처리
        s = input().strip()  # 문자열 입력받기
        ans = 0
        r = 1

        for i in range(len(s)):
            ans += (ord(s[i]) - ord('a')) * r  # 각 문자를 숫자로 변환
            r *= 26  # 26진법 자릿수 처리
        
        print(ans)  # A + B의 값 출력

if __name__ == "__main__":
    main()
