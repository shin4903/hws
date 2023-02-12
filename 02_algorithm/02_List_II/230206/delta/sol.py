import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    for x in range(N):
        for y in range(N):
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < N and 0 <= ny < N:
                    result = result + abs(arr[x][y] - arr[nx][ny])
    print(f'#{tc}',result)