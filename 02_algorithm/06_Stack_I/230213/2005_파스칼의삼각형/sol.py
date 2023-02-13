import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for x in range(N):
        for y in range(N):
            nx = x - 1
            ny = y - 1
            if 0 <= nx < N and 0 <= ny < N:
                arr[x][y] = arr[nx][ny] + arr[nx][y]
            if ny < 0 and 0 <= nx < N:
                arr[x][y] = arr[nx][y]

    print(f'#{tc}')
    arr2 = []
    for i in arr:
        for j in range(len(i)):
            if i[j] != 0:
                arr2.append(str(i[j]))

        print(' '.join(arr2))
        arr2.clear()
