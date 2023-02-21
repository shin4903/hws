import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# def DFS(x,y):
#     global maze, visited, res
#     visited[x][y] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] != 1:
#             if maze[nx][ny] == 3:
#                 res = 1
#                 return
#             DFS(nx,ny)

# for tc in range(1,11):
#     T = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     visited = [[0] * 16 for _ in range(16)]
#     res = 0
#     DFS(1,1)
#     print(f'#{tc}',res)

def DFS_recur(x,y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] != 1:
            if maze[nx][ny] == 3:
                return 1
            return DFS_recur(nx,ny)
    return 0

for tc in range(1,11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    print(f'#{tc}',DFS_recur(1,1))




# def DFS(start):
#     # 첫 시작위치 방문
#     visited[start] = 1
#     if start == G:
#         return 1
#     for next in range(1, V + 1):
#         if data[start][next] and not visited[next]:
#             return DFS(next)
#     return 0


