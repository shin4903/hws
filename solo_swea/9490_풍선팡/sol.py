import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0] # 상,하,좌,우 4방향
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]


    maxV = 0 # 최종 출력할 최대값
    for x in range(N):
        # x : data의 행 인덱스
        for y in range(M):
            # y : data의 열 인덱스
            cnt = data[x][y] # 꽃가루 합
            for i in range(4): # 네방향 조사
                for j in range(1,data[x][y]+1):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0 <= nx < N and 0 <= ny < M:
                        cnt += data[nx][ny]
            if cnt > maxV:
                maxV = cnt
    print(f'#{tc}',maxV)