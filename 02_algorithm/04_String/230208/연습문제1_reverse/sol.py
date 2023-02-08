import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    word = list(map(str, input())) # 입력받은 단어를 word 리스트에 문자열로 담음
    word.reverse() # word 리스트를 reverse
    print(''.join(word)) # join함수를 이용해 출력