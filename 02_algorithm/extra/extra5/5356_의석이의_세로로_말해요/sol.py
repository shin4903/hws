import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = [['']*15 for _ in range(5)]
    result = ''
    for i in range(5):
        word = input()
        for j in range(len(word)):
            arr[i][j] = word[j]

    for i in range(15):
        for j in range(5):
            if arr[j][i] != '':
                result += arr[j][i]
    print(f'#{tc}',result)