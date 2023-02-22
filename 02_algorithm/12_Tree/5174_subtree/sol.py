def preorder(node):  # 전위 순회
    global cnt
    global N

    if node != 0:
        cnt += 1
        if left[node]:
            N = left[node]
            preorder(left[node])
        if right[node]:
            N = right[node]
            preorder(right[node])

    return cnt


T = int(input())  # test case

for tc in range(1, T + 1):
    cnt = 0
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    parent, left, right = [0] * (E + 2), [0] * (E + 2), [0] * (E + 2)

    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]

        if left[p] == 0:  # 아직 왼쪽 자식 없으면
            left[p] = c  # p번의 왼쪽 자식 c
        else:
            right[p] = c
        parent[c] = p  # 그 자식의 부모 기록
    print(f'#{tc} {preorder(N)}')