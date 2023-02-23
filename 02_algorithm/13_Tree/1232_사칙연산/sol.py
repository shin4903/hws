import sys
sys.stdin = open('input.txt')


def inorder(node):
    global result
    if node <= N:
        inorder(node*2)
        inorder(node*2+1)
        result += data[node][1]


for tc in range(1, 11):
    N = int(input())
    data = [[]] + [list(input().split()) for _ in range(N)]
    result = ' '
    inorder(1)
    print(f'#{tc}',result)