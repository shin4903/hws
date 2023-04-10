import sys
sys.stdin = open('input.txt')

import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    X = max(N,M)
    # K시간 지난 후 최대 크기 배열 생성
    data = [[0]*(X+K+1) for _ in range(X+K+1)]

    # 최대 크기 배열의 중앙에 arr넣기
    for i in range(N):
        for j in range(M):
            data[(X+K)//2 + i][(K+X)//2 + j] = arr[i][j]

    # 시간 측정을 위해 data를 복사해 두고 data와 tmp의 같은 위치의 좌표에 tmp의 값이 data의 2배가 되면 번식(data에), 3배가 되면 삭제(data에) , tmp는 +만 해줌
    tmp = copy.deepcopy(data)

    S = X + K

    # K -= 1 씩 해주면 for문을 돔
    while K:
        # tmp에 1시간씩 올려줌
        for i in range(S):
            for j in range(S):
                if data[i][j]:
                    tmp[i][j] += 1

        for i in range(S):
            for j in range(S):
                # tmp의 값이 data의 2배가 되면 활성화, 2배 + 1이 되면 번식
                if data[i][j] and tmp[i][j] == data[i][j] * 2 + 1:
                    # tmp는 놔두고 data를 지움(3배일 때 구현) / tmp도 data도 0이면 값 추가 / data와 tmp에 값이 다 있고 그 값이 같으면 (왜냐면 시간이 안지난 것이기 때문에 같이 같은 셀에 2개가 번식해서) data에 큰 값을 줌
                    for dir in range(4):
                        nx = i + dx[dir]
                        ny = j + dy[dir]
                        if data[nx][ny] == 0 and tmp[nx][ny] == 0:
                            data[nx][ny] = data[i][j]
                            tmp[nx][ny] = data[i][j]
                        elif data[nx][ny] and tmp[nx][ny] and data[nx][ny] == tmp[nx][ny]:
                            data[nx][ny] = max(data[nx][ny], data[i][j])
                            tmp[nx][ny] = max(data[nx][ny], data[i][j])

        for i in range(S):
            for j in range(S):
                if data[i][j] * 3 == tmp[i][j]:
                    data[i][j] = 0
        K -= 1
    result = 0

    for i in data:
        for j in i:
            if j:
                result += 1
    print(f'#{tc}',result)
