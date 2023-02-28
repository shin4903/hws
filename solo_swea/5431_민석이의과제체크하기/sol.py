import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split()) # N = 수강생의 수 M = 제출한 사람의 수
    data = list(map(int,input().split())) # 과제를 제출한 사람의 번호
    numbers = [i for i in range(1,N+1)]
    result = []
    for i in numbers:
        result.append(i)
        if i in data:
            result.pop()
    print(f'#{tc}',*result)
