import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    result_cnt = 0
    result_cnt2 = 0

    for i in range(8):
        word = arr[i]
        for j in range(8 - N + 1):
            new_word = word[j:j + N]
            re_new_word = new_word[:]
            re_new_word.reverse()

            cnt = 0
            for k in range(N):
                if re_new_word[k] == new_word[k]:
                    cnt += 1
                    if cnt == N:
                        result_cnt += 1

    for i in range(8):
        for j in range(8):
            if i<j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(8):
        word = arr[i]
        for j in range(8 - N + 1):
            new_word = word[j:j + N]

            re_new_word = new_word[:]
            re_new_word.reverse()

            cnt = 0
            for k in range(N):
                if re_new_word[k] == new_word[k]:
                    cnt += 1
                    if cnt == N:
                        result_cnt2 += 1

    print(f'#{tc}', result_cnt+result_cnt2)