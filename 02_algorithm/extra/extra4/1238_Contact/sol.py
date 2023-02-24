import sys
sys.stdin = open('input.txt')

def BFS(S):
    queue = [S]
    while queue:
        start = queue.pop(0)
        if visited[start] == 0:
            visited[start] = 1
        for next in range(1,101):
            if arr[start][next] and not visited[next]:
                queue.append(next)
                visited[next] = visited[start] + 1


for tc in range(1,11):
    N, S = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[0]*101 for _ in range(101)]
    visited = [0] * 101
    for i in range(N//2):
        arr[data[i*2]][data[i*2+1]] += 1

    BFS(S)
    result = []
    maxV = 0
    for i in range(101):
        if visited[i] >= maxV:
            maxV = visited[i]
    for i in range(101):
        if visited[i] == maxV:
            result.append(i)
    print(f'#{tc}', max(result))