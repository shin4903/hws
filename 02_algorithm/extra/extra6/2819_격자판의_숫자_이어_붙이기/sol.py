import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(n, rlt, ci, cj):
    global result
    if n == 6:
        result.add(rlt)
        return
    for di in range(4):
        ni = ci + dx[di]
        nj = cj + dy[di]
        if 0 <= ni < 4 and 0 <= nj < 4:
            DFS(n+1,rlt+arr[ni][nj],ni,nj)


T = int(input())

for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            DFS(0, arr[i][j], i, j)

    print(f'#{tc}',len(result))