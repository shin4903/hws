import sys
sys.stdin = open('input.txt')

def back(i, tmp):
    global result
    if i >= 12:
        result = min(result, tmp)
        return

    if tmp >= result:
        return


    for k in range(4):
        if k == 0:
            back(i+1, tmp+plan[i]*cost[0])
        elif k == 1:
            if plan[i]:
                back(i+1, tmp + cost[1])
        elif k == 2:
            if plan[i]:
                for l in range(i,i+3):
                    if l < 12:
                        back(i+3, tmp+cost[2])
        else:
            back(i + 12, tmp + cost[3])




T = int(input())

for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    plan = list(map(int,input().split()))

    result = 10000000000

    back(0,0)
    print(f'#{tc}',result)