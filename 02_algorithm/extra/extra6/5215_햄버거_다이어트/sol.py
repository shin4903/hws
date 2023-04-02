import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1,T+1):
    Ti = []
    Ki = []
    N, cal = map(int,input().split())
    for _ in range(N):
        t, k = map(int,input().split())
        Ti.append(t)
        Ki.append(k)

    max_score = 0
    for i in range(1, 1 << N):
        score = 0
        calo = 0
        for j in range(0, N):
            if i & (1<<j):
                score += Ti[j]
                calo += Ki[j]
                if calo > cal:
                    break
        if calo <= cal:
            max_score = max(score,max_score)
    print(f'#{tc}',max_score)

