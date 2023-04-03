import sys
sys.stdin = open('input.txt')

def back(n, i, tmp):
    global result
    if n == N-1:
        tmp += arr[i][0]
        result = min(result, tmp)
        return

    if tmp >= result:
        return

    for j in range(1,N):
        if i != j and not visited[j]:
            visited[j] = 1
            back(n+1, j, tmp + arr[i][j])
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 100*N*N
    visited = [0] * N

    back(0,0,0)
    print(f'#{tc}',result)