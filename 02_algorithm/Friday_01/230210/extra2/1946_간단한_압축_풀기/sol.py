import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    word = ''
    K = 0
    for i in range(N):
        Ci, Ki = map(str, input().split())
        K += int(Ki)
        for j in range(int(Ki)):
            word += Ci

    print(f'#{tc}')
    for idx in range(0,K,10):
        print(word[idx:idx+10])


