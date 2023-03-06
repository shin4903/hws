import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    Ci = list(map(int,input().split()))
    minV = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if Ci[i] != Ci[i+1] and Ci[j] != Ci[j+1]:
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    if minV > max(A,B,C) - min(A,B,C):
                        minV = max(A,B,C) - min(A,B,C)
    if minV == 1000:
        print(f'#{tc}',-1)
    else:
        print(f'#{tc}', minV)