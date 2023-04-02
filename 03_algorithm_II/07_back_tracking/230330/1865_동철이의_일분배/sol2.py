import sys
sys.stdin = open('input.txt')

def cal(i, N, tmp):
    global per
    if i == N:
        per = max(per, tmp*100)
        return
    if tmp == 0:
        return
    if tmp*100 <= per:
        return


    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            cal(i+1, N, tmp*(arr[i][j]/100))
            visited[j] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    per = 0
    cal(0, N, 1)
    print(per)


