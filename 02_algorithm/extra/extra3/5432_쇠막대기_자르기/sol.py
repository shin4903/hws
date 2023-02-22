import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    steel = input()
    stack = []
    rasier = []

    print(steel)
    cnt = 0
    for i in range(len(steel)):
        if stack and stack[-1] == '(' and steel[i-1] == '(' and steel[i] ==')': # 레이저의 위치
            stack.pop()
            rasier.append(i)
            cnt += 1

            continue
        if stack and stack[-1] == '(' and steel[i] == ')' and steel[i-1] != '(': #
            stack.pop()
            cnt += 1
            continue

        stack.append(steel[i])
        cnt += 1


    print(rasier)
