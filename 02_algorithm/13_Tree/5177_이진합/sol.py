import sys
sys.stdin = open('input.txt')


def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        if tree[node] == '+':
            tree[node] = int(tree[left[node]]) + int(tree[right[node]])
        elif tree[node] == '-':
            tree[node] = int(tree[left[node]]) - int(tree[right[node]])
        elif tree[node] == '*':
            tree[node] = int(tree[left[node]]) * int(tree[right[node]])
        elif tree[node] == '/':
            tree[node] = int(tree[left[node]]) // int(tree[right[node]])


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        data = list(input().split())
        tree[int(data[0])] = data[1]
        if len(data) == 4:
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])
    postorder(1)
    print(f'#{tc} {tree[1]}')