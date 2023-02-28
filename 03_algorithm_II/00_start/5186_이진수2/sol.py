import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = float(input())

    result = ''
    while N:
        N *= 2
        if N >= 1:
            N -= 1
            result += '1'
        else:
            result += '0'
        # print(result)

    if len(result) >= 13:
        result = 'overflow'
    print(f'#{tc}',result)