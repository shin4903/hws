import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, Q = map(int,input().split())
    data = [0]*N
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L,R+1):
            data[j-1] = i
    print(f'#{tc}',*data)
