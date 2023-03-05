import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = []
    for _ in range(N):  # ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색
        data.append(input())
    result = N * M

    W = 0
    for i in range(N - 2):
        W += (M - data[i].count('W'))
        B = 0
        for j in range(i + 1, N - 1):
            B += (M - data[j].count('B'))
            R = 0
            for k in range(j + 1, N):
                R += (M - data[k].count('R'))
            if W + B + R < result:
                result = W + B + R
    print(f'#{tc}',result)
