import sys
sys.stdin = open('input.txt')

# for문 돌면서 좌표 1씩 이동, 이동 할 때마다 다른 원소들 좌표비교해가며 같으면 result에 에너지 더해주고 0으로 만들어줌
# for문 다 돌고나면 에너지 0인 애들 pop

# 상(0 , y +) 하(1, y -) 좌(2, x -) 우(3, x+)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int,input().split())))
    cnt = 0
    result = 0
    while cnt != 1002:
        for i in range(len(data)):
            if data[i][2] == 0:
                data[i][1] += 1

            elif data[i][2] == 1:
                data[i][1] -= 1

            elif data[i][2] == 2:
                data[i][0] -= 1

            elif data[i][2] == 3:
                data[i][0] += 1

            for j in range(len(data)):
                if data[i] != data[j] and data[i][0] == data[j][0] and data[i][1] == data[j][1] and ((data[i][2] == 1 and data[j][2] == 0) or (data[i][2] == 2 and data[j][2] == 3) or (data[i][2] == 0 and data[j][2] == 1) or (data[i][2] == 3 and data[j][2] == 2)) :
                    result += data[i][3]
                    result += data[j][3]
                    data[i][3] = 0
                    data[j][3] = 0
        # info = []
        # for i in range(len(data)):
        #     if data[i][3] == 0:
        #         if data[i][0] > 1000 or data[i][0] < -1000 or data[i][1] > 1000 or data[i][1] < -1000:
        #             if i not in info:
        #                 cnt += 1
        #                 info.append(i)
        #         elif i not in info:
        #             cnt += 1
        #             info.append(i)

        cnt += 1
    # for i in data:
    #     print(i)
    # print()

    print(f'#{tc}',result)

