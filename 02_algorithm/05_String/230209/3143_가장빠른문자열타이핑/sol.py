import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    target, pattern = map(str, input().split())
    count = 0
    typing = 0
    p_idx = 0
    t_idx = 0
    while t_idx < len(target): # t_idx가 target의 길이보다 작은 동안 반복
        if target[t_idx] != pattern[p_idx]: # ABC / AABBABC
            t_idx = t_idx - p_idx
            p_idx = -1
        p_idx += 1
        t_idx += 1
        if p_idx == len(pattern):
            count += 1
            p_idx = 0
    typing = len(target) - len(pattern) * count + count
    print(f'#{tc} {typing}')