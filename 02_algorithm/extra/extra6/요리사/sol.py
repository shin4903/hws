import sys
sys.stdin = open('input.txt')

def back(i,lst):
    if i == N:
        if len(lst) == 4:
            result.append(lst)
        return
    back(i + 1, lst + [A[i]])
    back(i+1, lst)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    result = []
    back(0,[])
    print(result)