import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [i for i in range(1,101)]
    N, K = map(int, input().split())
    for i in range(1 << N):
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                # print(arr[j], end=",")
                cnt += arr[j]
                print(cnt)
        print()
    print()