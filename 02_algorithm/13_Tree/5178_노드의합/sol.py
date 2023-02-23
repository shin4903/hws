import sys, math
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M, L = map(int,input().split()) # N = 노드의 개수, M = 리프노드의 개수, L = 출력할 노드의 번호
    arr = [0] * (N + 1)

    cnt = 1
    for _ in range(M):
        x, y = map(int,input().split())
        arr[x] = y
    for i in range(N,0,-1):
        if i // 2 > 0 :
            arr[i // 2] += arr[i]
    print(f'#{tc}', arr[L])
