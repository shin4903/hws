import sys
sys.stdin = open('input.txt')

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return cnt
T = int(input())

for tc in range(1,T+1):
    E, N = map(int,input().split())
    data = list(map(int,input().split()))
    tree = [[0]*3 for i in range(E+2)]
    cnt = 0
    for i in range(E):
        parent, child = data[i*2], data[i*2+1]

        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    print(preorder(N))