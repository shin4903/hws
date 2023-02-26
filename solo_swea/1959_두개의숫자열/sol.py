import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai
    S = M-N+1
    data = []
    result = []
    for i in range(S):
        data.append(Bj[i:i+N])
    # print('Ai', Ai)
    # print()
    # print('data', data)
    # print()
    for j in range(len(data)):
        value = 0
        for k in range(N):
            value += data[j][k] * Ai[k]
        result.append(value)
    print(f'#{tc}',max(result))