import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    bracket = input()
    stack = []
    # print(bracket)
    for char in bracket:
        # print(char)
        if char == '(':
            stack.append(char)
            # print(stack)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else: # 조사는 끝
        if stack:  # 하지만 값이 '(' 남아있는 경우
            # print(stack)
            result = -1
        else: # 조사가 끝나고 아무것도 없는 경우
            result = 1
    print(result)