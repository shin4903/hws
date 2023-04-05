import sys
sys.stdin = open('input.txt')

dx = [1,0]
dy = [0,1]

def dfs(x,y,tmp):
    global result
    if x == N-1 and y == N-1:
        result = min(result,tmp)
        return

    if tmp >= result:
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] > arr[x][y]: # 높은 곳으로 갈 때 그 차이만큼 더해줌
                dfs(nx,ny,tmp + 1 + (arr[nx][ny]-arr[x][y]))
            else: # 그렇지 않을 경우 1만 더함
                dfs(nx, ny, tmp + 1)
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 1000000000000

    dfs(0,0,0)
    print(f'#{tc}',result)


#
# def dijkstra(s, V):     # s : 출발, V : 마지막 정점 번호
#     U = [0] * (V+1)     # U 최소비용이 결정된 정점 집합
#     U[s] = 1            # U = {s}
#     for i in range(V+1): # s에서 정점 i로 가는 비용
#         D[i] = adjM[s][i]
#
#     # while U != V: 남은 정점의 비용 결정
#     N = V+1
#     for _ in range(N-1):    # N-1개 정점의 비용 결정
#         # D[w]가 최소인 w 결정
#         minV = INF
#         w = 0
#         for i in range(V+1):
#             if U[i] == 0 and minV > D[i]: # 남은 정점 i 중, 최소
#                 w = i
#                 minV = D[i]
#         U[w] = 1 # 최소인 w는 비용 D[w] 확정
#         # w에 인접인 정점에 대해 기존비용 vs w를 거쳐가는 비용 비교
#         for v in range(V+1):
#             if 0 < adjM[w][v] < INF: # w에 인접인 v의 조건
#                 D[v] = min(D[v], D[w] + adjM[w][v])
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     INF = 10000 # 문제에 따라
#     # V, E = map(int, input().split()) # 0~V번 정점, E : 간선 수
#     adjM = [[INF]*(N*N) for _ in range(N*N)] # 인접행렬
#     for i in range(N*N):
#         adjM[i][i] = 0 # 자기자신으로 가는 비용 : 0
#
#
#     for i in range(N*N):
#
#         adjM[u][v] = w
#
#     D = [0] * (V+1)
#     dijkstra(0, V)
# print(D)
