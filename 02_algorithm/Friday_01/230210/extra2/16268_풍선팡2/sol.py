import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    for x in range(N):
        for y in range(M):
            sum_num = 0
            sum_num += arr[x][y]
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < N and 0 <= ny < M:
                    sum_num += arr[nx][ny]
                if result < sum_num:
                    result = sum_num
    print(f'#{tc}', result)