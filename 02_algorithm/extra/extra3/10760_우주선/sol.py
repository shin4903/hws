import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    X, Y = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(X)]

    dx = [1, -1, 1, -1, 1, -1, 0, 0]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    count = 0
    for x in range(X):
        for y in range(Y):
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < X and 0 <= ny < Y and arr[nx][ny] < arr[x][y]:
                    cnt += 1
            if cnt >= 4:
                count += 1
    print(f'#{tc}', count)