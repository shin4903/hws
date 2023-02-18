import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    cal = input()
    stack = [] # 연산자들을 담을 스택
    result = '' # 최종 결과값
    for char in cal:
        if char in '+-*/()':
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
                stack.pop()
        else:
            result += char
    while stack:
        result += stack.pop()


    stack2 = []
    result2 = 0

    for char in result:
        if char not in '+-*/':
            stack2.append(char)
        else:
            x = int(stack2.pop())
            y = int(stack2.pop())
            if char == '*':
                stack2.append(y * x)
            elif char == '/':
                stack2.append(y / x)
            elif char == '+':
                stack2.append(y + x)
            elif char == '-':
                stack2.append(y - x)
    print(stack2[-1])