import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    max_value = 0
    for i in str1: # str1의 각 문자를 순회하며
        if max_value < str2.count(i): # str2에서 해당 문자의 개수가 max_value보다 크다면
            max_value = str2.count(i) # 그 문자가 max_value가 된다.
    print(f'#{tc}' ,max_value) # for문을 끝까지 순회하고 나온 max_value가 답이 된다.
