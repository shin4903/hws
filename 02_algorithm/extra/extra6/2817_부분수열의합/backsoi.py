import sys
sys.stdin = open('input.txt')

def back(i, n, s):
    global cnt
    if i == n:
        if s == K:
            cnt += 1
        return
    if s > K:
        return
    back(i + 1, n, s)
    back(i + 1, n, s+A[i])

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split())) #[1,2,1,2]
    cnt = 0
    back(0,N,0)
    print(f'#{tc}', cnt)