import sys
sys.stdin = open('input.text')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = input()
    num_list = [0] * (N+1)
    cnt_list = []
    cnt = 0
    cnt_list_num = 0
    for j in range(N):
        if int(num[j]) == 1:
            num_list[j] += 1

    for k in range(N):
        if int(num_list[k]) == 1:
            cnt += 1
            if int(num_list[k+1]) == 0:
                cnt_list.append(cnt)
        else:
            cnt = 0
    for l in cnt_list:
        if l > cnt_list_num:
            cnt_list_num = l
    print(f'#{tc} {cnt_list_num}')