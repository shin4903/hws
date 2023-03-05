import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    M = N // 2
    result = 0
    for i in range(N):
        for j in range(N):
            if (abs(i-M) + abs(j-M)) <= M:
                result += arr[i][j]
    print(f'#{tc}',result)