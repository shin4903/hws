import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1,13)]
    cnt = 0
    for i in range(1<<12):
        result = 0
        count = 0
        for j in range(12):
            if i & (1 << j):
                result += arr[j]
                count += 1
        if result == K and count == N:
            cnt += 1
    print(cnt)