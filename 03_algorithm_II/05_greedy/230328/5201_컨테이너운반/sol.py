import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    W = list(map(int,input().split()))
    T = list(map(int,input().split()))
    W.sort()
    T.sort()
    result = 0
    while T and W:
        A = W.pop()
        B = T.pop()
        if B >= A:
            result += A
        else:
            T.append(B)
    print(f'#{tc}',result)