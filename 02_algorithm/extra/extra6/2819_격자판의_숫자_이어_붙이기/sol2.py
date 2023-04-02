import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, rlt, x, y):
    if i == 6:
        result.add(rlt)
        return

    else:
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(i+1,rlt * 10 + arr[nx][ny], nx, ny)

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(0, arr[i][j], i, j)

    print(len(result))