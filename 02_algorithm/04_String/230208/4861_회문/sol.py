import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    for i in range(N):
        for l in range(N-M+1):
            word_list = []
            cnt = 0
            for j in range(l, l+M):
                word_list.append(arr[i][j])
                new_word_list = word_list[:]
                new_word_list.reverse()
            for k in range(len(word_list)):
                if word_list[k] == new_word_list[k]:
                    cnt += 1
        if cnt == M:
            print(f'#{tc}', ''.join(word_list))

    for i in range(N):
        for j in range(N):
            if i<j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(N):
        for l in range(N - M + 1):
            word_list = []
            cnt = 0
            for j in range(l,l + M):
                word_list.append(arr[i][j])

                new_word_list = word_list[:]
                new_word_list.reverse()
            for k in range(len(word_list)):
                if word_list[k] == new_word_list[k]:
                    cnt += 1
            if cnt == M:
                 print(f'#{tc}', ''.join(word_list))
