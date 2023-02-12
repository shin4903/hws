import sys
sys.stdin = open('input.text')

for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for _ in range(N):
        arr[-1] -= 1
        arr[0] += 1
        for i in range(len(arr) - 1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr[-1] - arr[0])