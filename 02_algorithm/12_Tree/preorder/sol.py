import sys
sys.stdin = open('input.txt')

def preorder(node):
    if node != 0:
        # 전위 순회기 때문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할 일은? 나를 출력
        print(node, end=' ')
        # 왼쪽 자식 조사
        preorder(left[node])
        # 오른쪽 자식 조사
        preorder(right[node])

def inorder(node):
    if node != 0:
        # 전위 순회기 때문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할 일은? 나를 출력

        # 왼쪽 자식 조사
        inorder(left[node])
        print(node, end=' ')
        # 오른쪽 자식 조사
        inorder(right[node])

def postorder(node):
    if node != 0:
        # 전위 순회기 때문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할 일은? 나를 출력
        # 왼쪽 자식 조사
        postorder(left[node])
        # 오른쪽 자식 조사
        postorder(right[node])
        print(node, end=' ')

V = int(input()) # 노드의 개수
E = V - 1  # 간선의 개수
edge = list(map(int, input().split()))

# 인덱스를 활용할 것이기 떄문에 노드의 개수 +1
# 0번 노드는 없음
parent = [0] * (V+1) # 부모의 정보
left = [0] * (V+1) # 왼쪽 자식 정보
right = [0] * (V+1) # 오른쪽 자식 정보

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    # print(p, c)
    if left[p] == 0: # 아직 왼쪽 자식이 없으면
        left[p] = c # p번의 왼쪽 자식 c
    else: # 왼쪽에 자식이 있으면
        right[p] = c
    parent[c] = p # 그 자식의 부모가 누군지 기록

root = 0
for i in range(1, V+1): # 모든 노드 순회
    if parent[i] == 0: # 부모정보를 담았는데, 부모가 없으면 루트
        root = i
        break

# 조사를 시작 root 노드부터
preorder(root)
print()
inorder(root)
print()
postorder(root)