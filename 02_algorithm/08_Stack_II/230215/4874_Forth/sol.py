import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = input().split()
    stack = []
    result = 0
    for char in cal:
        if char not in '+-*/.':
            stack.append(char)
        elif len(stack) >= 2 and char in '+-*/':
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                # 나눗셈일 경우 항상 나누어 떨어진다
                stack.append(y // x)
        elif len(stack) <= 1 and char in '+-*/':
            print(f'#{tc}','error')
            break
        elif len(stack) > 1 and char =='.':
            print(f'#{tc}', 'error')
            break
        elif len(stack) == 1 and char == '.':
            print(f'#{tc}',stack[-1])
    # else:
    #     stack.pop()
    #     print(f'#{tc}',stack[-1])

