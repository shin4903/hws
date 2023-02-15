import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    cal = input()
    stack = [] # 연산자들을 담을 스택
    result = '' # 최종 결과값

    # 후위연산식 만들기기
   for char in cal: # 전체 식을 순회하며
        if char in '*+': # 연산자들이고
            if char == '*': # 곱하기 일 때
                while stack and stack[-1] in '*': # stack에 값이 있고
                    result += stack.pop()
                stack.append(char)
            elif char == '+':
                while stack:
                    result += stack.pop()
                stack.append(char)
        else:
            result += char
    # print(stack)
    while stack:
        result += stack.pop()

    # 계산 실행
    stack2 = []
    for re in result:
        if re not in '+*':
            stack2.append(re)
        else:
            w = int(stack2.pop())
            z = int(stack2.pop())
            if re == '+':
                stack2.append(w + z)
            if re == '*':
                stack2.append(w * z)
    print(f'#{tc}', *stack2)