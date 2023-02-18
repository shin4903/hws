import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited = [0] * (V + 1)
    stack = [start]

    while stack:
        start = stack.pop()

        if start == G:
            return 1

        if visited[start] == 0:
            visited[start] = 1

        for next in range(1,V+1):
            if data[start][next] and not visited[next]:
                stack.append(next)
    return 0
T = int(input())

for tc in range(1,T+1):
    V, E = map(int, input().split())
    data = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1

    S, G  = map(int, input().split())

    print(DFS(S))