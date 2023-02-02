import sys
sys.stdin = open('input.text')
# K = 한 번 충전으로 이동할 수 있는 정류장수   3
# N = 정류장 수 0~N     10
# M = 충전기가 설치된 정류장 수   1 3 5 7 9
# Stop = 충전기가 설치된 정류장 번호
# 최소 충전 횟수를 구하라

T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    A = [0] * (N+1)
    Stop = list(map(int, input().split()))
    for j in Stop:
        A[j] += j
    print(A)

