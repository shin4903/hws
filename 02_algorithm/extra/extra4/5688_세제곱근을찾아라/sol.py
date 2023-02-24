import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    result = round(N ** (1/3),2)
    if result == int(result):
        print(f'#{tc}',int(result))
    else:
        print(f'#{tc}',-1)





