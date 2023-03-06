import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1], arr[N//2][N//2] = 2, 2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1
    for i in range(M):
        data = list(map(int,input().split()))
        arr[data[0]-1][data[1]-1] = data[2]

        if data[2] == 1:
            for j in range(8):
                for k in range(1,N):
                    nx = (data[0]-1) + dx[j] * k
                    ny = (data[1]-1) + dy[j] * k
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 2:
                            arr[nx][ny] = 1
                        elif arr[nx][ny] == 1:
                            break
        if data[2] == 2:
            for j in range(8):
                for k in range(1,N):
                    nx = (data[0]-1) + dx[j] * k
                    ny = (data[1]-1) + dy[j] * k
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 1:
                            arr[nx][ny] = 2
                        elif arr[nx][ny] == 2:
                            break
    for i in arr:
        print(i)

