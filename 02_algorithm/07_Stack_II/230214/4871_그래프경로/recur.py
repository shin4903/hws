import sys
sys.stdin = open('input.txt')

def DFS(start):
    # 첫 시작위치 방문
    visited[start] = 1
    if start == G:
        return 1
    for next in range(1, V + 1):
        if data[start][next] and not visited[next]:
            return DFS(next)
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0]*(V+1) for _ in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)
    # 간선 정보 입력 받기
    for _ in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1

    # 시작지점 S, 도착지점 G
    S,G = map(int, input().split())

    print(f'#{tc}', DFS(S))

