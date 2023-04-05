import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(K)]
    cnt = 0
    while cnt < M:
        for i in range(K):
            if data[i][3] == 1:
                data[i][0] -= 1
                if data[i][0] <= 0:
                    data[i][0] = 1
                    data[i][2] = data[i][2] // 2

            elif data[i][3] == 2:
                data[i][0] += 1
                if data[i][0] >= N-1:
                    data[i][0] = 5
                    data[i][2] = data[i][2] // 2

            elif data[i][3] == 3:
                data[i][1] -= 1
                if data[i][1] <= 0:
                    data[i][1] = 1
                    data[i][2] = data[i][2] // 2

            elif data[i][3] == 4:
                data[i][1] += 1
                if data[i][1] >= N - 1:
                    data[i][1] = 5
                    data[i][2] = data[i][2] // 2

                for j in range(K):
                    if i != j:
                        if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                            if data[i][2] > data[j][2]:
                                data[i][2] += data[j][2]
                                data.pop(j)
                                K -= 1
                            else:
                                data[j][2] += data[i][2]
                                data.pop(i)
                                K -= 1
        cnt += 1
    print(f'#{tc}',data)