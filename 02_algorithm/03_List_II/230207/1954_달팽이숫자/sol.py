import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0

    # 시작 위치
    x = -1
    y = 0

    # 행렬 하나씩 순회
    for i in range(0, N ** 2):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # range를 벗어나거나 값이 채워진 곳을 만나면 방향을 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[ny][nx] != 0:
            # range(4)를 순회해야하므로 나머지를 활용
            # 벽만나면 새로 nx ny값 만들어야됨
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]

        arr[ny][nx] = i + 1
        x, y = nx, ny
    print(f'#{tc + 1}')
    for i in range(N):
        print(*arr[i])