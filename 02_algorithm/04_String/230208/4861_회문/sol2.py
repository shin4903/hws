import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]


    for i in range(N):
        for k in range(N - M + 1):
            A = []
            for j in range(k,k+M):
                A.append(arr[i][j])
                B = A[:]
                B.reverse()
            if A == B:
                print(''.join(A))
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(N):
        for k in range(N - M + 1):
            A = []
            for j in range(k,k+M):
                A.append(arr[i][j])
                B = A[:]
                B.reverse()
            if A == B:
                print(''.join(A))
