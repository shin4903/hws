import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    visited = [[0]*16 for _ in range(16)]
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)

        if visited[x][y] == 0:
            visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and not visited[nx][ny]:
                if maze[nx][ny] == 3:
                    return 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return 0



for tc in range(1,11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{tc}',BFS(1,1))