import sys
sys.stdin = open('input.txt')

T = int(input())
for k in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(N-M+1): # ex) N = 5 , M = 3  /  5 - 3 + 1 = 2
        c = 0 # c 초기화

        for j in range(i, i+M):
            c += a[j] # i~i+M 인덱스의 합
        b.append(c) # 을 빈 리스트에 append
    # print(b)
    # 정렬 해서
    for p in range(len(b)-1, 0 , -1):
        for l in range(p):
            if b[l] > b[l+1]:
                b[l], b[l + 1] = b[l + 1], b[l]
    # print(b)
    # 마지막 값과 첫 번째 값을 빼줌
    print(f'#{k+1} {b[-1]-b[0]}')

