import sys
sys.stdin = open('input.txt')

def back(i, N, tmp):
    global cost
    if i == N :
        cost = min(tmp, cost)
        return

    if tmp > cost:
        return

    else:
        for j in range(N):
            if not visitid[j]:
                visitid[j] = 1
                back(i+1, N, tmp + arr[i][j])
                visitid[j] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visitid = [0]*N
    cost = 100 * N * N
    back(0, N, 0)
    print(cost)