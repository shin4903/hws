import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited = [0] * 100
    stack = [start]

    while stack:
        start = stack.pop()
        if start == 99:
            return 1
        if visited[start] == 0:
            visited[start] = 1
        for next in range(1,100):
            if matrix[start][next] and not visited[next]:
                stack.append(next)
    return 0



for _ in range(1,11):
    tc, N = map(int,input().split())
    data = list(map(int,input().split()))
    matrix = [[0]*100 for _ in range(100)]

    for i in range(N):
        matrix[data[i * 2]][data[i * 2 + 1]] = 1

    print(f'#{tc}',DFS(0))