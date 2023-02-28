import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = 0
    result = []

    for i in m_list:
        result.append(N//i)
        N %= i
    print(f'#{tc}')
    print(*result)