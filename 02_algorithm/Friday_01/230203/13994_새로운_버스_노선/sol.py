import sys
sys.stdin = open('input.text')

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split())) # 1 2 5
    B = list(map(int, input().split())) # 2 3 10
    C = list(map(int, input().split())) # 3 2 9
    stop = [0] * 100

    for j in range(A[1],A[2]+1):
        stop[j] += 1

    if B[1] % 2 == 1:
        for k in range(B[1]+1, B[2], 2):
            stop[B[1]] += 1
            stop[B[2]] += 1
            stop[k] += 1
    if B[1] % 2 == 0:
        for k in range(B[1]+1, B[2], 2):
            stop[B[1]] += 1
            stop[B[2]] += 1
            stop[k] += 1
    print(stop)
    # if C[1] % 2 == 1:
    #     for l in range(C[1]+1, C[2]):
    #         stop[C[1]] += 1
    #         stop[C[2]] += 1
    #         if l % 3 == 0 and l % 10 != 0:
    #             stop[l] += 1
    # if C[1] % 2 == 0:
    #     for l in range(C[1]+1, C[2]):
    #         stop[C[1]] += 1
    #         stop[C[2]] += 1
    #         if l % 4 == 0:
    #             stop[l] += 1
    # print(stop)

# 2345 , 3579 10, 2489
#