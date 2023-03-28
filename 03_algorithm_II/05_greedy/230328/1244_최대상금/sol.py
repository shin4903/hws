import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    num, cnt = map(str,input().split())
    money = []
    cnt = int(cnt)
    for i in num:
        money.append(int(i))
        t = 0
        con = 0

    while t != cnt and t < len(money):
        tmp = money[:]
        idx = 0
        maxv = 0
        for i in range(t, len(money)):
            if money[i] >= maxv:
                maxv = money[i]
                idx = i
        money[idx] = money[t]
        money[t] = maxv
        if money == tmp:
            cnt += 1
            con += 1
        t += 1

    print(money, t, con)

    if con - t != cnt:
        if con % 2 == 1:
            if money[-2] == money[-3]:
                pass
            else:
                money[-1], money[-2] = money[-2], money[-1]
    if money[0] == money[1] and cnt >= 2:
        if money[-1] > money[-2]:
            money[-2], money[-1] = money[-1], money[-2]

    A = cnt - (t - con)
    if A % 2 == 1:
        if con % 2 == 1:
            if money[-2] == money[-3]:
                pass
            else:
                money[-1], money[-2] = money[-2], money[-1]

    result = ''
    for i in money:
        result += str(i)
    print(f'#{tc}',result)