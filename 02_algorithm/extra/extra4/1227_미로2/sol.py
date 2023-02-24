import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x,y):
    stack = [(x,y)]
    visited = [[0] * 100 for _ in range(100)]

    while stack:
        x, y = stack.pop()

        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] != 1 and not visited[nx][ny]:
                if arr[nx][ny] == 3:
                    return 1
                stack.append((nx,ny))
                visited[nx][ny] = 1
    return 0




for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(100)]
    stack = []
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                print(f'#{tc}',DFS(i,j))