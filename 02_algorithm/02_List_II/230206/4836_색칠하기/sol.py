import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        A = list(map(int,input().split()))

        for i in range(A[0],A[2]+1):
            for j in range(A[1],A[3]+1):
                arr[i][j] += A[4]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1
    print(f'#{tc}',cnt)