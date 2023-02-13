import sys
sys.stdin = open('input.txt')

# def search(word):
#     temp = ''
#     # 조사 대상 문자와 조사 대상 다음 문자가
#     # 같은지 알아 보고,
#         # 같으면 다음 조사 대상에서 두 글자 모두 제외
#         # 다르면, 현재 조사대상인 문자는 다음 조사대상에 포함
#             # 그리고, 조사 대상을 다음칸으로 이동
#
#     # 조사대상 index
#     idx = 0
#     while idx < len(word)-1:
#         if word[idx] == word[idx+1]:
#             temp += word[idx+2:]
#             word = temp
#             # print(temp, word)
#             idx = 0
#             temp = ''
#         else:
#             temp += word[idx] # 다음 조사 대상에 현재 문자 추가
#             idx += 1          # 조사 위치 변경
#         # print(temp, idx)
#     return word
# T = int(input())
#
# for tc in range(1, T+1):
#     word = input()
#     print(f'#{tc}',len(search(word)))

# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     stack = []
#     for char in word:
#         if not stack:
#             stack.append(char)
#         elif stack and stack[-1] != char:
#             stack.append(char)
#         elif stack and stack[-1] == char:
#             stack.pop()
#     print(f'#{tc}', len(stack))




# 내가 푼거
T = int(input())

for tc in range(1, T+1):
    word = input()
    stack = []
    for char in word:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
            continue
        stack.append(char)
    print(f'#{tc}', len(stack))