import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
    for i in range(N):
        for j in range(N):
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]

