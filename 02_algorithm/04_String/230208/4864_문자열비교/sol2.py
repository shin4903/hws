import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    pattern = input()
    target = input()
    t_idx = 0
    p_idx = 0
    cnt = 0
    while t_idx < len(target):
        if pattern[p_idx] != target[t_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        t_idx += 1
        p_idx += 1

        if p_idx == len(pattern):
            p_idx = 0
            cnt += 1
    print(cnt)
