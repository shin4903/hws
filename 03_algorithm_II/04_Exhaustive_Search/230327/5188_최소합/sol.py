import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0]
dy = [0, 1]
result = []
def BFS(x,y):
    q = [(x,y)]
    while q :
        x, y = q.pop(0)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))
                elif visited[x][y] + arr[nx][ny] <= visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + arr[nx][ny]
                        q.append((nx,ny))

    return
for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    q = []
    BFS(0,0)
    print(f'#{tc}',visited[N-1][N-1])


