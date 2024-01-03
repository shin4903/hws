import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    room.sort()
    cnt = 1
    for i in range(len(room)-1):
        if room[i][0] < room[i+1][0] < room[i][1]:
            cnt += 1
    print(f'#{tc}', cnt)
