import sys
sys.stdin = open('input.txt')


# 행과 총합을 기준으로 min_sum 함수 생성
# result = 현재까지의 합 / total = 설정해둔 최소값
# i = 행이 몇번째 줄인지
def min_sum(i, result):
    global total

    # 만약 현재 합이 최소값보다 크면 계산 종료
    if result > total:
        return

    # 종료 조건 행이 N 줄까지 다 돌면 결과값 return

    if i == N:
        # print(result)
        if result < total:
            total = result
            return

    for j in range(N):
        if j not in visited:
            visited.append(j)
            # print(visited)
            min_sum(i+1, result+arr[i][j])
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    total = 10*N*N
    min_sum(0, 0)
    print(f'#{tc}', total)