import sys
sys.stdin = open('input.txt')


def func(N, Key):
    N_list = [i for i in range(1, N + 1)]
    start = 0
    end = N - 1
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end)//2
        if N_list[middle] == Key:
            return cnt
        elif N_list[middle] > Key:
            end = middle
        else:
            start = middle
    return N


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    if func(P,A) < func(P,B):
        print(f'#{tc} A')

    elif func(P,A) > func(P,B):
        print(f'#{tc} B')

    else:
        print(f'#{tc} 0')