import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())

    A = list(map(int,input().split()))

    cnt = 0
    for i in range(1, 1<<N):
        result = 0
        for j in range(0,N):
            if i & (1 << j):
                result += A[j]
                if result > K :
                    break
        if result == K:
            cnt += 1
    print(f'#{tc}',cnt)