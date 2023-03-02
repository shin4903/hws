import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        else:
            result.append(cnt)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        else:
            result.append(cnt)
    print(f'#{tc}',result.count(K))