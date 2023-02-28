import sys
sys.stdin = open('input.txt')

asc = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]

    # 모든 세로 줄에 대해서
    for i in range(N):
        # 가로 줄에 대해서는 뒤에서 앞으로
        for j in range(M-1,-1,-1):
            if arr[i][j] == '0': continue
            tmp = []
            break
            for k in range(j - 56 + 1, j, 7):
                tmp.append(arr[i][k:k+7])
            print(tmp)
            odd_numbers = (asc[tmp[0]] + asc[tmp[2]] + asc[tmp[4]] + asc[tmp[6]])
            even_numbers = (asc[tmp[1]] + asc[tmp[3]] + asc[tmp[5]] + asc[tmp[7]])

            if (odd_numbers + even_numbers) % 10 == 0:
                result = odd_numbers + even_numbers
            else:
                result = 0
        print(result)