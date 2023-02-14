import sys
sys.stdin = open('input.txt')

def DFS(start): # 문제에서는 1번 노드에서 출발
    stack = [start] # 시작지점
    visited = [0] * 100 # 이전에 방문한 곳은 다시 가지 않도록
    # 언제까지 조사?
    while stack:  # stack에 값이 있는 동안
        start = stack.pop() # 다음 조사 대상 꺼내기

        # 방문 표시
        # 이전번에 방문한 적 없다면
        if visited[start] == 0:
            visited[start] = 1
            # print(start, end= ' ')
            if start == 99:
                return 1
            # 현재 위치 start를 기준으로,
            # 0부터 V+1번 노드까지 모두 조사 가능한지 탐색
            for next in range(100):
                # start에서 next로 이동 가능하고, next를 방문한 적이 없다면
                if matrix[start][next] == 1 and visited[next] == 0:
                    # 다음 조사 대상에 next를 집어 넣는다.
                    stack.append(next)
    return 0

for tc in range(1,11):
    T, N = map(int, input().split())
    data = list(map(int,input().split()))
    matrix = [[0]*100 for _ in range(100)]

    for i in range(N):  # 모든 간선의 길이만큼
        # 이동 가능 정보를 담은 matrix의 인덱스는 각 노드 번호를 의미
        # 간선 정보 data의 0번째 -> 첫번째 출발 노드
        # 건선 정보 data의 1번째 -> 첫번째 도착 노드를 의미
        matrix[data[i * 2]][data[i * 2 + 1]] = 1

    print(f'#{tc}', DFS(0))
