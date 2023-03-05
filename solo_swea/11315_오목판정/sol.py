import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N)]

    result = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                for i in range(4):
                    cnt = 0
                    for j in range(1,5):
                        nx = x + dx[i] * j
                        ny = y + dy[i] * j
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                            cnt += 1
                    if cnt == 4:
                        result += 1
    if result:
        print(f'#{tc}','YES')
    else:
        print(f'#{tc}','NO')


    #         if arr[x][y] == 'o':
    #
    #             cnt = 1
    #             for _ in range(4):
    #                 nx = x + dx[1]
    #                 ny = y + dy[1]
    #                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
    #                     x = nx
    #                     y = ny
    #                     cnt += 1
    #                 if cnt == 5:
    #                     result += 1
    #
    #             cnt = 1
    #             for _ in range(4):
    #                 nx = x + dx[2]
    #                 ny = y + dy[2]
    #                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
    #                     x = nx
    #                     y = ny
    #                     cnt += 1
    #                 if cnt == 5:
    #                     result += 1
    #
    #             cnt = 1
    #             for _ in range(4):
    #                 nx = x + dx[3]
    #                 ny = y + dy[3]
    #                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
    #                     x = nx
    #                     y = ny
    #                     cnt += 1
    #                 if cnt == 5:
    #                     result += 1
    #
    #             cnt = 1
    #             for _ in range(4):
    #                 nx = x + dx[0]
    #                 ny = y + dy[0]
    #                 if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
    #                     x = nx
    #                     y = ny
    #                     cnt += 1
    #                 if cnt == 5:
    #                     result += 1
    # if result:
    #     print(f'#{tc}','YES')
    # else:
    #     print(f'#{tc}','NO')
