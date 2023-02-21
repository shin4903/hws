import sys
sys.stdin = open('input.txt')

def BFS(S):
    visited = [0] * (V+1)
    queue = [S]
    while queue:
        start = queue.pop(0)
        if start == G:
            return visited[start] - 1
        if visited[start] == 0:
            visited[start] = 1
        for next in range(1,V+1):
            if arr[start][next] and not visited[next]:
                queue.append(next)
                visited[next] = visited[start] + 1
    return 0


T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[0]*(V+1) for i in range(V+1)]
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    S, G = map(int, input().split())
    print(f'#{tc}', BFS(S))