import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    cal = input().split()
    result = 0
    stack = []

    for char in cal:
        if char not in '+-*/().':
            stack.append(char)

        elif len(stack) >= 2 :
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '*':
                stack.append(y * x)
            elif char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '/':
                stack.append(y // x)
        elif len(stack) < 2 and char in '+-*/':
            print(f'#{tc}','error')
            break
        elif len(stack) > 1 and char == '.':
            print(f'#{tc}', 'error')
            break
        elif len(stack) == 1 and char =='.':
            print(f'#{tc}', stack.pop())
