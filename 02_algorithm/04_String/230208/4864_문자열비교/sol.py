import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()


    a = 1 if str1 in str2 else 0
    print(f'#{tc}',a)

    # str1 = list(map(str,input()))
    # str2 = list(map(str,input()))
    #
    # N = len(str1)
    # M = len(str2)

    # cnt = 0
    # new_str2 = []
    # for j in range(M-N+1):
    #     for i in range(j, j+N):
    #         new_str2.append(str2[i])
    #         for k in range(N):
    #             if str1[k] == new_str2[k]:
    #                 cnt += 1
    #     if cnt == N:
    #         print(1)
    #     else:
    #         print(0)

