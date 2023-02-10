import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_list = []
    result = [[0]*N for _ in range(N)]

    for i in range(N):
        arr = [[row[i] for row in arr[::-1]] for i in range(len(arr[0]))]
        new_arr = [[0]*N for _ in range(N)]


        for j in range(N):
            num = ''
            for k in range(N):
                num += str(arr[j][k])
            num_list.append(num)
    print(num_list)

    # cnt = 0
    # for i in range(N):
    #     for j in range(N):
    #         result[j][i] += num_list[cnt]
    #         cnt += 1
    #
    # print(f'#{tc}')
    # for i in range(N):
    #     print(*result[i])