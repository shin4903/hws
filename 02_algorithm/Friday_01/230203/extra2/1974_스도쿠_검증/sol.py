import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    sd = []
    result = [0, 0, 0]
    for _ in range(9):
        line = list(map(int, input().split()))
        sd.append(line)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = []
    for l in range(0, 7, 3):
        for j in sd[l: l+3]:
            for k in j[:3]:
                b.append(k)
        b.sort()
        if a == b:
            result[0] += 1
        b.clear()

        for n in sd[l: l+3]:
            for m in n[3:6]:
                b.append(m)
        b.sort()
        if a == b:
            result[0] += 1
        b.clear()

        for o in sd[l: l + 3]:
            for p in o[6:9]:
                b.append(p)
        b.sort()
        if a == b:
            result[0] += 1
        b.clear()


    c = []
    for j in range(9):
        for k in range(9):
            c.append(sd[k][j])
        c.sort()
        if a == c:
            result[2] += 1
        c.clear()

    for i in sd:
        i.sort()
        if i == a:
            result[1] += 1



    if result[0] and result[1] and result[2] == 9:
        print(f'#{tc} {1}')

    else:
        print(f'#{tc} {0}')
