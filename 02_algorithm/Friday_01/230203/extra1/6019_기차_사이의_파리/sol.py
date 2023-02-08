import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())
    for t in range(D//B):
        if D - t * B > t * F:
            Q = (D - t * B) - t*F + (D - t * A)
    print(Q)
