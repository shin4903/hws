import sys
sys.stdin = open('input.txt')

def cal(i, tmp):
    global cost

    if i == N:
        cost = min(cost, tmp)
        return

    if tmp >= cost:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                cal(i+1, tmp + arr[i][j])
                visited[j] = 0



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = []
    cost = 100 * N

    cal(0,0)
    print(cost)