import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1 ,1]

def BFS(x,y):
    visited = [[0]*N for _ in range(N)]
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)

        if visited[x][y] == 0:
            visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                if maze[nx][ny] == 3:
                    return visited[x][y] - 1
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(f'#{tc}',BFS(i,j))