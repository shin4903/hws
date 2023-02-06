import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    arr = [num for num in range(10)] * 10
    N = int(input())
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + di[k]
                if 0 <= ni < N and 0 <= nj < N:
                    test = arr[ni][nj]
                    print(test)
