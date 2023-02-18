import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited = [0] * (V+1)
    stack = [start]

    while stack:
        start = stack.pop()
        if start == E:
            return 1
        if visited[start] == 0:
            visited[start] = 1
        for next in range(1,V+1):
            if matrix[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    S, E = map(int, input().split())
    print(DFS(S))