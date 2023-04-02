import sys
sys.stdin = open('input.txt')

def back(i, n, s):
    global A
    if i == n:
        if s >= B:
            A = min(A,s)
        return
    else:
        back(i + 1, n, s)
        back(i + 1, n, s + tall[i])


T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    tall = list(map(int,input().split()))
    A = sum(tall)

    back(0,N,0)
    print(f'#{tc}', A-B)