import sys

def main():
    input = sys.stdin.readline
    K = int(input())
    S = input().strip()
    
    n = []  # N의 개수를 세기 위한 스택
    s = []  # S의 개수를 세기 위한 스택
    v = []  # 각 그룹의 크기를 저장할 리스트
    flag = False  # N=True, S=False

    for char in S:
        if char == 'N':
            n.append(1)
            if not flag:
                v.append(len(s))  # 현재 S의 개수 저장
                s.clear()  # S 스택 초기화
            flag = True
        elif char == 'S':
            s.append(1)
            if flag:
                v.append(len(n))  # 현재 N의 개수 저장
                n.clear()  # N 스택 초기화
            flag = False

    if flag:
        v.append(len(n))  # 마지막 N의 개수 저장
    else:
        v.append(len(s))  # 마지막 S의 개수 저장

    v.append(0)  # 경계값 추가

    res = 0

    for i in range(1, len(v)):
        res = max(res, 2 * min(v[i - 1], v[i]))

    print(res)

if __name__ == "__main__":
    main()