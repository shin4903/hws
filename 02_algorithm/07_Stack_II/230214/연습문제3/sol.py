import sys
sys.stdin = open('input.txt')

# 조사 시작하는 노드의 번호
def DFS(start): # 문제에서는 1번 노드에서 출발
    stack = [start] # 시작지점
    visited = [0] * (V+1) # 이전에 방문한 곳은 다시 가지 않도록
    # 언제까지 조사?
    while stack:  # stack에 값이 있는 동안
        start = stack.pop() # 다음 조사 대상 꺼내기

        # 방문 표시
        # 이전번에 방문한 적 없다면
        if visited[start] == 0:
            visited[start] = 1
            print(start, end= ' ')
            # 현재 위치 start를 기준으로,
            # 0부터 V+1번 노드까지 모두 조사 가능한지 탐색
            for next in range(1, V+1):
                # start에서 next로 이동 가능하고, next를 방문한 적이 없다면
                if matrix[start][next] == 1 and visited[next] == 0:
                    # 다음 조사 대상에 next를 집어 넣는다.
                    stack.append(next)

# V = voltex = 노드
# E = Edge = 간선

V, E = map(int, input().split())
data = list(map(int,input().split()))

# 이동 가능 정보 2차원 리스트
# 7번 노드의 정보를 담기위한 7번 idx 필요
matrix = [[0]*(V+1) for _ in range(V+1)]
# for i in range(V+1):
#     print(matrix[i])

for i in range(E): # 모든 간선의 길이만큼
    # 이동 가능 정보를 담은 matrix의 인덱스는 각 노드 번호를 의미
    # 간선 정보 data의 0번째 -> 첫번째 출발 노드
    # 건선 정보 data의 1번째 -> 첫번째 도착 노드를 의미

    matrix[data[i * 2]][data[i * 2 + 1]] = 1
    matrix[data[i * 2 + 1]][data[i * 2]] = 1
# print()
# for i in range(V+1):
#     print(matrix[i])

DFS(1)