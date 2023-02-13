import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    dir = 0
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = [0,0,0]
    A = []
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    for i in range(1,8,3):
        for j in range(1,8,3):
            A.append(arr[i][j])
            for k in range(8):
                A.append(arr[i+dx[dir]][j+dy[dir]])
                dir += 1
                if dir >= 8:
                    dir = 0
            # print(A)
            A.sort()
            if A == B:
                result[0] +=1
                A.clear()

    for i in range(9):
        for j in range(9):
            A.append(arr[i][j])
            A.sort()
            if A == B:
                result[1] += 1
                A.clear()


    for i in range(9):
        for j in range(9):
            if i<j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(9):
        for j in range(9):
            A.append(arr[i][j])
            A.sort()
            if A == B:
                result[2] += 1
                A.clear()
    if result[0] and result[1] and result[2] == 9:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)

