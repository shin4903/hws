import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[j][i] == 1:
                tmp = 1
            if tmp == 1 and arr[j][i] == 2:
                result += 1
                tmp = 0
    print(f'#{tc}',result)

    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] == 2:
    #             arr[i][j] = 0
    #         if arr[i][j] == 1:
    #             break
    #
    # for i in range(N):
    #     for j in range(N-1,-1,-1):
    #         if arr[i][j] == 1:
    #             arr[i][j] = 0
    #         if arr[i][j] == 2:
    #             break
    #
    # for i in range(N):
    #     cnt = 0
    #     for j in range(N):
    #         if arr[i][j] == 1:
    #             arr[i][j] = 0
    #             arr[i][cnt] = 1
    #             cnt += 1
    #         if arr[i][j] == 2:
    #             arr[i][j] = 0
    #             arr[i][cnt] = 2
    #             cnt += 1
    # # for i in arr:
    # #     print(i)
    # # print()
    # for i in range(N):
    #     for j in range(N-1):
    #         if arr[i][j] != 0 and arr[i][j+1] != 0 and arr[i][j] != arr[i][j+1]:
    #             result += 1
    #             arr[i][j], arr[i][j+1] = 0, 0
    #
    # print(f'#{tc}',result)

