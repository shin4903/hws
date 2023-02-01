import sys
sys.stdin = open('input.txt')

T= int(input())
for i in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    result = 0
    for j in range(N):
        max_h = len(a) - (j+1)

        for k in range(j+1, len(a)):
            if a[j] <= a[k]:
                max_h -= 1
            if result < max_h:
                result = max_h
    print(f'#{i} {result}')
