import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    two = list(map(int,input()))
    the = list(map(str,input()))
    twolist = []
    thelist = []
    # 2진수
    for i in range(len(two)):
        if two[i] == 1:
            two[i] = 0
        else:
            two[i] = 1
        x = 0
        result = 0
        for j in range(len(two)-1,-1,-1):
            if two[j] == 1:
                result += 2**x
            x +=1
        twolist.append(result)
        if two[i] == 1:
            two[i] = 0
        else:
            two[i] = 1


    # 3진수
    for i in range(len(the)):
        tmp = the[:]
        if tmp[i] == '2':
            tmp[i] = '1'
            y = ''.join(tmp)
            thelist.append(int(y,3))

            tmp[i] = '0'
            y = ''.join(tmp)
            thelist.append(int(y, 3))

        elif tmp[i] == '1':
            tmp[i] = '2'
            y = ''.join(tmp)
            thelist.append(int(y, 3))

            tmp[i] = '0'
            y = ''.join(tmp)
            thelist.append(int(y, 3))

        elif tmp[i] == '0':
            tmp[i] = '1'
            y = ''.join(tmp)
            thelist.append(int(y, 3))

            tmp[i] = '2'
            y = ''.join(tmp)
            thelist.append(int(y, 3))


    ans = [x for x in twolist if x in thelist]
    print(f'#{tc}',ans[0])