import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = 10
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        if s == 0:
            print(1)
            break
    else:
        print(0)