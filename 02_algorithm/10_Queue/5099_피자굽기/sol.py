import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    queue = []
    result = [i for i in range(M)]
    result_queue = []

    for _ in range(N):
        x = Ci.pop(0)
        queue.append(x)
        rx = result.pop(0)
        result_queue.append(rx)

    while True:
        x = queue.pop(0) // 2
        rx = result_queue.pop(0)
        if x > 0:
            queue.append(x)
            result_queue.append(rx)
        elif x == 0 and Ci:
            y = Ci.pop(0)
            queue.append(y)
            ry = result.pop(0)
            result_queue.append(ry)

        if not Ci and len(queue) == 1:
            print(f'#{tc}',result_queue.pop()+1)
            break
