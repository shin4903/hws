import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    dx = [1, 0, 0]
    dy = [0, 1, -1]
    dir = 0
    for i in range(100):
        x, y = 0, i
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == 1:
            if ladder[nx][ny+1] == 1:
                ladder[nx][ny] = 0
                dir = 1
            elif ladder[nx][ny-1] == 1:
                ladder[nx][ny] = 0
                dir = 2
            elif ladder[nx+1][ny] == 1:
                ladder[nx][ny] = 0
                dir = 0
            x = nx
            y = ny
        if ladder[nx][ny] == 2:
            print(i)