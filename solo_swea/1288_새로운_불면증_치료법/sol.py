import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numlist = []
    for i in str(N):
        numlist.append(i)
    cnt = 1
    while True:
        X = N * cnt
        for i in str(X):
            numlist.append(i)
        if len(set(numlist)) == 10:
            break
        cnt += 1

    print(f'#{tc}',X)