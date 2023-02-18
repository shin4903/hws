import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited = [0] * (V + 1)
    stack = [start]
    while stack:
        start = stack.pop()
        if visited[start] == 0:
            visited[start] = 1
            print(start, end=' ')
        for next in range(1, V+1):
            if matrix[start][next] and not visited[next]:
                stack.append(next)


V, E = map(int,input().split())
data = list(map(int,input().split()))
matrix = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    matrix[data[i * 2]][data[i * 2 + 1]] = 1
    matrix[data[i * 2 + 1]][data[i * 2]] = 1
DFS(1)