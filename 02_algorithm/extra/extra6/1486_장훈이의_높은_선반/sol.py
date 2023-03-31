import sys
sys.stdin = open('input.txt')



T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    tall = list(map(int,input().split()))
    A = sum(tall)
    for i in range(1,1<<N):
        result = 0
        for j in range(0,N):
            if i & (1 << j):
                result += tall[j]
        if B <= result <= A :
            A = min(result, A)
    print(f'#{tc}',A-B)


