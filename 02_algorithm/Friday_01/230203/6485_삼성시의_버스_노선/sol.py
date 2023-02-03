import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    C = [0] * 500
    a = [0] * N
    b = [0] * N
    for j in range(N):
        A, B = map(int, input().split())
        a[j] += A
        b[j] += B
    P = int(input())
    for k in range(a[0], b[0]+1):
        C[k] += 1
    for l in range(a[1], b[1]+1):
        C[l] += 1

    max_value = 0
    cnt = 0
    cnt_list = []
    for m in C:
        if C[m] > 0 :
            cnt_list.append(str(C[m]))
    print(f'#{tc+1} {" ".join(cnt_list)}')