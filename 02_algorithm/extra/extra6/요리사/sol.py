import sys
sys.stdin = open('input.txt')

def back(i, alst, blst):
    global result
    if i == N :
        if len(alst) == N//2:
            asum = bsum = 0
            for x in range(N//2):
                for y in range(N//2):
                    asum += arr[alst[x]][alst[y]]
                    bsum += arr[blst[x]][blst[y]]
            result = min(result,abs(asum-bsum))
        return
    back(i+1, alst + [i], blst)
    back(i + 1, alst, blst + [i])


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    result = 20000*N*N

    back(0,[],[])
    print(f'#{tc}',result)