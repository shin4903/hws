import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    cal = input()
    stack = [] # 연산자들을 담아둘 stack
    result = '' #최종 결과값
    # 전체 식 순회
    for char in cal:
        # 연산자들이라면
        if char in '+-*/()':
            # print(char)
            # 연산자들의 우선순위에 맞춰서 값들을 stack에 넣는 과정
            if char == '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop() # '('를 뺴줌
        else:
            result += char

    while stack:
        result += stack.pop()

    cal = result

    stack2 = []
    result2 = 0
    for char in cal:
        if char not in '+-*/':
            stack2.append(char)
        else:
            x = int(stack2.pop())
            y = int(stack2.pop())
            if char == '+':
                stack2.append(y + x)
            elif char == '-':
                stack2.append(y - x)
            elif char == '*':
                stack2.append(y * x)
            elif char == '/':
                stack2.append(y / x)
    print(stack2[-1])
