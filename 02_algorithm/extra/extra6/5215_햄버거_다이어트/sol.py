import sys
sys.stdin = open('input.txt')

def backtrackin(idx ,tmpsco, tmpcal):
    if tmpcal > cal:
        return
    if score <= tmpsco:
        return
    for i in range(N):
        tmpsco += Ti[idx]
        tmpcal += Ki[idx]
        idx += 1
        backtrackin(idx, tmpsco, tmpcal)


T = int(input())

for tc in range(1,T+1):
    Ti = []
    Ki = []
    N, cal = map(int,input().split())
    for _ in range(N):
        t, k = map(int,input().split())
        Ti.append(t)
        Ki.append(k)

    score = 0

    backtrackin(0,0,0)
    print()