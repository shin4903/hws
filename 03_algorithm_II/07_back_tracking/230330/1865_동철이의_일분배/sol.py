import sys
sys.stdin = open('input.txt')

def backtracking(i,tmp):
    global per
    if i == N:
        per = max(per,tmp*100)
        return
    if tmp*100 <= per:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtracking(i+1, tmp * (arr[i][j]/100))
                visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    per = 0
    backtracking(0,1)
    print(f'#{tc}',format(per,".6f"))