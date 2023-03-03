import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    maxV = 0
    for x in range(N):
        for y in range(M):
            result = arr[x][y]
            for i in range(4):
                for j in range(1,M):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                    if 0 <= nx < N and 0 <= ny < N:
                        result += arr[nx][ny]

            if result > maxV:
                maxV = result

    for x in range(N):
        for y in range(M):
            result = arr[x][y]
            for i in range(4,8):
                for j in range(1, M):
                    nx = x + dx[i]*j
                    ny = y + dy[i]*j
                if 0 <= nx < N and 0 <= ny < N:
                    result += arr[nx][ny]

            if result > maxV:
                maxV = result
    print(maxV)