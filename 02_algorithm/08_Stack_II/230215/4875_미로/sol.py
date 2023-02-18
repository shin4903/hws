import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def maze(x,y):
    stack = [(x,y)]
    visited = [[0] * N for _ in range(N)]
    while stack:
        x, y = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] != 1:
                if arr[nx][ny] == 3:
                    return 1
                visited[nx][ny] = 1
                stack.append((nx,ny))
    return 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                print(f'#{tc}' , maze(i,j))


