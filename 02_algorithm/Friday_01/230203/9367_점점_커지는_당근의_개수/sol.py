import sys
sys.stdin = open('input.text')

T = int(input())

for tc in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    C_list = [0] * (N+2)
    CC = []
    for i in range(len(C)):
        C_list[i] += C[i]
    cnt = 1
    for j in range(N-1):
        if C_list[j] + 1 == C_list[j+1]:
            cnt += 1
            if C_list[j+1] + 1 != C_list[j+2]:
                CC.append(cnt)
                cnt = 1
        else:
            CC.append(cnt)
    CC_max = 0
    for k in CC:
        if k >= CC_max:
            CC_max = k
    print(f'#{tc+1} {CC_max}')
