import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    word_list = []
    re_word_list = []
    for i in word:
        word_list.append(i)
        re_word_list.append(i)
    re_word_list.reverse()
    cnt = 0
    for j in range(len(word_list)):
        if word_list[j] == re_word_list[j]:
            cnt += 1

    if cnt == len(word_list):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')