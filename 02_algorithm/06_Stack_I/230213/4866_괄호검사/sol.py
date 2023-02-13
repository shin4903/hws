import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    word = input()
    stack = []

    # 최종 결과값
    result = 1
    stack = []
    for char in word:
        if char == '(' or char =='{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    result = 0
                    break
                elif stack[-1] != '(':
                    result = 0
                    break

            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    break
                else:
                    stack.pop()
    if stack:
        result = 0
    print(f'#{tc}',result)


    # for char in word:
    #     if char == '(' or char == '{':
    #         stack.append(char)
    #
    #     elif char ==')':
    #         if stack[-1] == '(':
    #             stack.pop()
    #         else:
    #             result = -1
    #             break
    #
    #     elif char =='}':
    #         if stack[-1] == '{':
    #             stack.pop()
    #         else:
    #             result = 0
    #             break
    # else: # 조사는 끝
    #     if stack:  # 하지만 값이 '(' 남아있는 경우
    #         # print(stack)
    #         result = 0
    #     else: # 조사가 끝나고 아무것도 없는 경우
    #         result = 1
    # print(f'#{tc}',result)
    #
