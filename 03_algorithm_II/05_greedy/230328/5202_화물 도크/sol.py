import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    result = 1
    N = int(input())
    data = []
    for i in range(N):
        i = list(map(int,input().split()))
        if i not in data:
            data.append(i)
    data.sort(key= lambda x : (x[1],x[0]))
    s = data[0][1]
    for i in range(1,len(data)):
        if s <= data[i][0]:
            result += 1
            s = data[i][1]
    print(f'#{tc}',result)