import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    for _ in range(N):
        data[-1] -= 1
        data[0] += 1
        data.sort()
    print(data[-1] - data[0])
