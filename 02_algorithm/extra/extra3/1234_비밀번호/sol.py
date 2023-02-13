import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N, PW = map(str, input().split())
    real_PW = []
    for i in PW:
        if real_PW and real_PW[-1] == i:
            real_PW.pop()
            continue
        real_PW.append(i)

    print(f'#{tc}',''.join(real_PW))
