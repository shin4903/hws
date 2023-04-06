import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    visited = [[0]*N for _ in range(N)]
    q = [(x,y)]
    t = 1
    while q:
        x, y = q.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if tmp[nx][ny] < tmp[x][y]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif tmp[nx][ny] == tmp[x][y] and t:
                    t -= 1
                    tmp[nx][ny] -= K
                    visited[nx][ny] += visited[x][y] + 1
                    q.append((nx,ny))
    return visited
T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    q = []
    maxV = 0
    for i in range(N):
        for j in range(N):
            maxV = max(arr[i][j], maxV)
    for i in range(N):
        for j in range(N):
            tmp = arr[:]
            if arr[i][j] == maxV:
                print(arr[i][j])
                for k in bfs(i,j):
                    print(k)
                print()