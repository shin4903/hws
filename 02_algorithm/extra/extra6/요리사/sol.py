import sys
sys.stdin = open('input.txt')

def back(n, i, tmp):
    if n == N -1 :
        result.append(tmp)
        return

    for j in range(N):
        if i != j and not visited[j]:
            visited[j] = 1
            back(n+1, j, tmp + arr[i][j] + arr[j][i])
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    result = []
    visited = [0] * N
    back(0,0,0)
    print(result)