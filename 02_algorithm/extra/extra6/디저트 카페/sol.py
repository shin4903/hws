import sys
sys.stdin = open('input.txt')

dx = [1, 1, -1, -1, 1]
dy = [-1, 1, 1, -1, -1]

def dfs(n, x, y, v):
    global result
    if n > 3:
        return
    if n == 3 and (i,j) == (x,y):
        result = max(result, len(v))
        return

    if n == 2 and len(v) * 2 <= result:
        return

    for k in range(n, n+2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in v:
            v.append(arr[nx][ny])
            dfs(k, nx, ny, v)
            v.pop()




T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = -1


    for i in range(N-2):
        for j in range(1, N-1):
            dfs(0,i,j,[])

    print(f'#{tc}', result)