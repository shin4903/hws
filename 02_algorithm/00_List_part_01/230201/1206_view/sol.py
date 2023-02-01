import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    F = list(map(int, input().split()))
    result = 0

    for j in range(2,N-2):
        max_floor = 0
        for k in range(j-2, j+3):
            if k == j :
                continue
            elif F[k] > max_floor:
                max_floor = F[k]

        if F[j] - max_floor > 0:
            result += (F[j] - max_floor)

    print(f'#{i+1} {result}')


