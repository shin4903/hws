import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(K)]
    cnt = 0
    while cnt != M:
        for i in range(K):
            if data[i][3] == 1:
                data[i][0] -= 1

            elif data[i][3] == 2:
                data[i][0] += 1


            elif data[i][3] == 3:
                data[i][1] -= 1


            elif data[i][3] == 4:
                data[i][1] += 1


        for i in range(K):
            if data[i][0] == 0:
                data[i][3] = 2
                data[i][2] = data[i][2] // 2

            if data[i][0] == N-1:
                data[i][3] = 1
                data[i][2] = data[i][2] // 2

            if data[i][1] == 0:
                data[i][3] = 4
                data[i][2] = data[i][2] // 2

            if data[i][1] == N - 1:
                data[i][3] = 3
                data[i][2] = data[i][2] // 2

        # 두개 이상이 합쳐질 경우도 생각 (백트레킹?)
        A = []
        for i in range(K):
            for j in range(i+1,K):
                if i != j:
                    if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                        if [data[i][0],data[i][1]] not in A:
                            A.append([data[i][0],data[i][1]])
                        # if data[i][2] > data[j][2]:
                        #     data[i][2] += data[j][2]
                        #     data[j][2] = 0
                        #
                        # else:
                        #     data[j][2] += data[i][2]
                        #     data[i][2] = 0

        for x in A:
            B = []
            tmp = 0
            idx = 0
            for i in range(K):
                if data[i][0] == x[0] and data[i][1] == x[1]:
                    B.append([i, data[i][2]])
            for y in B:
                if y[1] > tmp:
                    tmp = y[1]
                    idx = y[0]

            # print(B)
            for z in range(len(B)):
                if B[z][0] != idx:
                    data[B[z][0]][2] = 0
                    data[idx][2] += B[z][1]


        cnt += 1
    result = 0
    for i in range(K):
        result += data[i][2]
    print(f'#{tc}',result)