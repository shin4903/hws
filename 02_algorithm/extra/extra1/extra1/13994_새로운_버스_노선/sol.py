import sys
sys.stdin = open('input.text')

T = int(input())
for tc in range(T):
    N = int(input())
    stop = [0] * 1001
    for i in range(1, N+1):
        bus = list(map(int, input().split()))

        if bus[0] == 1:
            for j in range(bus[1], bus[2] + 1):
                stop[j] += 1

        elif bus[0] == 2:
            if bus[1] % 2 == 0:
                stop[bus[2]] += 1
                for j in range(bus[1], bus[2], 2):
                    stop[j] += 1

            if bus[1] % 2 == 1 :
                stop[bus[2]] += 1
                for j in range(bus[1], bus[2], 2):
                    stop[j] += 1

        elif bus[0] == 3:
            if bus[1] % 2 == 0 :
                stop[bus[1]] += 1
                stop[bus[2]] += 1
                for j in range(bus[1] + 1, bus[2]):
                    if j % 4 == 0:
                        stop[j] += 1

            if bus[1] % 2 == 1:
                stop[bus[1]] += 1
                stop[bus[2]] += 1
                for j in range(bus[1] + 1, bus[2]):
                    if j % 3 == 0 and j % 10 != 0:
                        stop[j] += 1
    stop_max = 0
    for k in stop:
        if k > stop_max:
            stop_max = k
    print(f'#{tc+1} {stop_max}')
