import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # N = 몇 명인지, M초의 시간에 K개의 붕어빵 만듬
    P = list(map(int,input().split()))
    P.sort()
    time = 0
    fish = 0
    sell = 0
    for i in P:
        sell += 1
        fish = K/M*i
        A = fish - sell
        if A >= 0:
            continue
        else:
            print('Impossible')
            break
    else:

        print('Possible')