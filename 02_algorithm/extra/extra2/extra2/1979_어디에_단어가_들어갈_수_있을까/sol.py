import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(N-K+1):
            one = arr[i][j:j+K]
            if one.count(1) == K:
                result += 1


    # for i in range(N):
    #     for j in range(N):
    #         if i < j :
    #             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    #
    # for i in range(N):
    #     cnt = 0
    #     for j in range(N - 1):
    #         if arr[i][j] == arr[i][j + 1] and arr[i][j] == 1:
    #             cnt += 1
    #     if arr[i].count(1) == K and cnt >= 2:
    #         result += 1

    print(result)
