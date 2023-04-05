import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x
def union(x,y):
    rep[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1,T+1):

    V, E = map(int,input().split()) # V = 노드의 개수 , E = 간선의 개수
    rep = [i for i in range(V+1)] # 0을 안쓰기 떄문에 범위 V+1로 설정
    graph = [] # 간선 정보를 담음

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append([n1, n2, w])

    graph.sort(key=lambda x : x[2]) # 사이클을 제거하고 가중치의 합이 최소가 되어야 하므로 가중치를 기준으로 오름차순 정렬

    result = 0
    cnt = 0
    for n1, n2, w in graph:
        if find_set(n1) != find_set(n2): # n1과 n2의 대표 노드가 다르면
            cnt += 1 # 카운트를 1 증가시키고
            result += w # result에 가중치를 더해줌
            union(n1, n2) # 싸이클을 방지하기 위해 n1과 n2를 합쳐 대표노드를 동일하게 함
            if cnt == V: # MST 구성 완료
                break
    print(f'#{tc}',result)