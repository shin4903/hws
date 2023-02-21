import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())

    data = list(map(int, input().split()))
    for _ in range(M):
        x = data.pop(0)
        data.append(x)
    print(f'#{tc}',data.pop(0))