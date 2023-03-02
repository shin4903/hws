import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
                result.append([i,j])
            elif arr[i][j] and not arr[i+1][j] and not arr[i][j+1]:
                result.append([i,j])
    print(f'#{tc}',result)