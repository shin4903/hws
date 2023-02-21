import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    cnt = 1
    queue = list(map(int, input().split()))
    while True:

        x = queue.pop(0)
        y = x - cnt
        if y > 0:
            queue.append(y)
            cnt += 1
            if cnt == 6:
                cnt = 1
        elif y <= 0:
            y = 0
            queue.append(y)
            break
    result = []
    for i in queue:
        result.append(str(i))
    print(f'#{tc}', ' '.join(result))

