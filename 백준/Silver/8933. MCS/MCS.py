from collections import defaultdict

def count_chars(s):
    count = [0] * 4
    for char in s:
        if char == 'A':
            count[0] += 1
        elif char == 'C':
            count[1] += 1
        elif char == 'G':
            count[2] += 1
        elif char == 'T':
            count[3] += 1
    return tuple(count)

def find_k_mcs(k, w):
    n = len(w)
    freq = defaultdict(int)
    
    # 초기 윈도우 설정
    current_window = w[:k]
    current_count = count_chars(current_window)
    freq[current_count] += 1
    
    # 슬라이딩 윈도우
    for i in range(1, n - k + 1):
        # 이전 윈도우의 첫 문자 제거
        if w[i-1] == 'A':
            current_count = (current_count[0] - 1, current_count[1], current_count[2], current_count[3])
        elif w[i-1] == 'C':
            current_count = (current_count[0], current_count[1] - 1, current_count[2], current_count[3])
        elif w[i-1] == 'G':
            current_count = (current_count[0], current_count[1], current_count[2] - 1, current_count[3])
        elif w[i-1] == 'T':
            current_count = (current_count[0], current_count[1], current_count[2], current_count[3] - 1)
        
        # 새로운 윈도우의 마지막 문자 추가
        if w[i + k - 1] == 'A':
            current_count = (current_count[0] + 1, current_count[1], current_count[2], current_count[3])
        elif w[i + k - 1] == 'C':
            current_count = (current_count[0], current_count[1] + 1, current_count[2], current_count[3])
        elif w[i + k - 1] == 'G':
            current_count = (current_count[0], current_count[1], current_count[2] + 1, current_count[3])
        elif w[i + k - 1] == 'T':
            current_count = (current_count[0], current_count[1], current_count[2], current_count[3] + 1)
        
        freq[current_count] += 1
    
    return max(freq.values())

def main():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    
    for _ in range(t):
        k, w = input().strip().split()
        k = int(k)
        result = find_k_mcs(k, w)
        print(result)

if __name__ == "__main__":
    main()