import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, N):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(arr)
    result = []
    for i in range(1,6):
        result.append(arr[-i])
        result.append(arr[i-1])
    print(f'#{tc}', *result)
