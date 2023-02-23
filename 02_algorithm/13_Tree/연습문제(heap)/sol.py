N = 6
data = [3, 6, 2, 1, 7, 9]

tree = [0 for _ in range(N+1)]
last = 1

for i in range(len(data)):
    if not tree[i]:
        tree[last] = data[i]
    else:
        last += 1
        child = last # 새로 추가된 정점의 마지막 번호
        parent = child // 2 # 완전 이진트리에서의 부모 정점 번호

        tree[child] = data[i]

        # 부모가 있고, 부모가 자식보다 큰 동안
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모와 자식 위치 변경
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식 위치를 부모위치로 변경
            child = parent
            # 부모는 부모 // 2 => 조상노드
            parent = parent // 2
print(tree)